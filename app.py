import os
from pathlib import Path

import duckdb
import pandas as pd
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

APP_NAME = "EVisionary"

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "data" / "unified_EVmetadata_enriched.parquet"

if not DATA_PATH.exists():
    raise FileNotFoundError(f"Enriched Parquet dataset not found: {DATA_PATH}")

# ---------------------------------------------------------
# Database initialization
# ---------------------------------------------------------
con = duckdb.connect(database=":memory:")
con.execute(f"CREATE VIEW ev AS SELECT * FROM read_parquet('{DATA_PATH.as_posix()}')")

# ---------------------------------------------------------
# Constants
# ---------------------------------------------------------
MISSING_LIKE = {"", "unknown", "nan", "none", "null", "n/a", "-", "not reported"}

DISPLAY_COLUMNS = [
    "record_uid",
    "source_row_uid",
    "pre_dedup_uid",
    "pmid",
    "sample_name",
    "working_id",
    "molecule_type_raw",
    "molecule_type_norm",
    "molecule_type_group",
    "molecule_type",
    "method",
    "species",
    "year",
    "disease",
    "vesicle",
    "characterization",
    "ev_metric",
    "source",
    "metadata_utility_score",
    "metadata_score_band",
    "source_priority",
    "molecule_raw_norm_discrepant",
    "molecule_norm_alias_discrepant"
]

SEARCH_FIELDS = [
    ("working_id", 4.0),
    ("molecule_type_norm", 3.0),
    ("molecule_type_group", 2.5),
    ("molecule_type_raw", 2.0),
    ("species", 2.0),
    ("sample_name", 2.0),
    ("disease", 2.0),
    ("method", 1.5),
    ("vesicle", 1.5),
    ("source", 1.0),
    ("pmid", 1.0)
]

MAX_LIMIT = 500
DEFAULT_LIMIT = 500


# ---------------------------------------------------------
# Helpers
# ---------------------------------------------------------
def normalize_input(value):
    return (value or "").strip()


def normalize_limit(value, default=DEFAULT_LIMIT, max_limit=MAX_LIMIT):
    try:
        value = int(value)
    except (TypeError, ValueError):
        return default
    if value < 1:
        return default
    return min(value, max_limit)


def clean_text(val):
    if pd.isna(val):
        return "Unknown"
    text = str(val).strip()
    if text.casefold() in MISSING_LIKE:
        return "Unknown"
    return " ".join(text.replace("_", " ").split())


def clean_pmid(val):
    text = clean_text(val)
    if text == "Unknown":
        return text
    return text.replace(".0", "")


def clean_year(val):
    text = clean_text(val)
    if text == "Unknown":
        return text
    return text.replace(".0", "")


def build_search_sql(has_query: bool, has_source: bool, has_species: bool, has_group: bool):
    select_cols = ", ".join(DISPLAY_COLUMNS)

    if has_query:
        score_parts = []
        text_where_parts = []

        for field, weight in SEARCH_FIELDS:
            score_parts.append(f"""
                CASE
                    WHEN LOWER(COALESCE(CAST({field} AS VARCHAR), '')) = ? THEN {weight}
                    WHEN regexp_matches(LOWER(COALESCE(CAST({field} AS VARCHAR), '')), ?) THEN {weight * 0.7}
                    WHEN LOWER(COALESCE(CAST({field} AS VARCHAR), '')) LIKE ? THEN {weight * 0.4}
                    ELSE 0
                END
            """)
            text_where_parts.append(
                f"LOWER(COALESCE(CAST({field} AS VARCHAR), '')) LIKE ?"
            )

        retrieval_score_sql = f"""
        (
            {" + ".join(score_parts)}
            + CASE WHEN pmid__informative = 1 THEN 0.3 ELSE 0 END
            + CASE WHEN species__informative = 1 THEN 0.2 ELSE 0 END
            + CASE WHEN sample_name__informative = 1 THEN 0.2 ELSE 0 END
            + CASE WHEN source = 'EV-TRACK' AND ev_metric__informative = 1 THEN 0.2 ELSE 0 END
        ) AS retrieval_rank_score
        """

        sql = f"SELECT {select_cols}, {retrieval_score_sql} FROM ev"
        where_clauses = [f"({' OR '.join(text_where_parts)})"]

    else:
        sql = f"SELECT {select_cols}, 0.0 AS retrieval_rank_score FROM ev"
        where_clauses = []

    if has_source:
        where_clauses.append("source = ?")

    if has_species:
        where_clauses.append("species = ?")

    if has_group:
        where_clauses.append("molecule_type_group = ?")

    if where_clauses:
        sql += " WHERE " + " AND ".join(where_clauses)

    sql += """
    ORDER BY
        retrieval_rank_score DESC,
        metadata_utility_score DESC,
        source_priority DESC,
        TRY_CAST(year AS INTEGER) DESC NULLS LAST,
        record_uid
    LIMIT ?
    """
    return sql


def build_query_params(query, source_filter, species_filter, molecule_group_filter):
    params = []

    if query:
        q_cf = query.casefold()
        q_like = f"%{q_cf}%"
        q_regex = rf"(^|[^a-z0-9]){q_cf}([^a-z0-9]|$)"

        for _field, _weight in SEARCH_FIELDS:
            params.extend([q_cf, q_regex, q_like])

        for _field, _weight in SEARCH_FIELDS:
            params.append(q_like)

    if source_filter:
        params.append(source_filter)

    if species_filter:
        params.append(species_filter)

    if molecule_group_filter:
        params.append(molecule_group_filter)

    return params


def row_to_output(rd):
    return {
        "record_uid": clean_text(rd.get("record_uid")),
        "source_row_uid": clean_text(rd.get("source_row_uid")),
        "pre_dedup_uid": clean_text(rd.get("pre_dedup_uid")),
        "name": clean_text(rd.get("working_id")),
        "type": clean_text(rd.get("molecule_type")),
        "type_raw": clean_text(rd.get("molecule_type_raw")),
        "type_norm": clean_text(rd.get("molecule_type_norm")),
        "type_group": clean_text(rd.get("molecule_type_group")),
        "species": clean_text(rd.get("species")),
        "sample": clean_text(rd.get("sample_name")),
        "method": clean_text(rd.get("method")),
        "vesicle": clean_text(rd.get("vesicle")),
        "disease": clean_text(rd.get("disease")),
        "characterization": clean_text(rd.get("characterization")),
        "ev_metric": clean_text(rd.get("ev_metric")),
        "year": clean_year(rd.get("year")),
        "pmid": clean_pmid(rd.get("pmid")),
        "source": clean_text(rd.get("source")),
        "metadata_utility_score": round(float(rd.get("metadata_utility_score", 0) or 0), 3),
        "metadata_score_band": clean_text(rd.get("metadata_score_band")),
        "retrieval_rank_score": round(float(rd.get("retrieval_rank_score", 0) or 0), 3),
        "raw_norm_discrepant": int(rd.get("molecule_raw_norm_discrepant", 0) or 0),
        "norm_alias_discrepant": int(rd.get("molecule_norm_alias_discrepant", 0) or 0)
    }


def search_duckdb(query=None, limit=DEFAULT_LIMIT, source_filter=None, species_filter=None, molecule_group_filter=None):
    query = normalize_input(query)
    source_filter = normalize_input(source_filter)
    species_filter = normalize_input(species_filter)
    molecule_group_filter = normalize_input(molecule_group_filter)
    limit = normalize_limit(limit)

    has_query = bool(query)
    has_source = bool(source_filter)
    has_species = bool(species_filter)
    has_group = bool(molecule_group_filter)

    if not any([has_query, has_source, has_species, has_group]):
        return []

    sql = build_search_sql(
        has_query=has_query,
        has_source=has_source,
        has_species=has_species,
        has_group=has_group
    )

    params = build_query_params(
        query=query,
        source_filter=source_filter,
        species_filter=species_filter,
        molecule_group_filter=molecule_group_filter
    )
    params.append(limit)

    try:
        result = con.execute(sql, params)
        rows = result.fetchall()
        cols = [d[0] for d in result.description]

        output = []
        for row in rows:
            rd = dict(zip(cols, row))
            output.append(row_to_output(rd))

        return output

    except Exception as e:
        print("Backend query error:", e)
        return []


def get_distinct_values():
    try:
        sources = [
            r[0] for r in con.execute(
                """
                SELECT DISTINCT source
                FROM ev
                WHERE source IS NOT NULL
                  AND TRIM(source) <> ''
                  AND LOWER(source) NOT IN ('unknown', 'nan', 'none', 'null', 'n/a', '-', 'not reported')
                ORDER BY source
                """
            ).fetchall()
        ]

        species = [
            r[0] for r in con.execute(
                """
                SELECT DISTINCT species
                FROM ev
                WHERE species IS NOT NULL
                  AND TRIM(species) <> ''
                  AND LOWER(species) NOT IN ('unknown', 'nan', 'none', 'null', 'n/a', '-', 'not reported')
                ORDER BY species
                LIMIT 300
                """
            ).fetchall()
        ]

        molecule_groups = [
            r[0] for r in con.execute(
                """
                SELECT DISTINCT molecule_type_group
                FROM ev
                WHERE molecule_type_group IS NOT NULL
                  AND TRIM(molecule_type_group) <> ''
                  AND LOWER(molecule_type_group) NOT IN ('unknown', 'nan', 'none', 'null', 'n/a', '-', 'not reported')
                ORDER BY molecule_type_group
                """
            ).fetchall()
        ]

        return {
            "sources": sources,
            "species": species,
            "molecule_groups": molecule_groups
        }

    except Exception as e:
        print("Filter endpoint error:", e)
        return {
            "sources": [],
            "species": [],
            "molecule_groups": []
        }


# ---------------------------------------------------------
# Routes
# ---------------------------------------------------------
@app.route("/")
def index():
    return render_template("index.html", app_name=APP_NAME)


@app.route("/search")
def search():
    q = request.args.get("q", "")
    source_filter = request.args.get("source", "")
    species_filter = request.args.get("species", "")
    molecule_group_filter = request.args.get("molecule_group", "")
    limit = request.args.get("limit", DEFAULT_LIMIT)

    results = search_duckdb(
        query=q,
        limit=limit,
        source_filter=source_filter,
        species_filter=species_filter,
        molecule_group_filter=molecule_group_filter
    )
    return jsonify(results)


@app.route("/filters")
def filters():
    return jsonify(get_distinct_values())


# Optional lightweight health check
@app.route("/health")
def health():
    try:
        row_count = con.execute("SELECT COUNT(*) FROM ev").fetchone()[0]
        return jsonify({
            "status": "ok",
            "app": APP_NAME,
            "dataset": DATA_PATH.name,
            "rows": int(row_count)
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500


# ---------------------------------------------------------
# Entry point
# ---------------------------------------------------------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port, debug=False)
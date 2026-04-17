import os
import duckdb
import pandas as pd
from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

APP_NAME = "EVisionary"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "data", "unified_EVmetadata.parquet")

con = duckdb.connect(database=':memory:')

def clean_text(val):
    if pd.isna(val) or str(val).lower() in ["none", "nan", "null", "", "n/a", "unknown"]: return "Unknown"
    return " ".join(str(val).replace("_", " ").split())

def search_duckdb(query, limit=1000):
    try:
        if not os.path.exists(DATA_PATH):
            print(f"CRITICAL ERROR: File not found at {DATA_PATH}")
            return []

        cols = ["working_id", "molecule_type", "species", "sample_name", "method", "vesicle", "disease", "year", "pmid", "source", "ev_metric", "characterization"]
        
        safe_q = query.replace("'", "''").lower()
        
        where = " OR ".join([f"LOWER(\"{c}\") LIKE '%{safe_q}%'" for c in cols if c not in ['ev_metric']])
        
        sql = f"SELECT * FROM '{DATA_PATH}' WHERE {where} ORDER BY year DESC NULLS LAST LIMIT {limit}"
        
        rows = con.execute(sql).fetchall()
        db_cols = [d[0] for d in con.description]
        
        output = []
        for r in rows:
            rd = dict(zip(db_cols, r))
            
            raw_pmid = rd.get('pmid', 'Unknown')
            if pd.isna(raw_pmid) or str(raw_pmid).lower() in ['nan', 'none', 'unknown', '']:
                final_pmid = "Unknown"
            else:
                final_pmid = str(raw_pmid).replace('.0', '').strip()

            output.append({
                "name": clean_text(rd.get('working_id')),
                "type": clean_text(rd.get('molecule_type')),
                "species": clean_text(rd.get('species')),
                "sample": clean_text(rd.get('sample_name')),
                "method": clean_text(rd.get('method')),
                "vesicle": clean_text(rd.get('vesicle')),
                "disease": clean_text(rd.get('disease')),
                "characterization": clean_text(rd.get('characterization', 'Not Reported')),
                "ev_metric": clean_text(rd.get('ev_metric', 'Legacy')),
                "year": str(rd.get('year')).replace('.0', '') if rd.get('year') else "Unknown",
                "pmid": final_pmid,
                "source": clean_text(rd.get('source'))
            })
        return output
    except Exception as e:
        print("Backend Query Error:", e)
        return []

@app.route("/")
def index():
    return render_template("index.html", app_name=APP_NAME)

@app.route("/search")
def search():
    q = request.args.get("q", "")
    return jsonify(search_duckdb(q))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

"""
Single source of truth for the EVisionary pipeline.

Every harmonization, enrichment, application, and validation script imports
constants and helpers from this module to guarantee numerical consistency
across the manuscript and all supplementary tables.
"""

import re
from pathlib import Path
import pandas as pd

# ---------------------------------------------------------
# Paths (key_B).
# ---------------------------------------------------------
REPO_ROOT = Path(__file__).resolve().parent

LOCAL_KEYB_OUTPUT_DIR = Path("/Users/sogand/EVisionary_outputs_keyB")
REPO_DATA_DIR = REPO_ROOT / "data"

KEYB_OUTPUT_DIR = (
    LOCAL_KEYB_OUTPUT_DIR if LOCAL_KEYB_OUTPUT_DIR.exists() else REPO_DATA_DIR
)

DATA_PATH_MASTER = str(KEYB_OUTPUT_DIR / "unified_EVmetadata_keyB.parquet")
DATA_PATH_ENRICHED = str(KEYB_OUTPUT_DIR / "unified_EVmetadata_enriched.parquet")

# ---------------------------------------------------------
# Single canonical missing-like token set.
# ---------------------------------------------------------
MISSING_LIKE = {
    "", "-", "--", ".", "n/a", "na", "nan", "nd", "none",
    "not available", "not reported", "null", "unavailable",
    "unknown", "unknown/other", "unnamed", "unspecified",
    "not applicable", "not provided", "unk", "metadata",
}

# ---------------------------------------------------------
# Single source-priority dictionary (matches enrichment output).
# ---------------------------------------------------------
SOURCE_PRIORITY = {"EV-TRACK": 3, "Vesiclepedia": 2, "ExoCarta": 1}

SOURCE_DISPLAY_ORDER = ["ExoCarta", "Vesiclepedia", "EV-TRACK"]

# ---------------------------------------------------------
# Recognised binomial scientific names eligible for italic rendering.
# ---------------------------------------------------------
KNOWN_SCIENTIFIC = {
    "Homo sapiens", "Mus musculus", "Rattus norvegicus", "Bos taurus",
    "Sus scrofa", "Drosophila melanogaster", "Canis lupus familiaris",
    "Escherichia coli", "Ovis aries", "Equus caballus", "Gallus gallus",
    "Pseudomonas aeruginosa", "Neisseria meningitidis", "Staphylococcus aureus",
    "Porphyromonas gingivalis", "Acinetobacter baumannii", "Salmonella enterica",
    "Helicobacter pylori", "Vibrio cholerae",
}

# ---------------------------------------------------------
# Canonical molecule-type normalization rule.
#
# This lightweight, documented mapping defines the EXPECTED canonical
# label for a given raw molecular annotation. It is used only to decide
# whether a raw -> normalized transformation is an expected harmonization
# outcome or a genuine inconsistency. It does NOT overwrite the stored
# molecule_type_norm produced by the main harmonization pipeline.
# ---------------------------------------------------------
CANONICAL_MOLECULE_MAP = {
    "protein": "Protein",
    "proteins": "Protein",
    "mrna": "mRNA",
    "messenger rna": "mRNA",
    "mirna": "miRNA",
    "micro rna": "miRNA",
    "microrna": "miRNA",
    "lipid": "Lipid",
    "lipids": "Lipid",
}

# Canonical labels that represent an intentional "no specific class" mapping.
UNSPECIFIED_MOLECULE_CANONICAL = {"Unknown/Other", "Unknown"}


def normalize_molecule_type(value):
    """
    Return the expected canonical molecule-type label for a raw value.

    Missing-like inputs are mapped to 'Unknown/Other'. Recognised raw
    tokens are mapped to their canonical class. Unrecognised but informative
    tokens are returned in a standardized title form so that pure
    capitalization differences are not treated as discrepancies.
    """
    if value is None or (isinstance(value, float) and pd.isna(value)):
        return "Unknown/Other"

    text = str(value).strip()
    if text == "" or text.casefold() in MISSING_LIKE:
        return "Unknown/Other"

    return CANONICAL_MOLECULE_MAP.get(text.casefold(), text)


# ---------------------------------------------------------
# Canonical query definitions.
# ---------------------------------------------------------
QUERY_PATTERNS = {
    "Protein": r"^protein$",
    "mRNA": r"^mrna$",
    "miRNA": r"^mirna$",
    "Lipid": r"^lipid$",
    "Plasma": r"\bplasma\b",
    "Breast Cancer": r"\bbreast[-\s]+cancer\b",
    "Homo sapiens": r"\bhomo\s+sapiens\b",
}

MOLECULE_CONCEPTS = [
    ("Protein", "protein", r"^protein$"),
    ("mRNA",    "mrna",    r"^mrna$"),
    ("miRNA",   "mirna",   r"^mirna$"),
    ("Lipid",   "lipid",   r"^lipid$"),
]

FIELDS_WITH_RAW_STAGE = {"molecule_type"}

# ---------------------------------------------------------
# Shared text helpers
# ---------------------------------------------------------
def valid_text_series(s):
    """Trim, stringify, and blank-out missing-like tokens (casefold-based)."""
    s_clean = s.fillna("").astype(str).str.strip()
    return s_clean.mask(s_clean.str.casefold().isin(MISSING_LIKE), "")


def contains_ci(series, pattern):
    """Case-insensitive regex match."""
    return series.str.contains(pattern, case=False, regex=True, na=False)


def count_unique_pmids(df, mask):
    pm = valid_text_series(df.loc[mask, "pmid"])
    return int(pm[pm != ""].nunique())


def count_unique_sources(df, mask):
    src = valid_text_series(df.loc[mask, "source"])
    return int(src[src != ""].nunique())


def summarize_sources(df, mask):
    s = valid_text_series(df.loc[mask, "source"])
    s = s[s != ""]
    if s.empty:
        return ""
    return " | ".join(f"{src}:{cnt}" for src, cnt in s.value_counts().items())


def safe_records_per_pmid(n_records, n_pmids):
    return round(n_records / n_pmids, 2) if n_pmids > 0 else None


def safe_fold_change(base, target):
    return round(target / base, 2) if base > 0 else None


# ---------------------------------------------------------
# PMID helper (shared by backend and validation)
# ---------------------------------------------------------
_PMID_NUMERIC = re.compile(r"^\d+$")


def clean_pmid_value(val):
    """Return a cleaned PMID string or 'Unknown'."""
    if val is None or (isinstance(val, float) and pd.isna(val)):
        return "Unknown"
    text = str(val).strip()
    if text == "" or text.casefold() in MISSING_LIKE:
        return "Unknown"
    return text.replace(".0", "")


def pmid_to_pubmed_url(val):
    """Return a valid PubMed URL only for a purely numeric PMID."""
    pmid = clean_pmid_value(val)
    if pmid == "Unknown":
        return None
    if not _PMID_NUMERIC.match(pmid):
        return None
    return f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"


# ---------------------------------------------------------
# Italic species helpers (display layer only)
# ---------------------------------------------------------
def species_to_html(val):
    """For web/JSON display. Wraps recognised binomials in <i> tags."""
    text = "" if pd.isna(val) else str(val).strip()
    if text == "" or text.casefold() in MISSING_LIKE:
        return "Unknown"
    parts = [p.strip() for p in re.split(r"\s*\|\s*", text)]
    return " | ".join(
        f"<i>{p}</i>" if p in KNOWN_SCIENTIFIC else p for p in parts
    )


def italicize_species_label(label):
    """For matplotlib figures (mathtext)."""
    if label is None or str(label).strip() == "":
        return str(label)
    if str(label).strip().casefold() in MISSING_LIKE:
        return "Unknown"
    out = []
    for p in re.split(r"\s*\|\s*", str(label)):
        p = p.strip()
        if p in KNOWN_SCIENTIFIC:
            t = p.split()
            sci = r"$\it{" + " ".join(t[:2]).replace(" ", r"\ ") + r"}$"
            out.append((sci + " " + " ".join(t[2:])).strip())
        else:
            out.append(p)
    return " | ".join(out)
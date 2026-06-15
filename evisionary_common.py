# evisionary_common.py
"""
Single source of truth for the EVisionary pipeline.

Every harmonization, enrichment, application, and validation script imports
constants and helpers from this module to guarantee numerical consistency
across the manuscript and all supplementary tables.
"""

import re
import os
from pathlib import Path
import pandas as pd

# ---------------------------------------------------------
# Paths (key_B).
# ---------------------------------------------------------
KEYB_OUTPUT_DIR = "/Users/sogand/EVisionary_outputs_keyB"
Path(KEYB_OUTPUT_DIR).mkdir(parents=True, exist_ok=True)

DATA_PATH_MASTER = os.path.join(KEYB_OUTPUT_DIR, "unified_EVmetadata_keyB.parquet")
DATA_PATH_ENRICHED = os.path.join(KEYB_OUTPUT_DIR, "unified_EVmetadata_enriched.parquet")

# ---------------------------------------------------------
# Single canonical missing-like token set.
# Used identically for completeness, informativeness, and PMID counting.
# ---------------------------------------------------------
MISSING_LIKE = {
    "", "-", "--", ".", "n/a", "na", "nan", "nd", "none",
    "not available", "not reported", "null", "unavailable",
    "unknown", "unknown/other", "unnamed", "unspecified",
    "not applicable", "not provided", "unk", "metadata",
}

# ---------------------------------------------------------
# Single source-priority dictionary (matches enrichment output).
# Higher value is preferred in deterministic ranking tie-breaks.
# ---------------------------------------------------------
SOURCE_PRIORITY = {"EV-TRACK": 3, "Vesiclepedia": 2, "ExoCarta": 1}

# Display-only ordering for source-combination strings (not a priority claim).
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
# Single canonical query definitions. ONE pattern per concept,
# used by every validation script to keep counts identical.
#
# Controlled fields (molecule_type) use anchored exact patterns.
# Free-text fields (sample_name, disease) use word-boundary patterns.
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
# Fields that have a genuine raw -> normalized -> canonical chain.
# Only molecule_type qualifies; others are lexical-stabilization only.
FIELDS_WITH_RAW_STAGE = {"molecule_type"}

# ---------------------------------------------------------
# Shared text helpers
# ---------------------------------------------------------
def valid_text_series(s):
    """Trim, stringify, and blank-out missing-like tokens (casefold-based)."""
    s_clean = s.fillna("").astype(str).str.strip()
    return s_clean.mask(s_clean.str.casefold().isin(MISSING_LIKE), "")

def contains_ci(series, pattern):
    """Case-insensitive regex match. Use everywhere instead of inline (?i)."""
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
# Italic species helpers (display layer only; never written to Parquet)
# ---------------------------------------------------------
def species_to_html(val):
    """For web/JSON display. Wraps recognised binomials in <i> tags."""
    text = "" if pd.isna(val) else str(val).strip()
    if text == "" or text.casefold() in MISSING_LIKE:
        return "Unknown"
    parts = [p.strip() for p in re.split(r"\s*\|\s*", text)]
    return " | ".join(f"<i>{p}</i>" if p in KNOWN_SCIENTIFIC else p for p in parts)

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
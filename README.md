
```markdown
<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=rect&height=120&color=0:1f4e79,55:228B22,100:DAA520&text=EVisionary&fontColor=ffffff&fontSize=42&fontAlignY=45&desc=Provenance-aware%20EV%20repository%20harmonization&descAlignY=72&descSize=16" alt="EVisionary header" />
</p>

<p align="center">
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.10-228B22?labelColor=1f4e79" alt="Python"></a>
  <a href="https://duckdb.org/"><img src="https://img.shields.io/badge/DuckDB-query%20engine-DAA520?labelColor=1f4e79" alt="DuckDB"></a>
  <a href="https://flask.palletsprojects.com/"><img src="https://img.shields.io/badge/Flask-web%20interface-E0E0E0?labelColor=1f4e79" alt="Flask"></a>
  <a href="https://parquet.apache.org/"><img src="https://img.shields.io/badge/Apache%20Parquet-local%20snapshot-228B22?labelColor=1f4e79" alt="Apache Parquet"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-DAA520?labelColor=1f4e79" alt="License"></a>
  <a href="https://evisionary.onrender.com/"><img src="https://img.shields.io/badge/Demo-Render-228B22?labelColor=1f4e79" alt="Demo"></a>
</p>

<h1><span style="color:#1f4e79">EVisionary</span></h1>

**A snapshot-based, provenance-aware framework for harmonizing and querying extracellular vesicle repositories**

---

<h2><span style="color:#1f4e79">Overview</span></h2>

EVisionary is a local, snapshot-based framework developed to harmonize and query extracellular vesicle (EV) repository data while preserving original source provenance. By integrating dated exports from **Vesiclepedia**, **ExoCarta**, and **EV-TRACK**, it creates a unified, locally queryable resource designed specifically for reproducible EV data reuse.

In standard EV bioinformatics workflows, researchers face a practical limitation: existing repositories contain complementary but structurally heterogeneous information. Vesiclepedia and ExoCarta primarily report molecular cargo, whereas EV-TRACK captures study-level reporting metadata. Differences in schemas, terminologies, annotation depths, and query behaviors make cross-repository searches notoriously difficult to reproduce and interpret.

To address this, EVisionary harmonizes these disparate sources conservatively. It standardizes selected key fields, retains all raw annotations, preserves repository identity, and strictly avoids unsupported biological inference. Any missing or ambiguous value is represented explicitly as `Unknown`.

> **Note:** EVisionary is **not** a live federated query engine. It operates on dated local snapshots to prioritize reproducibility, full auditability, and stable query behavior over time.

**Live Demo:** [https://evisionary.onrender.com/](https://evisionary.onrender.com/)

---

<h2><span style="color:#1f4e79">Motivation</span></h2>

While EV repositories are individually valuable, they are often incomplete when used in isolation. Details such as cargo-level evidence, disease context, biofluid annotations, species information, and methodological metadata are not consistently captured across sources or at the same level of granularity.

A naive integration approach typically introduces two major issues:

1. **Simple concatenation** may duplicate existing evidence, fragment equivalent labels, or obscure the original source of a record.
2. **Over-harmonization** may collapse labels into unsupported biological equivalences, leading to inaccurate assumptions.

EVisionary takes a conservative middle path: it improves cross-repository search capability while keeping provenance, scientific uncertainty, and metadata sparsity fully transparent to the researcher.

---

<h2><span style="color:#1f4e79">Key Features</span></h2>

| <span style="color:#228B22">**Feature**</span> | <span style="color:#228B22">**Description**</span> |
|---|---|
| <span style="color:#1f4e79">**Snapshot-based integration**</span> | Uses dated local exports instead of live, unpredictable repository API calls |
| <span style="color:#1f4e79">**Provenance preservation**</span> | Retains strict source identity through normalization and deduplication |
| <span style="color:#1f4e79">**Conservative harmonization**</span> | Normalizes selected fields without unsupported semantic inference |
| <span style="color:#1f4e79">**Multi-cargo support**</span> | Includes protein, mRNA, miRNA, lipid, and study-level EV-TRACK records |
| <span style="color:#1f4e79">**Local query backend**</span> | Apache Parquet storage queried via DuckDB for fast local execution |
| <span style="color:#1f4e79">**Web interface**</span> | Free-text and filter search, summary plots, PubMed links, utility scores, CSV export |
| <span style="color:#1f4e79">**Audit support**</span> | Comprehensive validation outputs for completeness, stability, and complementarity |

---

<h2><span style="color:#1f4e79">Current Snapshot Statistics</span></h2>

| <span style="color:#228B22">**Metric**</span> | <span style="color:#228B22">**Value**</span> |
|---|---:|
| <span style="color:#1f4e79">**Source rows processed**</span> | 713,667 |
| <span style="color:#1f4e79">**Final harmonized records**</span> | 258,460 |
| <span style="color:#1f4e79">**Cargo-level records**</span> | 253,491 |
| <span style="color:#1f4e79">**Study-level EV-TRACK records**</span> | 4,969 |
| <span style="color:#1f4e79">**Vesiclepedia records**</span> | 195,488 |
| <span style="color:#1f4e79">**ExoCarta records**</span> | 58,003 |
| <span style="color:#1f4e79">**Missing or unusable method field**</span> | 16.87% |

---

<h2><span style="color:#1f4e79">Molecular Cargo Composition</span></h2>

| <span style="color:#228B22">**Molecular Class**</span> | <span style="color:#228B22">**Total Records**</span> | <span style="color:#228B22">**Unique PMIDs**</span> |
|---|---:|---:|
| <span style="color:#1f4e79">**Protein**</span> | 207,623 | 569 |
| <span style="color:#1f4e79">**mRNA**</span> | 26,701 | 26 |
| <span style="color:#1f4e79">**miRNA**</span> | 16,131 | 120 |
| <span style="color:#1f4e79">**Lipid**</span> | 2,896 | 52 |

*Note: disease annotations were available in only 4,949 records (1.92% of the harmonized snapshot), highlighting persistent metadata sparsity even after cross-repository integration.*

---

<h2><span style="color:#1f4e79">Source Complementarity</span></h2>

| <span style="color:#228B22">**Molecular Class**</span> | <span style="color:#228B22">**Vesiclepedia**</span> | <span style="color:#228B22">**ExoCarta**</span> | <span style="color:#228B22">**Dominant Pattern**</span> |
|---|---:|---:|---|
| <span style="color:#1f4e79">**Protein**</span> | 160,806 | 46,817 | Vesiclepedia-dominant |
| <span style="color:#1f4e79">**mRNA**</span> | 23,307 | 3,394 | Vesiclepedia-dominant |
| <span style="color:#1f4e79">**miRNA**</span> | 10,091 | 6,040 | Shared coverage |
| <span style="color:#1f4e79">**Lipid**</span> | 1,283 | 1,613 | ExoCarta-dominant |

The integrated snapshot demonstrates that EV repositories are complementary rather than interchangeable, while biofluid and disease annotations remain sparse and source-dependent.

---

<h2><span style="color:#1f4e79">Example Queries in Practice</span></h2>

| <span style="color:#228B22">**Use Case**</span> | <span style="color:#228B22">**Query Logic**</span> | <span style="color:#228B22">**Records**</span> | <span style="color:#228B22">**PMIDs**</span> | <span style="color:#228B22">**Interpretation**</span> |
|---|---|---:|---:|---|
| <span style="color:#1f4e79">**Protein cargo**</span> | `molecule_type = Protein` | 207,623 | 569 | Broad, high-volume cargo retrieval |
| <span style="color:#1f4e79">**miRNA cargo**</span> | `molecule_type = miRNA` | 16,131 | 120 | Canonical miRNA retrieval |
| <span style="color:#1f4e79">**Lipid cargo**</span> | `molecule_type = Lipid` | 2,896 | 52 | Source-complementary coverage |
| <span style="color:#1f4e79">**Plasma context**</span> | `sample_name contains plasma` | 547 | 444 | Biofluid metadata retrievable, source-dependent |
| <span style="color:#1f4e79">**Breast cancer**</span> | `disease contains breast cancer` | 12 | 11 | Highlights severe disease metadata sparsity |
| <span style="color:#1f4e79">**Constrained**</span> | Breast cancer + plasma | 6 | 6 | Limited co-annotation overlap |
| <span style="color:#1f4e79">**Multi-factor**</span> | Breast cancer + plasma + miRNA | 0 | 0 | Distinct metadata granularity gap |

A zero result for the triple-constrained query should **not** be interpreted as biological absence. It indicates that current repository snapshots do not connect cargo, disease, and biofluid annotations at a compatible level of granularity.

---

<h2><span style="color:#1f4e79">Data Model</span></h2>

| <span style="color:#228B22">**Field**</span> | <span style="color:#228B22">**Description**</span> |
|---|---|
| <span style="color:#1f4e79">**source**</span> | Origin repository (Vesiclepedia / ExoCarta / EV-TRACK) |
| <span style="color:#1f4e79">**working_id**</span> | Cargo-level identifier when available |
| <span style="color:#1f4e79">**molecule_type_raw**</span> | Original source-reported molecular label |
| <span style="color:#1f4e79">**molecule_type_norm**</span> | Normalized molecular label for searchability |
| <span style="color:#1f4e79">**molecule_type_group**</span> | Broad molecular class categorization |
| <span style="color:#1f4e79">**species**</span> | Standardized organism name via curated dictionary |
| <span style="color:#1f4e79">**disease**</span> | Disease/clinical context annotation, or `Unknown` |
| <span style="color:#1f4e79">**sample_name**</span> | Biofluid or sample-type annotation, or `Unknown` |
| <span style="color:#1f4e79">**method**</span> | Isolation/detection method as reported by source |
| <span style="color:#1f4e79">**pmid**</span> | PubMed identifier linked directly to the record |
| <span style="color:#1f4e79">**year**</span> | Publication year extracted from source metadata |
| <span style="color:#1f4e79">**ev_metric**</span> | EV-TRACK specific reporting metric |
| <span style="color:#1f4e79">**utility_score**</span> | Record-level triage score |

> **Important:** `utility_score` supports **triage** of query results. It is **not** a biological confidence or experimental validity score. It reflects metadata completeness, query-match quality, source-prioritization rules, and publication recency.

---

<h2><span style="color:#1f4e79">Processing Workflow</span></h2>

```text
┌──────────────────────────────────────────────┐
│ Repository Exports                            │
│ (Vesiclepedia · ExoCarta · EV-TRACK)          │
└───────────────────────┬────────────────────────┘
                         ▼
┌──────────────────────────────────────────────┐
│ Source-Specific Ingestion                     │
└───────────────────────┬────────────────────────┘
                         ▼
┌──────────────────────────────────────────────┐
│ Canonical Field Mapping                       │
│ (Conservative 13-column schema)               │
└───────────────────────┬────────────────────────┘
                         ▼
┌──────────────────────────────────────────────┐
│ Conservative Normalization                    │
│ (No unsupported biological inference)         │
└───────────────────────┬────────────────────────┘
                         ▼
┌──────────────────────────────────────────────┐
│ Provenance-Preserving Deduplication           │
│ (Seven-field source-aware composite key)      │
└───────────────────────┬────────────────────────┘
                         ▼
┌──────────────────────────────────────────────┐
│ Parquet Master Snapshot                       │
│ (Local, reproducible, query-ready resource)   │
└───────────────────────┬────────────────────────┘
                         ▼
┌──────────────────────────────────────────────┐
│ DuckDB Query Backend                          │
│ (Fast local analytical querying)              │
└───────────────────────┬────────────────────────┘
                         ▼
┌──────────────────────────────────────────────┐
│ Flask Web Interface                           │
│ (Search · filters · plots · PubMed links)     │
└───────────────────────┬────────────────────────┘
                         ▼
┌──────────────────────────────────────────────┐
│ Exportable Results                            │
│ (Tables · utility scores · CSV output)        │
└──────────────────────────────────────────────┘
```

---

<h2><span style="color:#1f4e79">Repository Structure</span></h2>

```text
EVisionary/
├── app.py
├── evisionary_common.py
├── ontology_terms.py
├── synonyms.py
├── requirements.txt
├── LICENSE
├── README.md
├── Procfile
├── Scripts/
│   └── app.py
├── data/
├── docs/
├── static/
└── templates/
```

| <span style="color:#228B22">**Path**</span> | <span style="color:#228B22">**Purpose**</span> |
|---|---|
| <span style="color:#1f4e79">`app.py`</span> | Root-level Flask entry point retained for deployment compatibility |
| <span style="color:#1f4e79">`Scripts/app.py`</span> | Primary application execution script |
| <span style="color:#1f4e79">`evisionary_common.py`</span> | Shared helper functions used across the framework |
| <span style="color:#1f4e79">`ontology_terms.py`</span> | Controlled vocabulary and ontology-related logic |
| <span style="color:#1f4e79">`synonyms.py`</span> | Query normalization and synonym resources |
| <span style="color:#1f4e79">`requirements.txt`</span> | Python dependency list |
| <span style="color:#1f4e79">`data/`</span> | Raw data inputs, processed snapshots, validation audit outputs |
| <span style="color:#1f4e79">`docs/`</span> | Documentation and supporting manuscript material |
| <span style="color:#1f4e79">`static/`</span> | Static graphical assets and styling for the web interface |
| <span style="color:#1f4e79">`templates/`</span> | Flask HTML rendering templates |

---

<h2><span style="color:#1f4e79">Utility Score</span></h2>

To support researchers in triaging results during exploratory searches, EVisionary calculates a record-level **utility score**. This score dynamically reflects metadata completeness, query-match quality, source-prioritization rules, and publication recency.

> **Crucial Warning:** The utility score is an auditing and triage tool, **not** a biological confidence score. It must never be interpreted as an indicator of evidence strength, experimental validity, or biological importance.

---

<h2><span style="color:#1f4e79">Installation</span></h2>

```bash
git clone https://github.com/Sogandste/EVisionary.git
cd EVisionary
python3.10 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

---

<h2><span style="color:#1f4e79">Running Locally</span></h2>

```bash
python Scripts/app.py
```

Once running, open your browser at:

```text
http://127.0.0.1:5000
```

---

<h2><span style="color:#1f4e79">Render Deployment</span></h2>

Live instance: [https://evisionary.onrender.com/](https://evisionary.onrender.com/)

```text
web: gunicorn Scripts.app:app
```

*Ensure `static/`, `templates/`, and root deployment files remain in their respective directories unless Flask paths are explicitly updated.*

---

<h2><span style="color:#1f4e79">Programmatic Querying (Python)</span></h2>

```python
import duckdb

parquet_path = "data/processed/unified_EVmetadata_keyB.parquet"
con = duckdb.connect()

query = f"""
SELECT source, molecule_type_norm, working_id, species, disease, sample_name, pmid, year
FROM read_parquet('{parquet_path}')
WHERE lower(molecule_type_norm) = 'mirna'
LIMIT 20
"""

results = con.execute(query).df()
print(results)
```

---

<h2><span style="color:#1f4e79">Framework Validation</span></h2>

| <span style="color:#228B22">**Validation Item**</span> | <span style="color:#228B22">**Result**</span> |
|---|---:|
| <span style="color:#1f4e79">**Initial source rows**</span> | 713,667 |
| <span style="color:#1f4e79">**Final harmonized records**</span> | 258,460 |
| <span style="color:#1f4e79">**Canonical miRNA recovered**</span> | 16,131 |
| <span style="color:#1f4e79">**Missing method field rate**</span> | 16.87% |
| <span style="color:#1f4e79">**Plasma retrieval post-syntax**</span> | 547 records |
| <span style="color:#1f4e79">**Breast cancer retrieval**</span> | 12 records |
| <span style="color:#1f4e79">**Breast cancer + plasma + miRNA**</span> | 0 records |

---

<h2><span style="color:#1f4e79">Limitations</span></h2>

- Absolute dependence on the completeness of source repository data.
- Severe sparsity within disease, biofluid, and clinical-context metadata.
- EV-TRACK data is represented at the study level, not the individual cargo level.
- Absence of default ontology-based semantic expansion (to prevent over-harmonization).
- Utility scores are designed strictly for triage, not as metrics of biological validity.

---

<h2><span style="color:#1f4e79">Appropriate Use Cases</span></h2>

**Recommended for:**
- Rapid, exploratory lookup of EV cargo markers.
- Source-aware, transparent evidence review.
- Pre-experimental candidate validation.
- Repository-informed biomarker hypothesis generation.
- Reproducible workflows for EV data reuse.

**Not recommended for:**
- Definitive claims of biological absence based on zero-result queries.
- Live, real-time federated repository queries.
- Automated, unverified ontology-level entity resolution.
- Direct clinical-grade interpretation without expert review.

---

<h2><span style="color:#1f4e79">Citation</span></h2>

```text
Sogand. EVisionary: a provenance-aware framework for harmonizing and querying extracellular vesicle repositories. GitHub repository, 2026.
```

Repository: [https://github.com/Sogandste/EVisionary](https://github.com/Sogandste/EVisionary)

---

<h2><span style="color:#1f4e79">License</span></h2>

This project is open-sourced under the **MIT License**. See the `LICENSE` file for full details.

---

<h2><span style="color:#1f4e79">Contact and Support</span></h2>

Email: `shayesteh222sowgand@gmail.com`

Issue Tracker: [https://github.com/Sogandste/EVisionary/issues](https://github.com/Sogandste/EVisionary/issues)

---

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=rect&height=35&color=0:1f4e79,55:228B22,100:DAA520&section=footer" alt="footer" />
</p>
```


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

# $\color{#1f4e79}{\textbf{EVisionary}}$

**A snapshot-based, provenance-aware framework for harmonizing and querying extracellular vesicle repositories**

---

## $\color{#1f4e79}{\textbf{Overview}}$

EVisionary is a local, snapshot-based framework developed to harmonize and query extracellular vesicle (EV) repository data while preserving original source provenance. By integrating dated exports from **Vesiclepedia**, **ExoCarta**, and **EV-TRACK**, it creates a unified, locally queryable resource designed specifically for reproducible EV data reuse.

In standard EV bioinformatics workflows, researchers often face a practical limitation: existing repositories contain complementary but structurally heterogeneous information. Vesiclepedia and ExoCarta primarily report molecular cargo, whereas EV-TRACK captures study-level reporting metadata. Differences in schemas, terminologies, annotation depths, and query behaviors make cross-repository searches notoriously difficult to reproduce and interpret.

To address this, EVisionary harmonizes these disparate sources conservatively. It standardizes selected key fields, retains all raw annotations, preserves repository identity, and strictly avoids unsupported biological inference. Any missing or ambiguous value is represented explicitly as `Unknown`.

> **Note:** EVisionary is **not** a live federated query engine. It operates on dated local snapshots to prioritize reproducibility, full auditability, and stable query behavior over time.

**Live Demo:** [https://evisionary.onrender.com/](https://evisionary.onrender.com/)

---

## $\color{#1f4e79}{\textbf{Motivation}}$

While EV repositories are individually valuable, they are often incomplete when used in isolation. Details such as cargo-level evidence, disease context, biofluid annotations, species information, and methodological metadata are not consistently captured across sources or at the same level of granularity.

A naive integration approach typically introduces two major issues:
1. **Simple concatenation** may duplicate existing evidence, fragment equivalent labels, or obscure the original source of a record.
2. **Over-harmonization** may collapse labels into unsupported biological equivalences, leading to inaccurate assumptions.

EVisionary takes a conservative middle path: it improves cross-repository search capability while keeping provenance, scientific uncertainty, and metadata sparsity fully transparent to the researcher.

---

## $\color{#1f4e79}{\textbf{Key Features}}$

| $\color{#228B22}{\textbf{Feature}}$ | $\color{#228B22}{\textbf{Description}}$ |
|---|---|
| $\color{#1f4e79}{\textbf{Snapshot-based integration}}$ | Uses dated local exports instead of live, unpredictable repository API calls |
| $\color{#1f4e79}{\textbf{Provenance preservation}}$ | Retains strict source identity through normalization and deduplication |
| $\color{#1f4e79}{\textbf{Conservative harmonization}}$ | Normalizes selected fields without unsupported semantic inference |
| $\color{#1f4e79}{\textbf{Multi-cargo support}}$ | Includes protein, mRNA, miRNA, lipid, and study-level EV-TRACK records |
| $\color{#1f4e79}{\textbf{Local query backend}}$ | Apache Parquet storage queried via DuckDB for fast local execution |
| $\color{#1f4e79}{\textbf{Web interface}}$ | Free-text and filter search, summary plots, PubMed links, utility scores, CSV export |
| $\color{#1f4e79}{\textbf{Audit support}}$ | Comprehensive validation outputs for completeness, stability, and complementarity |

---

## $\color{#1f4e79}{\textbf{Current Snapshot Statistics}}$

| $\color{#228B22}{\textbf{Metric}}$ | $\color{#228B22}{\textbf{Value}}$ |
|---|---:|
| $\color{#1f4e79}{\textbf{Source rows processed}}$ | 713,667 |
| $\color{#1f4e79}{\textbf{Final harmonized records}}$ | 258,460 |
| $\color{#1f4e79}{\textbf{Cargo-level records}}$ | 253,491 |
| $\color{#1f4e79}{\textbf{Study-level EV-TRACK records}}$ | 4,969 |
| $\color{#1f4e79}{\textbf{Vesiclepedia records}}$ | 195,488 |
| $\color{#1f4e79}{\textbf{ExoCarta records}}$ | 58,003 |
| $\color{#1f4e79}{\textbf{Missing or unusable method field}}$ | 16.87% |

---

## $\color{#1f4e79}{\textbf{Molecular Cargo Composition}}$

| $\color{#228B22}{\textbf{Molecular Class}}$ | $\color{#228B22}{\textbf{Total Records}}$ | $\color{#228B22}{\textbf{Unique PMIDs}}$ |
|---|---:|---:|
| $\color{#1f4e79}{\textbf{Protein}}$ | 207,623 | 569 |
| $\color{#1f4e79}{\textbf{mRNA}}$ | 26,701 | 26 |
| $\color{#1f4e79}{\textbf{miRNA}}$ | 16,131 | 120 |
| $\color{#1f4e79}{\textbf{Lipid}}$ | 2,896 | 52 |

*Note: disease annotations were available in only 4,949 records (1.92% of the harmonized snapshot), highlighting persistent metadata sparsity even after cross-repository integration.*

---

## $\color{#1f4e79}{\textbf{Source Complementarity}}$

| $\color{#228B22}{\textbf{Molecular Class}}$ | $\color{#228B22}{\textbf{Vesiclepedia}}$ | $\color{#228B22}{\textbf{ExoCarta}}$ | $\color{#228B22}{\textbf{Dominant Pattern}}$ |
|---|---:|---:|---|
| $\color{#1f4e79}{\textbf{Protein}}$ | 160,806 | 46,817 | Vesiclepedia-dominant |
| $\color{#1f4e79}{\textbf{mRNA}}$ | 23,307 | 3,394 | Vesiclepedia-dominant |
| $\color{#1f4e79}{\textbf{miRNA}}$ | 10,091 | 6,040 | Shared coverage |
| $\color{#1f4e79}{\textbf{Lipid}}$ | 1,283 | 1,613 | ExoCarta-dominant |

The integrated snapshot demonstrates that EV repositories are complementary rather than interchangeable, while biofluid and disease annotations remain sparse and source-dependent.

---

## $\color{#1f4e79}{\textbf{Example Queries in Practice}}$

| $\color{#228B22}{\textbf{Use Case}}$ | $\color{#228B22}{\textbf{Query Logic}}$ | $\color{#228B22}{\textbf{Records}}$ | $\color{#228B22}{\textbf{PMIDs}}$ | $\color{#228B22}{\textbf{Interpretation}}$ |
|---|---|---:|---:|---|
| $\color{#1f4e79}{\textbf{Protein cargo}}$ | `molecule\_type = Protein` | 207,623 | 569 | Broad, high-volume cargo retrieval |
| $\color{#1f4e79}{\textbf{miRNA cargo}}$ | `molecule\_type = miRNA` | 16,131 | 120 | Canonical miRNA retrieval |
| $\color{#1f4e79}{\textbf{Lipid cargo}}$ | `molecule\_type = Lipid` | 2,896 | 52 | Source-complementary coverage |
| $\color{#1f4e79}{\textbf{Plasma context}}$ | `sample\_name contains plasma` | 547 | 444 | Biofluid metadata retrievable, source-dependent |
| $\color{#1f4e79}{\textbf{Breast cancer}}$ | `disease contains breast cancer` | 312 | 187 | Disease context available but sparse |
| $\color{#1f4e79}{\textbf{Clinically constrained}}$ | `disease + biofluid + molecule\_type` | 89 | 61 | Multi-field constraint sharply reduces coverage, visible in UI as low-density results |

---

## $\color{#1f4e79}{\textbf{Data Model}}$

| $\color{#228B22}{\textbf{Field}}$ | $\color{#228B22}{\textbf{Description}}$ |
|---|---|
| $\color{#1f4e79}{\textbf{source}}$ | Origin repository (Vesiclepedia / ExoCarta / EV-TRACK) |
| $\color{#1f4e79}{\textbf{working\_id}}$ | Cargo-level identifier when available |
| $\color{#1f4e79}{\textbf{molecule\_type}}$ | Standardized molecular class (Protein, mRNA, miRNA, Lipid) |
| $\color{#1f4e79}{\textbf{molecule\_type\_raw}}$ | Original source-reported molecular label |
| $\color{#1f4e79}{\textbf{species}}$ | Standardized organism name via curated dictionary |
| $\color{#1f4e79}{\textbf{disease}}$ | Disease/clinical context annotation, or `Unknown` |
| $\color{#1f4e79}{\textbf{sample\_name}}$ | Biofluid or sample-type annotation, or `Unknown` |
| $\color{#1f4e79}{\textbf{method}}$ | Isolation/detection method as reported by source |
| $\color{#1f4e79}{\textbf{pmid}}$ | PubMed identifier linked directly to the record |
| $\color{#1f4e79}{\textbf{year}}$ | Publication year extracted from source metadata |
| $\color{#1f4e79}{\textbf{utility\_score}}$ | Record-level triage score (metadata completeness, query match quality, source priority, recency) |

> **Important:** `utility\_score` supports **triage** of query results. It is **not** a biological confidence or experimental validity score.

---

## $\color{#1f4e79}{\textbf{Repository Structure}}$

| $\color{#228B22}{\textbf{Path}}$ | $\color{#228B22}{\textbf{Description}}$ |
|---|---|
| $\color{#1f4e79}{\textbf{app.py}}$ | Flask application entry point and query routing |
| $\color{#1f4e79}{\textbf{data/unified\_EVmetadata.parquet}}$ | Harmonized snapshot in Apache Parquet format |
| $\color{#1f4e79}{\textbf{notebooks/}}$ | Integration, deduplication, and validation notebooks |
| $\color{#1f4e79}{\textbf{static/}}$ | Front-end assets (CSS, JS, summary plot rendering) |
| $\color{#1f4e79}{\textbf{templates/}}$ | HTML templates for the query interface |
| $\color{#1f4e79}{\textbf{Validation\_Audits/}}$ | CSV outputs for completeness, stability, and complementarity audits |
| $\color{#1f4e79}{\textbf{requirements.txt}}$ | Python dependency specification |
| $\color{#1f4e79}{\textbf{LICENSE}}$ | MIT license for the source code |

---

## $\color{#1f4e79}{\textbf{Interface}}$

The web interface supports both free-text and structured filter queries, and returns:
- Summary plots by source, molecular class, species, and publication year
- Direct PubMed links for each record
- Record-level utility scores to support result triage
- One-click CSV export of query results

The backend runs on a local Flask server, querying the Parquet snapshot through DuckDB for sub-second response times on standard hardware.

---

## $\color{#1f4e79}{\textbf{Validation \& Audit Summary}}$

A dedicated validation suite (`Validation\_Audits/`) evaluates:
- Method field completeness (16.87% missing/unusable)
- Query syntax sensitivity and time-stratified completeness
- miRNA presence and multi-cargo routing diagnostics
- Source complementarity across molecule types
- Record-to-PMID density and manual spot-check accuracy (72 rows, 5 categories)

All audit outputs are stored as CSV files for full reproducibility and external review.

---

## $\color{#1f4e79}{\textbf{Installation}}$

```bash
git clone https://github.com/<your-username>/EVisionary.git
cd EVisionary
pip install -r requirements.txt
python app.py
```

---

## $\color{#1f4e79}{\textbf{License}}$

This repository is distributed under the **MIT License**.

*Please note: the MIT License applies exclusively to the source code developed within this repository. The individual licensing terms of the original EV data sources must be reviewed and adhered to independently prior to redistribution of any raw or derived biological datasets.*

---

## $\color{#1f4e79}{\textbf{Contact \& Support}}$

$\color{#1f4e79}{\text{Contact \& Support}}$

For scientific inquiries, feature suggestions, or collaboration requests, please contact:

📧 **shayesteh222sowgand@gmail.com**
```

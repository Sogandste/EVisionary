# EVisionary

**A snapshot-based, provenance-aware framework for harmonizing and querying extracellular vesicle repositories**

[![Python](https://img.shields.io/badge/Python-3.10-blue.svg)](https://www.python.org/)
[![DuckDB](https://img.shields.io/badge/DuckDB-query%20engine-yellow.svg)](https://duckdb.org/)
[![Flask](https://img.shields.io/badge/Flask-web%20interface-lightgrey.svg)](https://flask.palletsprojects.com/)
[![Parquet](https://img.shields.io/badge/Apache%20Parquet-local%20snapshot-green.svg)](https://parquet.apache.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-orange.svg)](LICENSE)
[![Demo](https://img.shields.io/badge/Demo-Render-purple.svg)](https://evisionary.onrender.com/)

---

## Overview

**EVisionary** is a local, snapshot-based, provenance-aware framework for harmonizing and querying extracellular vesicle (EV) repository data.

Public EV resources such as **Vesiclepedia**, **ExoCarta**, and **EV-TRACK** provide valuable EV cargo and study-level metadata, but they differ in schema, terminology, granularity, reporting focus, and query behavior. In practice, researchers often need to search multiple repositories separately, manually reconcile inconsistent labels, and track whether evidence is source-specific or shared across repositories.

EVisionary addresses this problem by converting dated repository exports into a local, harmonized, and auditable query snapshot. It preserves repository provenance, raw annotations, and normalized fields while avoiding unsupported biological inference.

> EVisionary is **not** a live federated query system.  
> It uses locally obtained, dated repository snapshots to support reproducible and auditable EV data reuse.

A public demonstration is available at:

```text
https://evisionary.onrender.com/
```

---

## Why EVisionary?

EV repositories are complementary but incomplete in isolation.

- **Vesiclepedia** and **ExoCarta** primarily catalogue molecular cargo, including proteins, mRNAs, miRNAs, and lipids.
- **EV-TRACK** captures study-level reporting and contextual metadata.
- Cargo, disease, biofluid, species, and clinical context are not consistently co-annotated across repositories.
- Simple concatenation can fragment equivalent labels, inflate apparent evidence, or hide repository provenance.
- Over-aggressive harmonization can introduce unsupported biological equivalences.

EVisionary provides a conservative query and harmonization layer that:

- standardizes source-specific schemas into a canonical structure;
- preserves source attribution throughout processing;
- keeps raw and normalized annotations available for audit;
- exposes metadata sparsity instead of hiding it;
- supports reproducible local querying through Parquet and DuckDB;
- provides a lightweight Flask web interface for interactive exploration.

---

## Key Features

- **Snapshot-based integration**  
  Uses dated local exports rather than live remote querying.

- **Provenance-aware harmonization**  
  Retains source information throughout normalization, deduplication, and querying.

- **Conservative canonical schema**  
  Maps heterogeneous repository fields to a standardized schema while using `Unknown` for missing or semantically unsafe values.

- **Multi-cargo EV support**  
  Supports protein, mRNA, miRNA, lipid, and study-level metadata records.

- **Source-aware deduplication**  
  Uses a provenance-preserving deduplication strategy to avoid collapsing records from different repositories into unsupported biological assertions.

- **Local query backend**  
  Uses Apache Parquet and DuckDB for fast local querying.

- **Flask web interface**  
  Provides interactive search, filters, summary plots, PubMed links, utility scores, and CSV export.

- **Validation and audit outputs**  
  Includes field-completeness checks, syntax-sensitivity analyses, source-complementarity audits, clinically constrained query tests, benchmarking, and manual spot-checks.

---

## Current Snapshot Summary

The current EVisionary snapshot integrates EV-related records from Vesiclepedia, ExoCarta, and EV-TRACK.

| Metric | Value |
|---|---:|
| Source rows processed | 713,667 |
| Final harmonized records | 258,460 |
| Cargo-level records | 253,491 |
| Study-level EV-TRACK records | 4,969 |
| Vesiclepedia records | 195,488 |
| ExoCarta records | 58,003 |
| EV-TRACK records | 4,969 |
| Missing or unusable method field | 16.87% |

---

## Molecular Cargo Composition

| Molecular class | Records | Unique PMIDs |
|---|---:|---:|
| Protein | 207,623 | 569 |
| mRNA | 26,701 | 26 |
| miRNA | 16,131 | 120 |
| Lipid | 2,896 | 52 |

Disease annotations were available in **4,949 records**, corresponding to **1.92%** of the harmonized snapshot. This highlights persistent sparsity of disease and clinical-context metadata even after cross-repository integration.

---

## Repository Complementarity

EVisionary shows that EV repositories are complementary rather than interchangeable.

| Molecular class | Vesiclepedia | ExoCarta | Main pattern |
|---|---:|---:|---|
| Protein | 160,806 | 46,817 | Vesiclepedia-enriched |
| mRNA | 23,307 | 3,394 | Vesiclepedia-enriched |
| miRNA | 10,091 | 6,040 | Vesiclepedia + ExoCarta |
| Lipid | 1,283 | 1,613 | ExoCarta-enriched |

Contextual metadata such as plasma and breast-cancer annotations are largely source-dependent in the current snapshot. EVisionary makes these dependencies visible so that users can distinguish true query failure from metadata sparsity or granularity mismatch.

---

## Example Use Cases

| Use case | Query / filter | Records | Unique PMIDs | Interpretation |
|---|---|---:|---:|---|
| Protein cargo search | `molecule_type = Protein` | 207,623 | 569 | Broad cargo retrieval with retained provenance |
| miRNA cargo search | `molecule_type = miRNA` | 16,131 | 120 | Stable canonical miRNA retrieval |
| Lipid cargo search | `molecule_type = Lipid` | 2,896 | 52 | Lipid evidence is source-complementary |
| Plasma context search | `sample_name contains plasma` | 547 | 444 | Biofluid metadata are retrievable but source-dependent |
| Breast cancer context search | `disease contains breast cancer` | 12 | 11 | Disease metadata are sparse and repository-dependent |
| Breast cancer + plasma | `breast cancer AND plasma` | 6 | 6 | Disease and biofluid co-annotation exists but remains sparse |
| Breast cancer + plasma + miRNA | `breast cancer AND plasma AND miRNA` | 0 | 0 | Metadata granularity gap, not backend failure |

The zero-result clinically constrained query does **not** imply absence of biological evidence. It indicates that the current repository snapshots do not connect cargo, disease, and biofluid annotations at compatible granularity.

---

## Architecture

```text
Repository exports
       |
       |  Vesiclepedia
       |  ExoCarta
       |  EV-TRACK
       v
Source-specific ingestion
       |
       v
Canonical field mapping
       |
       v
Conservative normalization
       |
       v
Provenance-preserving deduplication
       |
       v
Apache Parquet master snapshot
       |
       v
DuckDB query backend
       |
       v
Flask web interface
       |
       v
Source-aware tables, summary plots,
PubMed links, utility scores, CSV export
```

---

## Repository Structure

The repository is organized around the web interface, harmonization scripts, source/processed data, and documentation.

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

Main components:

| Path | Purpose |
|---|---|
| `app.py` | Root-level Flask application entry point retained for deployment compatibility |
| `Scripts/app.py` | Script-level Flask application entry point / working application script |
| `evisionary_common.py` | Shared EVisionary helper functions |
| `ontology_terms.py` | Ontology or controlled vocabulary terms used by the interface/pipeline |
| `synonyms.py` | Synonym and query-normalization resources |
| `requirements.txt` | Python dependencies |
| `data/` | Data files, processed outputs, or audit tables |
| `docs/` | Documentation, figures, and supporting materials |
| `static/` | Static web assets |
| `templates/` | Flask HTML templates |

---

## Data Model

EVisionary maps heterogeneous repository exports to a conservative canonical schema.

Core fields include:

| Field | Description |
|---|---|
| `pmid` | Publication identifier |
| `sample_name` | Sample or biosource descriptor |
| `working_id` | Cargo-level identifier when available |
| `molecule_type_raw` | Original source-reported cargo label |
| `molecule_type_norm` | Cleaned canonical cargo label |
| `molecule_type_group` | Broad molecular grouping |
| `method` | Isolation or methodological descriptor |
| `species` | Harmonized organism label |
| `year` | Publication year |
| `disease` | Disease or condition annotation |
| `vesicle` | Vesicle subtype or EV-related annotation |
| `ev_metric` | EV-TRACK-associated reporting metric |
| `source` | Repository provenance |

Missing or semantically unsafe values are represented as `Unknown` rather than inferred.

---

## Conservative Harmonization Policy

EVisionary performs:

- schema-level harmonization;
- lexical normalization;
- species-label standardization using curated mappings;
- source-aware deduplication;
- syntax-stabilized querying;
- audit-friendly reporting.

EVisionary does **not** perform:

- live federated querying;
- ontology-based synonym expansion by default;
- unsupported biological entity collapse across repositories;
- unsupported inference from study-level metadata to cargo-level records;
- experimental validation;
- biological confidence scoring.

This conservative design helps prevent false equivalences and keeps the integrated resource auditable.

---

## Utility Score

EVisionary includes a record-level utility score to help users prioritize records during exploratory searches.

The utility score reflects:

- metadata completeness;
- query-match quality;
- source-prioritization rules;
- publication year.

The utility score is intended for **exploratory triage only**.

It should **not** be interpreted as:

- biological importance;
- experimental validity;
- evidence strength;
- confidence in the underlying biological claim.

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Sogandste/EVisionary.git
cd EVisionary
```

### 2. Create a Python environment

EVisionary was developed for Python 3.10.

```bash
python3.10 -m venv .venv
source .venv/bin/activate
```

On Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Web Interface Locally

The working application entry point is:

```bash
python Scripts/app.py
```

Then open:

```text
http://127.0.0.1:5000
```

Depending on deployment configuration, the root-level `app.py` may also be used for Render compatibility.

```bash
python app.py
```

---

## Render Deployment

The public demonstration is deployed on Render:

```text
https://evisionary.onrender.com/
```

If using a `Procfile`, the expected command is:

```text
web: gunicorn Scripts.app:app
```

If Render is configured to use the root-level application instead, use:

```text
web: gunicorn app:app
```

Do not move `static/`, `templates/`, or root-level deployment files unless the Flask paths and Render start command are updated accordingly.

---

## Input Data

EVisionary expects local exports from:

- Vesiclepedia
- ExoCarta
- EV-TRACK

Raw source data should be obtained from the original repositories according to their own licensing and redistribution terms.

Recommended local organization:

```text
data/raw/Vesiclepedia/
data/raw/ExoCarta/
data/raw/EV-TRACK/
data/processed/
data/audit/
```

Large raw or processed data files may be excluded from GitHub and distributed separately depending on licensing and file-size constraints.

---

## Example Queries

The interface supports free-text and filter-based exploration. Example queries include:

```text
Protein
miRNA
plasma
breast cancer
breast cancer AND plasma
breast cancer AND plasma AND miRNA
```

A zero result for a clinically constrained query should be interpreted carefully. It may reflect missing co-annotation or incompatible granularity across repositories rather than true biological absence.

---

## Programmatic Querying with DuckDB

Example query against a local Parquet snapshot:

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

Example contextual query:

```python
query = f"""
SELECT source, disease, sample_name, pmid, year
FROM read_parquet('{parquet_path}')
WHERE regexp_matches(lower(disease), 'breast[-\\s]+cancer')
  AND regexp_matches(lower(sample_name), '\\bplasma\\b')
"""

results = con.execute(query).df()
print(results)
```

---

## Validation Summary

The current validation and audit workflow supports:

- field-completeness auditing;
- method-field missingness audit;
- syntax-sensitivity analysis;
- gain-provenance analysis;
- miRNA presence and routing diagnostic;
- source-complementarity analysis;
- record-to-PMID density analysis;
- ablation analysis;
- error taxonomy;
- manual spot-check samples;
- clinically constrained query audit;
- local query benchmarking.

Key validation results:

- `713,667` source rows were processed.
- `258,460` records were retained in the harmonized snapshot.
- `16,131` canonical miRNA records were recovered through multi-cargo integration.
- `16.87%` of records had missing or unusable method information.
- Plasma retrieval increased from 2 exact matches to 547 stabilized matches.
- Breast cancer retrieval increased from 8 exact matches to 12 stabilized matches.
- Breast cancer + plasma + miRNA returned zero records despite individual-term retrievability, indicating a metadata co-annotation/granularity gap rather than backend failure.

---

## Reproducibility

EVisionary supports reproducible EV data reuse through:

- dated source snapshots;
- explicit source-to-canonical mappings;
- conservative missing-value handling;
- provenance-preserving deduplication;
- local Parquet snapshot storage;
- DuckDB-based querying;
- validation and audit outputs.

Because source repositories evolve over time, row counts may change when newer exports are used. For reproducibility, users should report:

- source repository names;
- snapshot dates;
- raw row counts;
- invalid-record filtering criteria;
- deduplication key;
- final harmonized row count;
- software version or commit hash.

---

## Limitations

EVisionary is a conservative query and harmonization layer, not a replacement for primary EV repositories.

Important limitations:

- The framework depends on the completeness and structure of source repository exports.
- Disease, biofluid, and clinical-context annotations remain sparse.
- EV-TRACK contributes study-level metadata rather than molecule-level cargo records.
- EVisionary does not perform ontology-based semantic expansion by default.
- Zero-result queries may reflect metadata granularity gaps rather than biological absence.
- Utility scores support exploratory triage, not biological confidence.
- New repository snapshots may change counts and source distributions.

---

## When Should I Use EVisionary?

EVisionary is useful for:

- rapid EV cargo lookup;
- pre-experimental candidate checks;
- source-aware evidence review;
- exploratory EV biomarker queries;
- identifying repository-specific metadata gaps;
- preparing systematic EV data reuse workflows;
- comparing cargo and contextual metadata availability across EV repositories.

EVisionary is less suitable for:

- definitive biological absence claims;
- live repository federation;
- automatic ontology-based entity resolution;
- replacing expert curation for clinical-grade interpretation.

---

## Citation

A manuscript describing EVisionary is currently in preparation. Citation details will be added upon publication.

Until then, if you use this repository, please cite the GitHub project:

```text
Sogand. EVisionary: a snapshot-based, provenance-aware framework for harmonizing and querying extracellular vesicle repositories. GitHub repository, 2026.
```

Repository:

```text
https://github.com/Sogandste/EVisionary
```

---

## Related Resources

- Vesiclepedia: https://www.microvesicles.org/
- ExoCarta: http://www.exocarta.org/
- EV-TRACK: https://evtrack.org/
- DuckDB: https://duckdb.org/
- Apache Parquet: https://parquet.apache.org/
- Flask: https://flask.palletsprojects.com/

---

## Data Availability

Raw source data should be obtained from the original repositories according to their respective licensing and redistribution terms.

Derived harmonized outputs, validation audits, and example query results will be made available according to data-source licensing constraints and manuscript release status.

---

## License

This project is released under the MIT License. See the `LICENSE` file for details.

Please check the licensing and redistribution terms of the original data sources before redistributing raw or derived datasets.

---

## Contact

For questions, suggestions, or collaboration requests:

```text
shayesteh222sowgand@gmail.com
```

Or open an issue:

```text
https://github.com/Sogandste/EVisionary/issues
```

---

## Short Project Summary

EVisionary is a local, snapshot-based, provenance-aware framework for harmonizing extracellular vesicle repository exports into an auditable Parquet-based resource. It enables source-aware querying of molecular cargo and contextual metadata while making repository complementarity and metadata sparsity explicit.

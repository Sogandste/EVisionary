<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=rect&height=150&color=0:1f4e79,55:228B22,100:DAA520&text=EVisionary&fontColor=ffffff&fontSize=44&fontAlignY=42&desc=Provenance-aware%20exploration%20of%20extracellular%20vesicle%20repositories&descAlignY=70&descSize=16" width="100%" alt="EVisionary">
</p>

<p align="center">
  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/Python-3.10-228B22?labelColor=1f4e79" alt="Python 3.10">
  </a>
  <a href="https://duckdb.org/">
    <img src="https://img.shields.io/badge/DuckDB-query%20engine-DAA520?labelColor=1f4e79" alt="DuckDB">
  </a>
  <a href="https://parquet.apache.org/">
    <img src="https://img.shields.io/badge/Apache%20Parquet-snapshot-228B22?labelColor=1f4e79" alt="Apache Parquet">
  </a>
  <a href="https://flask.palletsprojects.com/">
    <img src="https://img.shields.io/badge/Flask-web%20interface-DAA520?labelColor=1f4e79" alt="Flask">
  </a>
  <a href="LICENSE">
    <img src="https://img.shields.io/badge/License-MIT-228B22?labelColor=1f4e79" alt="MIT License">
  </a>
</p>

<p align="center">
  <strong>
    A local, snapshot-based framework for harmonizing and querying extracellular vesicle repository data while retaining source provenance
  </strong>
</p>

<p align="center">
  <a href="https://evisionary.onrender.com/"><strong>Live application</strong></a>
  &nbsp;·&nbsp;
  <a href="#quick-start"><strong>Quick start</strong></a>
  &nbsp;·&nbsp;
  <a href="#validated-reference-snapshot"><strong>Reference snapshot</strong></a>
  &nbsp;·&nbsp;
  <a href="https://github.com/Sogandste/EVisionary/issues"><strong>Report an issue</strong></a>
</p>

---

## Overview

EVisionary is a local, snapshot-based framework for harmonizing and querying extracellular vesicle (EV) repository data. It brings together dated exports from **Vesiclepedia**, **ExoCarta**, and **EV-TRACK** in a unified resource designed for reproducible, source-aware exploration.

Public EV repositories provide complementary information but differ in schema design, terminology, annotation depth, and evidence granularity. Vesiclepedia and ExoCarta primarily contribute cargo-level records, whereas EV-TRACK provides study-level reporting metadata. These differences make cross-repository searches difficult to reproduce and audit.

EVisionary addresses this problem conservatively. It standardizes selected fields needed for retrieval while retaining repository identity, source-reported annotations, and record-level provenance. Missing or unresolved values remain explicit and are not replaced by unsupported biological inference.

> [!IMPORTANT]
> EVisionary is not a live federated search engine. It queries dated local snapshots so that retrieval behavior remains stable, reproducible, and auditable.

<p align="center">
  <a href="https://evisionary.onrender.com/">
    <img src="https://img.shields.io/badge/OPEN%20LIVE%20APPLICATION-EVisionary-228B22?style=for-the-badge&labelColor=1f4e79" alt="Open EVisionary">
  </a>
</p>

---

## Why EVisionary?

No single public EV repository captures molecular cargo, species, disease, biofluid, experimental method, vesicle annotation, publication linkage, and reporting information at equal depth.

Simple concatenation of repository exports can retain duplicate content, fragment related labels, and obscure the origin of individual records. At the same time, aggressive normalization can collapse distinct annotations into unsupported biological equivalences.

EVisionary follows a conservative middle path:

- improves cross-repository searchability;
- preserves the identity of the contributing source;
- retains raw and normalized annotation layers;
- applies source-aware deduplication rules;
- represents unresolved values explicitly;
- exposes metadata gaps rather than concealing them;
- avoids unsupported biological or clinical inference.

The framework is intended to help researchers identify what is represented in the selected snapshots, where that information originates, and which metadata limitations should be considered before export or interpretation.

---

## Key capabilities

- **Snapshot-based integration**  
  Processes dated local exports rather than relying on live API availability.

- **Provenance retention**  
  Preserves repository identity and source-oriented record identifiers throughout processing.

- **Conservative harmonization**  
  Standardizes selected fields without inferring missing biological relationships.

- **Provenance-aware deduplication**  
  Removes duplicated content under defined source-aware rules.

- **Multi-cargo retrieval**  
  Supports protein, mRNA, miRNA, lipid, and study-level EV-TRACK records.

- **Local analytical querying**  
  Uses Apache Parquet and DuckDB for fast and reproducible retrieval.

- **Interactive exploration**  
  Provides free-text search, structured filters, summary plots, PubMed links, record inspection, and CSV export.

- **Transparent result triage**  
  Displays metadata utility independently from query-match scoring.

- **Audit-oriented validation**  
  Supports completeness checks, source-complementarity analysis, constrained-query evaluation, and manual inspection.

---

## Quick start

### Requirements

- Python 3.10
- Git
- A compatible local data snapshot when the processed dataset is not distributed with the repository

### 1. Clone the repository

```bash
git clone https://github.com/Sogandste/EVisionary.git
cd EVisionary
```

### 2. Create a virtual environment

#### macOS or Linux

```bash
python3.10 -m venv .venv
source .venv/bin/activate
```

#### Windows PowerShell

```powershell
py -3.10 -m venv .venv
.venv\Scripts\Activate.ps1
```

### 3. Install the dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Run EVisionary locally

```bash
python Scripts/app.py
```

Open the interface at:

```text
http://127.0.0.1:5000
```

> [!NOTE]
> `Scripts/app.py` is the documented local entry point. The root-level `app.py` is retained for deployment compatibility.

---

## Using the interface

The public demonstration is available at:

**[https://evisionary.onrender.com/](https://evisionary.onrender.com/)**

A typical retrieval workflow consists of the following steps:

1. Enter a molecular identifier or a contextual search term.
2. Apply source, species, or molecular-group filters when needed.
3. inspect the returned-set summaries.
4. Open individual records to review provenance and available metadata.
5. Follow PubMed links for publication-level verification.
6. Export the current result set as CSV for downstream review.

The interface supports exploratory searches involving:

- molecular identifiers;
- molecular classes;
- diseases or conditions;
- species;
- sample and biofluid annotations;
- methodological descriptors;
- vesicle annotations;
- source repositories;
- PubMed identifiers.

Summary plots allow users to assess whether a retrieved set is dominated by a particular repository, species, molecular class, or metadata-utility band before exporting the records.

---

## Metadata utility and query matching

EVisionary presents two separate record-level indicators.

### Metadata Utility Score

The **Metadata Utility Score** is a query-independent indicator of available record-level metadata. It supports triage by helping users distinguish records with comparatively more inspectable context from records containing limited annotations.

### Query-match Score

The **Query-match Score** is query-dependent and reflects lexical agreement between the current search expression and searchable record fields. It supports ordering within the active retrieved set.

These values are displayed separately because metadata completeness and query relevance are not equivalent.

> [!CAUTION]
> Neither score measures biological confidence, evidence strength, experimental validity, study quality, biomarker relevance, or clinical significance. They are provided only to support transparent exploratory retrieval and record triage.

---

## Processing workflow

```text
Dated repository exports
Vesiclepedia · ExoCarta · EV-TRACK
                  │
                  ▼
Source-specific ingestion
                  │
                  ▼
Canonical field mapping
                  │
                  ▼
Conservative normalization
                  │
                  ▼
Provenance-aware deduplication
                  │
                  ▼
Query-ready Parquet snapshot
                  │
                  ▼
DuckDB analytical query layer
                  │
                  ▼
Flask exploration interface
                  │
                  ▼
Auditable and exportable results
```

The workflow retains source identity and raw annotations wherever possible. Normalized fields are added to support retrieval, while unresolved biological or clinical context remains explicit.

---

## Repository structure

```text
EVisionary/
├── app.py
├── evisionary_common.py
├── ontology_terms.py
├── synonyms.py
├── requirements.txt
├── runtime.txt
├── Procfile
├── LICENSE
├── README.md
│
├── Scripts/
├── data/
├── docs/
├── static/
└── templates/
```

### Main files and directories

- `app.py` — root-level Flask entry point used for deployment.
- `Scripts/` — local application and processing scripts.
- `evisionary_common.py` — shared query, formatting, and processing utilities.
- `ontology_terms.py` — controlled terminology used during annotation handling.
- `synonyms.py` — conservative synonym and query-normalization resources.
- `templates/` — Flask HTML templates.
- `static/` — stylesheets, JavaScript, and interface assets.
- `data/` — permitted local inputs, processed snapshots, and audit outputs.
- `docs/` — extended technical and validation documentation.
- `requirements.txt` — Python dependencies.
- `runtime.txt` — deployment runtime configuration.
- `Procfile` — hosting process declaration.
- `LICENSE` — MIT License for original EVisionary code.

> [!WARNING]
> Do not move `app.py`, `Procfile`, `requirements.txt`, `runtime.txt`, `templates/`, or `static/` unless the corresponding Flask and deployment paths are updated.

---

## Canonical data representation

EVisionary maps heterogeneous source records into a conservative canonical representation.

### Provenance fields

- `record_uid` — identifier of the retained harmonized record.
- `source_row_uid` — identifier linked to the original source row.
- `pre_dedup_uid` — identifier retained before deduplication.
- `source` — contributing repository.
- `source_priority` — deterministic processing value, not a measure of scientific quality.

### Molecular fields

- `working_id` — cargo-level identifier when available.
- `molecule_type_raw` — source-reported molecular label.
- `molecule_type_norm` — conservatively normalized label.
- `molecule_type_group` — broader molecular grouping.
- `molecule_type` — compatibility field exposed in retrieval outputs.

### Context fields

- `species`
- `sample_name`
- `disease`
- `method`
- `vesicle`
- `characterization`
- `pmid`
- `year`
- `ev_metric`

Missing, blank, or unresolved values are represented explicitly as `Unknown`. EVisionary does not infer absent species, disease, biofluid, method, or clinical context from neighboring records.

Differences between raw, normalized, and compatibility fields are retained as inspection points. A detected difference does not automatically indicate a biological or processing error.

---

## Validated reference snapshot

The following values describe the validated reference snapshot used during framework evaluation. They are not live totals from the original repositories.

| Metric | Value |
|---|---:|
| Source rows processed | 713,667 |
| Final harmonized records | 258,460 |
| Cargo-level records | 253,491 |
| Study-level EV-TRACK records | 4,969 |
| Vesiclepedia records | 195,488 |
| ExoCarta records | 58,003 |
| Missing or unusable method annotations | 16.87% |

The difference between source rows and final records reflects processing, schema alignment, and provenance-aware deduplication. It should not be interpreted as a measure of repository quality.

### Molecular cargo coverage

| Molecular class | Records | Unique PMIDs |
|---|---:|---:|
| Protein | 207,623 | 569 |
| mRNA | 26,701 | 26 |
| miRNA | 16,131 | 120 |
| Lipid | 2,896 | 52 |

Disease annotations were available for **4,949 records**, corresponding to **1.92%** of the harmonized reference snapshot. This sparsity limits highly constrained disease-, biofluid-, and cargo-level retrieval.

### Source complementarity

| Molecular class | Vesiclepedia | ExoCarta |
|---|---:|---:|
| Protein | 160,806 | 46,817 |
| mRNA | 23,307 | 3,394 |
| miRNA | 10,091 | 6,040 |
| Lipid | 1,283 | 1,613 |

The observed distributions show that Vesiclepedia and ExoCarta provide complementary rather than interchangeable coverage. EV-TRACK remains represented at the study level and should not be treated as directly equivalent to cargo-level records.

---

## Example retrieval scenarios

| Scenario | Retrieval condition | Records | PMIDs |
|---|---|---:|---:|
| Protein cargo | `molecule_type = Protein` | 207,623 | 569 |
| miRNA cargo | `molecule_type = miRNA` | 16,131 | 120 |
| Lipid cargo | `molecule_type = Lipid` | 2,896 | 52 |
| Plasma context | `sample_name contains plasma` | 547 | 444 |
| Breast cancer | `disease contains breast cancer` | 12 | 11 |
| Breast cancer and plasma | Combined context | 6 | 6 |
| Breast cancer, plasma, and miRNA | Combined context and cargo | 0 | 0 |

A zero-result constrained query does not establish biological absence. It indicates only that the selected snapshots do not connect the requested annotations at a compatible record level under the applied query rules.

---

## Programmatic querying

The generated Parquet snapshot can be queried directly with DuckDB.

### Retrieve miRNA records

```python
import duckdb

parquet_path = "data/processed/unified_EVmetadata_keyB.parquet"

query = """
SELECT
    source,
    working_id,
    molecule_type_norm,
    species,
    disease,
    sample_name,
    pmid,
    year
FROM read_parquet(?)
WHERE lower(molecule_type_norm) = 'mirna'
LIMIT 20
"""

with duckdb.connect() as connection:
    results = connection.execute(query, [parquet_path]).df()

print(results)
```

### Retrieve breast-cancer records with plasma context

```python
import duckdb

parquet_path = "data/processed/unified_EVmetadata_keyB.parquet"

query = r"""
SELECT
    source,
    working_id,
    molecule_type_norm,
    disease,
    sample_name,
    pmid,
    year
FROM read_parquet(?)
WHERE regexp_matches(
        lower(coalesce(disease, '')),
        'breast[-\s]+cancer'
      )
  AND regexp_matches(
        lower(coalesce(sample_name, '')),
        '\bplasma\b'
      )
"""

with duckdb.connect() as connection:
    results = connection.execute(query, [parquet_path]).df()

print(results)
```

Update `parquet_path` if the processed snapshot is stored in a different local directory.

---

## Validation

The validated reference snapshot was evaluated using an audit suite that included:

- field-completeness analysis;
- method-field missingness assessment;
- query-syntax sensitivity testing;
- time-stratified completeness checks;
- miRNA presence and routing diagnostics;
- source-complementarity analysis;
- record-to-PMID density assessment;
- ablation analysis;
- error taxonomy development;
- manual spot-check sampling;
- clinically constrained query auditing;
- local query-performance benchmarking.

Manual spot checks included representative records associated with plasma, breast cancer, protein, miRNA, and lipid retrieval. A total of **72 spot-check rows** were inspected across these scenarios.

The recovery of **16,131 canonical miRNA records** confirmed miRNA presence through multi-cargo integration. The zero-result breast cancer, plasma, and miRNA query was attributable to the absence of compatible cross-field co-annotation in the evaluated snapshot rather than the general absence of miRNA records.

---

## Reproducibility

Analyses based on EVisionary should report:

- repositories included;
- acquisition or snapshot dates;
- source filenames or release identifiers;
- initial source-row counts;
- preprocessing and exclusion rules;
- canonical mapping version;
- normalization rules;
- provenance and deduplication keys;
- final harmonized record count;
- exact query expressions and filters;
- result limits, where applied;
- software release or Git commit hash;
- relevant validation outputs.

Record counts and query results can change when source exports, terminology maps, processing rules, or software versions are updated.

Record the current software commit with:

```bash
git rev-parse HEAD
```

---

## Deployment

The public EVisionary instance is hosted on Render:

**[https://evisionary.onrender.com/](https://evisionary.onrender.com/)**

The root-level Flask application is used as the deployment entry point. A typical `Procfile` declaration is:

```text
web: gunicorn app:app
```

The following deployment-sensitive components should remain in their expected locations:

```text
app.py
Procfile
requirements.txt
runtime.txt
templates/
static/
```

Render instances on resource-limited plans may require a short cold-start period before the first request is completed.

---

## Data availability

Raw data from Vesiclepedia, ExoCarta, and EV-TRACK must be obtained from their original repositories and handled according to their respective access, citation, licensing, and redistribution requirements.

A recommended local organization is:

```text
data/
├── raw/
│   ├── Vesiclepedia/
│   ├── ExoCarta/
│   └── EV-TRACK/
├── processed/
└── audit/
```

- `raw/` contains unchanged source exports.
- `processed/` contains generated harmonized snapshots.
- `audit/` contains validation and diagnostic outputs.

Derived snapshots may be shared only where permitted by source-data conditions. The absence of raw or processed data from this repository may reflect licensing, redistribution, file-size, or release-stage restrictions.

---

## Limitations

EVisionary is a harmonization and retrieval layer, not a replacement for primary repositories or publication-level evidence assessment.

Current limitations include:

- dependence on the completeness and consistency of source metadata;
- substantial sparsity in disease, biofluid, and clinical annotations;
- unequal annotation depth across repositories and molecular classes;
- source-dependent terminology and metadata granularity;
- study-level rather than cargo-level representation of EV-TRACK records;
- no default broad ontology expansion, to reduce over-harmonization;
- possible result changes when newer snapshots or mapping rules are used;
- retrieval indicators intended for triage rather than biological validation;
- practical output limits in the public demonstration interface.

Integration broadens searchable coverage but cannot recover information that was never reported or retained by the original sources.

---

## Responsible use

### Appropriate uses

EVisionary is intended for:

- exploratory lookup of EV-associated cargo records;
- source-aware inspection of repository evidence;
- preliminary candidate review;
- repository-informed hypothesis generation;
- identification of source-specific coverage;
- evaluation of metadata completeness and gaps;
- reproducible retrieval from dated snapshots;
- export of candidate records for expert review.

### Inappropriate uses

EVisionary should not be used for:

- claims of biological absence based on zero-result queries;
- direct clinical interpretation or decision support;
- treatment of metadata utility as biological confidence;
- treatment of query matching as evidence strength;
- automatic acceptance of harmonized annotations;
- unsupported ontology-level entity resolution;
- replacement of primary publications or repository records;
- claims of real-time repository coverage.

> [!IMPORTANT]
> All biologically or clinically important records should be verified against the original repository entries and linked publications before interpretation.

---

## Related resources

### EV repositories

- [Vesiclepedia](https://www.microvesicles.org/)
- [ExoCarta](http://www.exocarta.org/)
- [EV-TRACK](https://evtrack.org/)

### Technical components

- [Python](https://www.python.org/)
- [DuckDB](https://duckdb.org/)
- [Apache Parquet](https://parquet.apache.org/)
- [Flask](https://flask.palletsprojects.com/)
- [Render](https://render.com/)

EVisionary is an independent harmonization project. Inclusion of a repository or technology does not imply formal endorsement by its maintainers.

---

## Citation

An application note describing EVisionary is in preparation. Until a formal publication becomes available, please cite the repository as:

```text
Sogand. EVisionary: a provenance-aware framework for harmonizing and querying extracellular vesicle repositories. GitHub repository, 2026.
https://github.com/Sogandste/EVisionary
```

For reproducible use, include the release identifier or Git commit hash.

**Repository:** [https://github.com/Sogandste/EVisionary](https://github.com/Sogandste/EVisionary)

---

## License

Original EVisionary source code is released under the [MIT License](LICENSE).

The MIT License applies to code and other original materials developed for this repository. It does not supersede the access, citation, licensing, or redistribution conditions of Vesiclepedia, ExoCarta, EV-TRACK, linked publications, or other third-party data resources.

Users are responsible for reviewing the applicable source-data terms before redistributing raw or derived biological data.

---

## Contact and support

For scientific questions, feature suggestions, or collaboration requests:

**Email:** [shayesteh222sowgand@gmail.com](mailto:shayesteh222sowgand@gmail.com)

For technical issues:

- [GitHub issue tracker](https://github.com/Sogandste/EVisionary/issues)
- [EVisionary repository](https://github.com/Sogandste/EVisionary)

When reporting an issue, include the operating system, Python version, executed command, complete error message, and Git commit hash whenever possible.

---

<p align="center">
  <strong>Explore extracellular vesicle metadata without hiding its provenance or its gaps.</strong>
</p>

<p align="center">
  <a href="https://evisionary.onrender.com/">Live application</a>
  &nbsp;·&nbsp;
  <a href="https://github.com/Sogandste/EVisionary">Source code</a>
  &nbsp;·&nbsp;
  <a href="https://github.com/Sogandste/EVisionary/issues">Issue tracker</a>
</p>

<p align="center">
  <sub>
    EVisionary supports source-aware metadata exploration and does not provide biological validation or clinical interpretation.
  </sub>
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=rect&height=32&color=0:1f4e79,55:228B22,100:DAA520&section=footer" width="100%" alt="EVisionary footer">
</p>

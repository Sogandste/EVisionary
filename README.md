
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

<p align="center">
  <b>A snapshot-based, provenance-aware framework for harmonizing and querying extracellular vesicle repositories</b>
</p>

---

<p align="center">
  <img src="https://placehold.co/1200x48/1f4e79/ffffff.svg?text=Overview" alt="Overview" width="100%">
</p>

EVisionary is a local, snapshot-based framework developed to harmonize and query extracellular vesicle (EV) repository data while preserving the original source provenance. By integrating dated exports from **Vesiclepedia**, **ExoCarta**, and **EV-TRACK**, it creates a unified, locally queryable resource designed specifically for reproducible EV data reuse.

In standard EV bioinformatics workflows, researchers often face a practical limitation: existing repositories contain complementary but structurally heterogeneous information. For instance, Vesiclepedia and ExoCarta primarily report molecular cargo, whereas EV-TRACK captures study-level reporting metadata. Differences in schemas, terminologies, annotation depths, and query behaviors make cross-repository searches difficult to reproduce and interpret.

To address this, EVisionary harmonizes these disparate sources conservatively. It standardizes selected key fields, retains all raw annotations, preserves repository identity, and avoids unsupported biological inference. Missing or ambiguous values are represented explicitly as `Unknown`.

> **Note:** EVisionary is **not** a live federated query engine. It operates on dated local snapshots to prioritize reproducibility, auditability, and stable query behavior over time.

**Live Demo:** [https://evisionary.onrender.com/](https://evisionary.onrender.com/)

---

<p align="center">
  <img src="https://placehold.co/1200x48/1f4e79/ffffff.svg?text=Motivation" alt="Motivation" width="100%">
</p>

EV repositories are individually valuable, but they are often incomplete when used in isolation. Important details such as cargo-level evidence, disease context, biofluid annotations, species information, and methodological metadata are not consistently captured across sources or at the same level of granularity.

A naive integration approach typically introduces two issues:

1. **Simple concatenation** may duplicate existing evidence, fragment equivalent labels, or obscure the original source of a record.
2. **Over-harmonization** may collapse labels into unsupported biological equivalences, leading to inaccurate assumptions.

EVisionary takes a conservative middle path: it improves cross-repository search capability while keeping provenance, uncertainty, and metadata sparsity visible to the researcher.

---

<p align="center">
  <img src="https://placehold.co/1200x48/1f4e79/ffffff.svg?text=Key%20Features" alt="Key Features" width="100%">
</p>

| **Feature** | **Description** |
|---|---|
| **Snapshot-based integration** | Uses dated local exports rather than live and unstable repository API calls |
| **Provenance preservation** | Retains strict source identity throughout normalization and deduplication |
| **Conservative harmonization** | Normalizes selected fields without unsupported semantic inference |
| **Multi-cargo support** | Includes protein, mRNA, miRNA, lipid, and study-level EV-TRACK records |
| **Local query backend** | Uses Apache Parquet and DuckDB for efficient local querying |
| **Web interface** | Supports search, filtering, summary plots, PubMed links, utility scores, and CSV export |
| **Audit support** | Provides validation outputs for completeness, query stability, and source complementarity |

---

<p align="center">
  <img src="https://placehold.co/1200x48/1f4e79/ffffff.svg?text=Current%20Snapshot%20Statistics" alt="Current Snapshot Statistics" width="100%">
</p>

| **Metric** | **Value** |
|---|---:|
| Source rows processed | 713,667 |
| Final harmonized records | 258,460 |
| Cargo-level records | 253,491 |
| Study-level EV-TRACK records | 4,969 |
| Vesiclepedia records | 195,488 |
| ExoCarta records | 58,003 |
| Missing or unusable method | 16.87% |

---

<p align="center">
  <img src="https://placehold.co/1200x48/1f4e79/ffffff.svg?text=Molecular%20Cargo%20Composition" alt="Molecular Cargo Composition" width="100%">
</p>

| **Molecular Class** | **Total Records** | **Unique PMIDs** |
|---|---:|---:|
| Protein | 207,623 | 569 |
| mRNA | 26,701 | 26 |
| miRNA | 16,131 | 120 |
| Lipid | 2,896 | 52 |

*Disease annotations were available in only 4,949 records, corresponding to 1.92% of the harmonized snapshot. This highlights persistent sparsity of disease and clinical-context metadata even after cross-repository integration.*

---

<p align="center">
  <img src="https://placehold.co/1200x48/1f4e79/ffffff.svg?text=Source%20Complementarity" alt="Source Complementarity" width="100%">
</p>

| **Molecular Class** | **Vesiclepedia** | **ExoCarta** | **Main Pattern** |
|---|---:|---:|---|
| Protein | 160,806 | 46,817 | Vesiclepedia-dominant |
| mRNA | 23,307 | 3,394 | Vesiclepedia-dominant |
| miRNA | 10,091 | 6,040 | Shared coverage |
| Lipid | 1,283 | 1,613 | ExoCarta-dominant |

The integrated snapshot shows that EV repositories are complementary rather than interchangeable. Biofluid and disease annotations remain sparse and source-dependent.

---

<p align="center">
  <img src="https://placehold.co/1200x48/1f4e79/ffffff.svg?text=Example%20Queries%20in%20Practice" alt="Example Queries in Practice" width="100%">
</p>

| **Use Case** | **Query Logic** | **Records** | **PMIDs** | **Interpretation** |
|---|---|---:|---:|---|
| Protein cargo | `molecule_type = Protein` | 207,623 | 569 | Broad, high-volume cargo retrieval |
| miRNA cargo | `molecule_type = miRNA` | 16,131 | 120 | Canonical miRNA retrieval |
| Lipid cargo | `molecule_type = Lipid` | 2,896 | 52 | Source-complementary coverage |
| Plasma context | `sample_name contains plasma` | 547 | 444 | Biofluid metadata are retrievable but source-dependent |
| Breast cancer | `disease contains breast cancer` | 12 | 11 | Highlights severe disease metadata sparsity |
| Constrained | Breast cancer + plasma | 6 | 6 | Reveals limited co-annotation overlap |
| Multi-factor | Breast cancer + plasma + miRNA | 0 | 0 | Demonstrates a metadata granularity gap |

A zero result for the triple-constrained query should **not** be interpreted as biological absence. It indicates that current repository snapshots do not connect cargo, disease, and biofluid annotations at a compatible level of granularity.

---

<p align="center">
  <img src="https://placehold.co/1200x48/1f4e79/ffffff.svg?text=Processing%20Workflow" alt="Processing Workflow" width="100%">
</p>

```text
┌──────────────────────────────────────────────┐
│ Repository Exports                           │
│ (Vesiclepedia · ExoCarta · EV-TRACK)         │
└───────────────────────┬──────────────────────┘
                        ▼
┌──────────────────────────────────────────────┐
│ Source-Specific Ingestion                    │
└───────────────────────┬──────────────────────┘
                        ▼
┌──────────────────────────────────────────────┐
│ Canonical Field Mapping                      │
│ (Conservative 18-column schema)              │
└───────────────────────┬──────────────────────┘
                        ▼
┌──────────────────────────────────────────────┐
│ Conservative Normalization                   │
│ (No unsupported biological inference)        │
└───────────────────────┬──────────────────────┘
                        ▼
┌──────────────────────────────────────────────┐
│ Provenance-Preserving Deduplication          │
│ (Source-aware composite key)                 │
└───────────────────────┬──────────────────────┘
                        ▼
┌──────────────────────────────────────────────┐
│ Parquet Master Snapshot                      │
│ (Local, reproducible, query-ready resource)  │
└───────────────────────┬──────────────────────┘
                        ▼
┌──────────────────────────────────────────────┐
│ DuckDB Query Backend                         │
│ (Fast local analytical querying)             │
└───────────────────────┬──────────────────────┘
                        ▼
┌──────────────────────────────────────────────┐
│ Flask Web Interface                          │
│ (Search · filters · plots · PubMed links)    │
└───────────────────────┬──────────────────────┘
                        ▼
┌──────────────────────────────────────────────┐
│ Exportable Results                           │
│ (Tables · utility scores · CSV output)       │
└──────────────────────────────────────────────┘
```

---

<p align="center">
  <img src="https://placehold.co/1200x48/1f4e79/ffffff.svg?text=Repository%20Structure" alt="Repository Structure" width="100%">
</p>

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

| **Path** | **Purpose** |
|---|---|
| `app.py` | Root-level Flask entry point retained for deployment compatibility |
| `Scripts/app.py` | Primary application execution script |
| `evisionary_common.py` | Shared helper functions used across the framework |
| `ontology_terms.py` | Controlled vocabulary and ontology-related logic |
| `synonyms.py` | Query normalization and synonym resources |
| `requirements.txt` | Python dependency list |
| `data/` | Raw inputs, processed snapshots, and validation audit outputs |
| `docs/` | Documentation and supporting manuscript material |
| `static/` | Static graphical assets and styling for the web interface |
| `templates/` | Flask HTML rendering templates |

---

<p align="center">
  <img src="https://placehold.co/1200x48/1f4e79/ffffff.svg?text=Data%20Model" alt="Data Model" width="100%">
</p>

EVisionary maps heterogeneous source exports to a conservative canonical schema. The core fields include:

| **Field** | **Description** |
|---|---|
| `pmid` | PubMed publication identifier |
| `sample_name` | Original sample or biosource descriptor |
| `working_id` | Cargo-level identifier when available |
| `molecule_type_raw` | Original source-reported molecular label |
| `molecule_type_norm` | Normalized molecular label for searchability |
| `molecule_type_group` | Broad molecular class categorization |
| `method` | Isolation or methodological descriptor |
| `species` | Harmonized organism label |
| `year` | Publication year |
| `disease` | Disease or clinical condition annotation |
| `vesicle` | Vesicle subtype or EV-related annotation |
| `ev_metric` | EV-TRACK specific reporting metric |
| `source` | Strict repository provenance tracking |

Missing or ambiguous values are assigned `Unknown`. The framework explicitly avoids inferring missing biological or clinical annotations.

---

<p align="center">
  <img src="https://placehold.co/1200x48/228B22/ffffff.svg?text=Utility%20Score" alt="Utility Score" width="100%">
</p>

To support researchers in triaging results during exploratory searches, EVisionary calculates a record-level utility score. This score reflects metadata completeness, query-match quality, source-prioritization rules, and publication recency.

> **Crucial warning:** The utility score is an auditing and triage tool, **not** a biological confidence score. It must not be interpreted as evidence strength, experimental validity, or biological importance.

---

<p align="center">
  <img src="https://placehold.co/1200x48/228B22/ffffff.svg?text=Installation" alt="Installation" width="100%">
</p>

Clone the repository:

```bash
git clone https://github.com/Sogandste/EVisionary.git
cd EVisionary
```

Create and activate a Python 3.10 environment:

```bash
python3.10 -m venv .venv
source .venv/bin/activate
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

---

<p align="center">
  <img src="https://placehold.co/1200x48/228B22/ffffff.svg?text=Running%20Locally" alt="Running Locally" width="100%">
</p>

Execute the primary application script:

```bash
python Scripts/app.py
```

Once running, open:

```text
http://127.0.0.1:5000
```

Depending on deployment configuration, the root-level entry point may also be used:

```bash
python app.py
```

---

<p align="center">
  <img src="https://placehold.co/1200x48/228B22/ffffff.svg?text=Render%20Deployment" alt="Render Deployment" width="100%">
</p>

The public instance of EVisionary is hosted at:

[https://evisionary.onrender.com/](https://evisionary.onrender.com/)

If deploying via `Scripts/app.py`:

```text
web: gunicorn Scripts.app:app
```

If deploying via the root-level `app.py`:

```text
web: gunicorn app:app
```

Keep `static/`, `templates/`, and root deployment files in their expected directories unless Flask paths are explicitly updated.

---

<p align="center">
  <img src="https://placehold.co/1200x48/228B22/ffffff.svg?text=Input%20Data%20Configuration" alt="Input Data Configuration" width="100%">
</p>

EVisionary is built to process local exports directly from Vesiclepedia, ExoCarta, and EV-TRACK. Recommended internal organization:

```text
data/raw/Vesiclepedia/
data/raw/ExoCarta/
data/raw/EV-TRACK/
data/processed/
data/audit/
```

**Note:** Raw source data must be obtained directly from the original repositories, following their respective licensing and redistribution terms.

---

<p align="center">
  <img src="https://placehold.co/1200x48/228B22/ffffff.svg?text=Programmatic%20Querying%20Python" alt="Programmatic Querying Python" width="100%">
</p>

For bioinformatics pipelines, EVisionary's backend can be queried directly. Example DuckDB query fetching canonical miRNA data:

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

A clinically constrained example searching for breast cancer and plasma markers:

```python
query = rf"""
SELECT source, disease, sample_name, pmid, year
FROM read_parquet('{parquet_path}')
WHERE regexp_matches(lower(disease), 'breast[-\s]+cancer')
  AND regexp_matches(lower(sample_name), '\bplasma\b')
"""

results = con.execute(query).df()
print(results)
```

---

<p align="center">
  <img src="https://placehold.co/1200x48/1f4e79/ffffff.svg?text=Framework%20Validation" alt="Framework Validation" width="100%">
</p>

A comprehensive validation suite supports EVisionary's processing engine, including:

- Field completeness auditing
- Method-field missingness analysis
- Syntax sensitivity testing
- Source complementarity checks
- miRNA presence and routing diagnostics
- Record-to-PMID density analysis
- Ablation testing and error taxonomy
- Manual spot-checking samples
- Clinically constrained query auditing
- Local query speed benchmarking

**Selected validation outcomes:**

| **Validation Item** | **Result** |
|---|---:|
| Initial source rows | 713,667 |
| Final harmonized records | 258,460 |
| Canonical miRNA recovered | 16,131 |
| Missing method field rate | 16.87% |
| Plasma retrieval post-syntax | 547 records |
| Breast cancer retrieval | 12 records |
| Breast cancer + plasma + miRNA | 0 records |

The zero-result metric in triple-constrained queries reflects a systemic metadata co-annotation gap across public repositories, rather than a backend retrieval failure.

---

<p align="center">
  <img src="https://placehold.co/1200x48/1f4e79/ffffff.svg?text=Guidelines%20for%20Reproducibility" alt="Guidelines for Reproducibility" width="100%">
</p>

To ensure reproducibility in downstream publications, users should explicitly report:

- Original source repositories used
- Snapshot dates of the raw exports
- Initial raw row counts
- Applied preprocessing filters
- Deduplication keys
- Final harmonized row count
- Software version or commit hash

Row counts and query outputs will change when updated repository exports are used.

---

<p align="center">
  <img src="https://placehold.co/1200x48/DAA520/ffffff.svg?text=Limitations" alt="Limitations" width="100%">
</p>

EVisionary is a harmonization and query layer, not a replacement for primary EV repositories. Current limitations include:

- Dependence on the completeness of source repository data
- Severe sparsity within disease, biofluid, and clinical-context metadata
- EV-TRACK data represented at the study level rather than the individual cargo level
- No default ontology-based semantic expansion, to prevent over-harmonization
- Utility scores designed strictly for triage, not biological validity

---

<p align="center">
  <img src="https://placehold.co/1200x48/DAA520/ffffff.svg?text=Appropriate%20Use%20Cases" alt="Appropriate Use Cases" width="100%">
</p>

EVisionary is recommended for:

- Rapid exploratory lookup of EV cargo markers
- Source-aware evidence review
- Pre-experimental candidate validation
- Repository-informed biomarker hypothesis generation
- Identifying and documenting repository-specific metadata gaps
- Reproducible workflows for EV data reuse

EVisionary should **not** be used for:

- Definitive claims of biological absence based on zero-result queries
- Acting as a live, real-time federated repository
- Automated, unverified ontology-level entity resolution
- Direct clinical-grade interpretation without expert review

---

<p align="center">
  <img src="https://placehold.co/1200x48/1f4e79/ffffff.svg?text=Citation" alt="Citation" width="100%">
</p>

A comprehensive application note describing EVisionary is currently in preparation. Until formal publication, please cite this framework as:

```text
Sogand. EVisionary: a provenance-aware framework for harmonizing and querying extracellular vesicle repositories. GitHub repository, 2026.
```

Repository: [https://github.com/Sogandste/EVisionary](https://github.com/Sogandste/EVisionary)

---

<p align="center">
  <img src="https://placehold.co/1200x48/1f4e79/ffffff.svg?text=Related%20Resources" alt="Related Resources" width="100%">
</p>

- Vesiclepedia: [https://www.microvesicles.org/](https://www.microvesicles.org/)
- ExoCarta: [http://www.exocarta.org/](http://www.exocarta.org/)
- EV-TRACK: [https://evtrack.org/](https://evtrack.org/)
- DuckDB: [https://duckdb.org/](https://duckdb.org/)
- Apache Parquet: [https://parquet.apache.org/](https://parquet.apache.org/)
- Flask: [https://flask.palletsprojects.com/](https://flask.palletsprojects.com/)

---

<p align="center">
  <img src="https://placehold.co/1200x48/1f4e79/ffffff.svg?text=Data%20Availability" alt="Data Availability" width="100%">
</p>

Raw source datasets must be obtained individually from their original repositories under their respective licensing terms. Derived harmonized outputs, audit tables, and benchmark query results will be released subject to data-source licensing constraints and manuscript publication status.

---

<p align="center">
  <img src="https://placehold.co/1200x48/1f4e79/ffffff.svg?text=License" alt="License" width="100%">
</p>

This project is open-sourced under the MIT License. See the `LICENSE` file for full details.

Please note: the MIT License applies exclusively to the source code developed within this repository. Licensing terms of the original EV data sources must be reviewed and followed independently before redistributing any raw or derived biological datasets.

---

<p align="center">
  <img src="https://placehold.co/1200x48/1f4e79/ffffff.svg?text=Contact%20and%20Support" alt="Contact and Support" width="100%">
</p>

For scientific inquiries, feature suggestions, or collaboration requests:

📧 **shayesteh222sowgand@gmail.com**

To report bugs or technical issues, please use the [Issue Tracker](https://github.com/Sogandste/EVisionary/issues).

---

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=rect&height=35&color=0:1f4e79,55:228B22,100:DAA520&section=footer" alt="EVisionary footer" />
</p>

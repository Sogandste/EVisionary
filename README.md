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

# $\color{#1f4e79}{\text{EVisionary}}$

**A snapshot-based, provenance-aware framework for harmonizing and querying extracellular vesicle repositories**

---

## $\color{#1f4e79}{\text{Overview}}$

EVisionary is a local, snapshot-based framework developed to harmonize and query extracellular vesicle (EV) repository data while preserving the original source provenance. By integrating dated exports from **Vesiclepedia**, **ExoCarta**, and **EV-TRACK**, it creates a unified, locally queryable resource designed specifically for reproducible EV data reuse.

In standard EV bioinformatics workflows, researchers often face a practical limitation: existing repositories contain complementary but structurally heterogeneous information. For instance, Vesiclepedia and ExoCarta primarily report molecular cargo, whereas EV-TRACK captures study-level reporting metadata. The inherent differences in schemas, terminologies, annotation depths, and query behaviors make cross-repository searches notoriously difficult to reproduce and interpret.

To address this, EVisionary harmonizes these disparate sources conservatively. It standardizes selected key fields, retains all raw annotations, preserves repository identity, and strictly avoids unsupported biological inference. Any missing or ambiguous values are represented explicitly as `Unknown`.

> **Note:** EVisionary is **not** a live federated query engine. It operates on dated local snapshots to prioritize reproducibility, full auditability, and stable query behavior over time.

**Live Demo:** [https://evisionary.onrender.com/](https://evisionary.onrender.com/)

---

## $\color{#1f4e79}{\text{Motivation}}$

While EV repositories are incredibly valuable, they are often incomplete when utilized in isolation. Vital details such as cargo-level evidence, disease context, biofluid annotations, species information, and methodological metadata are not consistently captured across sources or at the same level of granularity.

A naive integration approach typically introduces two major issues:
1. **Simple concatenation** may duplicate existing evidence, fragment equivalent labels, or obscure the original source of a record.
2. **Over-harmonization** might collapse labels into unsupported biological equivalences, leading to inaccurate assumptions.

EVisionary takes a conservative middle path. It significantly improves cross-repository search capabilities while ensuring that data provenance, scientific uncertainty, and metadata sparsity remain fully transparent to the researcher.

---

## $\color{#1f4e79}{\text{Key Features}}$

| $\color{#228B22}{\text{Feature}}$ | $\color{#228B22}{\text{Description}}$ |
|---|---|
| $\color{#1f4e79}{\text{Snapshot-based integration}}$ | Uses dated local exports rather than live, unpredictable repository API calls |
| $\color{#1f4e79}{\text{Provenance preservation}}$ | Retains strict source identity throughout the normalization and deduplication pipelines |
| $\color{#1f4e79}{\text{Conservative harmonization}}$ | Normalizes selected fields without making unsupported semantic inferences |
| $\color{#1f4e79}{\text{Multi-cargo support}}$ | Seamlessly includes protein, mRNA, miRNA, lipid, and study-level EV-TRACK records |
| $\color{#1f4e79}{\text{Local query backend}}$ | Leverages Apache Parquet and DuckDB for highly efficient local querying |
| $\color{#1f4e79}{\text{Web interface}}$ | Provides robust search, filtering, summary plots, PubMed links, utility scores, and CSV exports |
| $\color{#1f4e79}{\text{Audit support}}$ | Delivers comprehensive validation outputs for completeness, query stability, and source complementarity |

---

## $\color{#1f4e79}{\text{Current Snapshot Statistics}}$

| $\color{#228B22}{\text{Metric}}$ | $\color{#228B22}{\text{Value}}$ |
|---|---:|
| $\color{#1f4e79}{\text{Source rows processed}}$ | 713,667 |
| $\color{#1f4e79}{\text{Final harmonized records}}$ | 258,460 |
| $\color{#1f4e79}{\text{Cargo-level records}}$ | 253,491 |
| $\color{#1f4e79}{\text{Study-level EV-TRACK records}}$ | 4,969 |
| $\color{#1f4e79}{\text{Vesiclepedia records}}$ | 195,488 |
| $\color{#1f4e79}{\text{ExoCarta records}}$ | 58,003 |
| $\color{#1f4e79}{\text{Missing or unusable method}}$ | 16.87% |

---

## $\color{#1f4e79}{\text{Molecular Cargo Composition}}$

| $\color{#228B22}{\text{Molecular Class}}$ | $\color{#228B22}{\text{Total Records}}$ | $\color{#228B22}{\text{Unique PMIDs}}$ |
|---|---:|---:|
| $\color{#1f4e79}{\text{Protein}}$ | 207,623 | 569 |
| $\color{#1f4e79}{\text{mRNA}}$ | 26,701 | 26 |
| $\color{#1f4e79}{\text{miRNA}}$ | 16,131 | 120 |
| $\color{#1f4e79}{\text{Lipid}}$ | 2,896 | 52 |

*Note: Disease annotations were available in only 4,949 records, corresponding to 1.92% of the harmonized snapshot. This highlights the persistent sparsity of disease and clinical-context metadata, even after comprehensive cross-repository integration.*

---

## $\color{#1f4e79}{\text{Source Complementarity}}$

| $\color{#228B22}{\text{Molecular Class}}$ | $\color{#228B22}{\text{Vesiclepedia}}$ | $\color{#228B22}{\text{ExoCarta}}$ | $\color{#228B22}{\text{Main Pattern}}$ |
|---|---:|---:|---|
| $\color{#1f4e79}{\text{Protein}}$ | 160,806 | 46,817 | Vesiclepedia-dominant |
| $\color{#1f4e79}{\text{mRNA}}$ | 23,307 | 3,394 | Vesiclepedia-dominant |
| $\color{#1f4e79}{\text{miRNA}}$ | 10,091 | 6,040 | Shared coverage |
| $\color{#1f4e79}{\text{Lipid}}$ | 1,283 | 1,613 | ExoCarta-dominant |

The integrated snapshot clearly demonstrates that EV repositories are complementary rather than interchangeable. Biofluid and disease annotations remain highly sparse and deeply source-dependent.

---

## $\color{#1f4e79}{\text{Example Queries in Practice}}$

| $\color{#228B22}{\text{Use Case}}$ | $\color{#228B22}{\text{Query Logic}}$ | $\color{#228B22}{\text{Records}}$ | $\color{#228B22}{\text{PMIDs}}$ | $\color{#228B22}{\text{Interpretation}}$ |
|---|---|---:|---:|---|
| $\color{#1f4e79}{\text{Protein cargo}}$ | `molecule_type = Protein` | 207,623 | 569 | Broad, high-volume cargo retrieval |
| $\color{#1f4e79}{\text{miRNA cargo}}$ | `molecule_type = miRNA` | 16,131 | 120 | Canonical miRNA retrieval |
| $\color{#1f4e79}{\text{Lipid cargo}}$ | `molecule_type = Lipid` | 2,896 | 52 | Source-complementary coverage |
| $\color{#1f4e79}{\text{Plasma context}}$ | `sample_name contains plasma` | 547 | 444 | Biofluid metadata are retrievable but source-dependent |
| $\color{#1f4e79}{\text{Breast cancer}}$ | `disease contains breast cancer` | 12 | 11 | Highlights severe disease metadata sparsity |
| $\color{#1f4e79}{\text{Constrained}}$ | Breast cancer + plasma | 6 | 6 | Reveals limited co-annotation overlap |
| $\color{#1f4e79}{\text{Multi-factor}}$ | Breast cancer + plasma + miRNA | 0 | 0 | Demonstrates a distinct metadata granularity gap |

A zero result for the triple-constrained query should **not** be interpreted as biological absence. Instead, it indicates that the current repository snapshots simply do not connect cargo, disease, and biofluid annotations at a compatible level of granularity.

---

## $\color{#1f4e79}{\text{Processing Workflow}}$

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

## $\color{#1f4e79}{\text{Repository Structure}}$

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

| $\color{#228B22}{\text{Path}}$ | $\color{#228B22}{\text{Purpose}}$ |
|---|---|
| $\color{#1f4e79}{\texttt{app.py}}$ | Root-level Flask entry point retained for deployment compatibility |
| $\color{#1f4e79}{\texttt{Scripts/app.py}}$ | Primary application execution script |
| $\color{#1f4e79}{\texttt{evisionary\_common.py}}$ | Shared helper functions utilized across the framework |
| $\color{#1f4e79}{\texttt{ontology\_terms.py}}$ | Controlled vocabulary and ontology-related logic |
| $\color{#1f4e79}{\texttt{synonyms.py}}$ | Query normalization and advanced synonym resources |
| $\color{#1f4e79}{\texttt{requirements.txt}}$ | Python dependency list |
| $\color{#1f4e79}{\texttt{data/}}$ | Raw data inputs, processed snapshots, and validation audit outputs |
| $\color{#1f4e79}{\texttt{docs/}}$ | Documentation and supporting manuscript material |
| $\color{#1f4e79}{\texttt{static/}}$ | Static graphical assets and styling for the web interface |
| $\color{#1f4e79}{\texttt{templates/}}$ | Flask HTML rendering templates |

---

## $\color{#1f4e79}{\text{Data Model}}$

EVisionary strictly maps heterogeneous source exports to a conservative canonical schema. The core fields include:

| $\color{#228B22}{\text{Field}}$ | $\color{#228B22}{\text{Description}}$ |
|---|---|
| $\color{#1f4e79}{\texttt{pmid}}$ | PubMed publication identifier |
| $\color{#1f4e79}{\texttt{sample\_name}}$ | Original sample or biosource descriptor |
| $\color{#1f4e79}{\texttt{working\_id}}$ | Cargo-level identifier when available |
| $\color{#1f4e79}{\texttt{molecule\_type\_raw}}$ | Original source-reported molecular label |
| $\color{#1f4e79}{\texttt{molecule\_type\_norm}}$| Normalized molecular label for searchability |
| $\color{#1f4e79}{\texttt{molecule\_type\_group}}$| Broad molecular class categorization |
| $\color{#1f4e79}{\texttt{method}}$ | Isolation or methodological descriptor |
| $\color{#1f4e79}{\texttt{species}}$ | Harmonized organism label |
| $\color{#1f4e79}{\texttt{year}}$ | Publication year |
| $\color{#1f4e79}{\texttt{disease}}$ | Disease or clinical condition annotation |
| $\color{#1f4e79}{\texttt{vesicle}}$ | Vesicle subtype or EV-related annotation |
| $\color{#1f4e79}{\texttt{ev\_metric}}$ | EV-TRACK specific reporting metric |
| $\color{#1f4e79}{\texttt{source}}$ | Strict repository provenance tracking |

Any missing or ambiguous values are carefully assigned as `Unknown`. The framework explicitly avoids inferring missing biological or clinical annotations.

---

## $\color{#1f4e79}{\text{Utility Score}}$

To support researchers in triaging results during exploratory searches, EVisionary calculates a record-level **utility score**. This score dynamically reflects metadata completeness, query-match quality, source-prioritization rules, and the recency of the publication.

> **Crucial Warning:** The utility score is an auditing and triage tool, **not** a biological confidence score. It must never be interpreted as an indicator of evidence strength, experimental validity, or biological importance.

---

## $\color{#1f4e79}{\text{Installation}}$

Clone the repository to your local machine:

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

## $\color{#1f4e79}{\text{Running Locally}}$

Execute the primary application script:

```bash
python Scripts/app.py
```

Once running, navigate to the local server in your web browser:

```text
http://127.0.0.1:5000
```

Depending on your specific deployment configuration, the root-level entry point may also be utilized:

```bash
python app.py
```

---

## $\color{#1f4e79}{\text{Render Deployment}}$

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

*Ensure that `static/`, `templates/`, and root deployment files remain in their respective directories unless Flask paths are explicitly updated.*

---

## $\color{#1f4e79}{\text{Input Data Configuration}}$

EVisionary is built to process local exports directly from **Vesiclepedia**, **ExoCarta**, and **EV-TRACK**. 

We recommend the following internal directory organization:
```text
data/raw/Vesiclepedia/
data/raw/ExoCarta/
data/raw/EV-TRACK/
data/processed/
data/audit/
```

*Note: Raw source data must be obtained directly from the original repositories, adhering to their respective licensing and redistribution terms.*

---

## $\color{#1f4e79}{\text{Programmatic Querying (Python)}}$

For bioinformatics pipelines, EVisionary's backend can be queried directly. Below is an example DuckDB query fetching canonical miRNA data:

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

A clinically constrained example (searching for breast cancer and plasma markers):

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

## $\color{#1f4e79}{\text{Framework Validation}}$

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

**Selected Validation Outcomes:**

| $\color{#228B22}{\text{Validation Item}}$ | $\color{#228B22}{\text{Result}}$ |
|---|---:|
| $\color{#1f4e79}{\text{Initial source rows}}$ | 713,667 |
| $\color{#1f4e79}{\text{Final harmonized records}}$ | 258,460 |
| $\color{#1f4e79}{\text{Canonical miRNA recovered}}$ | 16,131 |
| $\color{#1f4e79}{\text{Missing method field rate}}$ | 16.87% |
| $\color{#1f4e79}{\text{Plasma retrieval post-syntax}}$ | 547 records |
| $\color{#1f4e79}{\text{Breast cancer retrieval}}$ | 12 records |
| $\color{#1f4e79}{\text{Breast cancer + plasma + miRNA}}$ | 0 records |

*The zero-result metric in triple-constrained queries reflects a systemic metadata co-annotation gap across public repositories, rather than a backend retrieval failure.*

---

## $\color{#1f4e79}{\text{Guidelines for Reproducibility}}$

To ensure complete reproducibility in downstream publications, users utilizing EVisionary should explicitly report:
- Original source repositories utilized
- Snapshot dates of the raw exports
- Initial raw row counts
- Applied preprocessing filters
- Deduplication keys
- Final harmonized row count
- Software version or specific commit hash

*Be aware that row counts and query outputs will dynamically change when updated repository exports are utilized.*

---

## $\color{#1f4e79}{\text{Limitations}}$

EVisionary serves as a robust harmonization and query layer. It is not intended to replace primary EV repositories. Current known limitations include:
- Absolute dependence on the completeness of source repository data.
- Severe sparsity within disease, biofluid, and clinical-context metadata.
- EV-TRACK data is represented at the study level, rather than the individual cargo level.
- Absence of default ontology-based semantic expansion (to prevent over-harmonization).
- Utility scores are designed strictly for triage, not as metrics of biological validity.

---

## $\color{#1f4e79}{\text{Appropriate Use Cases}}$

**EVisionary is highly recommended for:**
- Rapid, exploratory lookup of EV cargo markers.
- Conducting source-aware, transparent evidence reviews.
- Pre-experimental candidate validation and checking.
- Generating repository-informed biomarker hypotheses.
- Identifying and documenting repository-specific metadata gaps.
- Establishing reproducible workflows for EV data reuse.

**EVisionary should NOT be used for:**
- Making definitive claims of biological absence based on zero-result queries.
- Acting as a live, real-time federated repository.
- Automated, unverified ontology-level entity resolution.
- Direct clinical-grade interpretations without thorough expert review.

---

## $\color{#1f4e79}{\text{Citation}}$

A comprehensive application note detailing EVisionary is currently in preparation. Until formal publication, please cite this framework as:

```text
Sogand. EVisionary: a provenance-aware framework for harmonizing and querying extracellular vesicle repositories. GitHub repository, 2026.
```

Repository Link: [https://github.com/Sogandste/EVisionary](https://github.com/Sogandste/EVisionary)

---

## $\color{#1f4e79}{\text{Related Resources}}$

- **Vesiclepedia:** [https://www.microvesicles.org/](https://www.microvesicles.org/)
- **ExoCarta:** [http://www.exocarta.org/](http://www.exocarta.org/)
- **EV-TRACK:** [https://evtrack.org/](https://evtrack.org/)
- **DuckDB:** [https://duckdb.org/](https://duckdb.org/)
- **Apache Parquet:** [https://parquet.apache.org/](https://parquet.apache.org/)
- **Flask:** [https://flask.palletsprojects.com/](https://flask.palletsprojects.com/)

---

## $\color{#1f4e79}{\text{Data Availability}}$

Raw source datasets must be individually obtained from their original respective repositories under their established licensing terms. Derived harmonized outputs, audit tables, and benchmark query results generated by EVisionary will be formally released subject to data-source licensing constraints and manuscript publication status.

---

## $\color{#1f4e79}{\text{License}}$

This project is open-sourced under the **MIT License**. See the `LICENSE` file for full details. 

*Please note: The MIT License applies exclusively to the source code developed within this repository. The individual licensing terms of the original EV data sources must be reviewed and adhered to independently prior to the redistribution of any raw or derived biological datasets.*

---

## $\color{#1f4e79}{\text{Contact & Support}}$

For scientific inquiries, feature suggestions, or collaboration requests, please contact:

Email: `shayesteh222sowgand@gmail.com`

To report bugs or technical issues, please utilize our Issue Tracker:
[https://github.com/Sogandste/EVisionary/issues](https://github.com/Sogandste/EVisionary/issues)

---

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=rect&height=35&color=0:1f4e79,55:228B22,100:DAA520&section=footer" alt="footer" />
</p>
```

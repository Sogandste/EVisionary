
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

# EVisionary

**A snapshot-based, provenance-aware framework for harmonizing and querying extracellular vesicle repositories**

---

## Overview

EVisionary is a local, snapshot-based framework developed to harmonize and query extracellular vesicle (EV) repository data while preserving the original source provenance. By integrating dated exports from **Vesiclepedia**, **ExoCarta**, and **EV-TRACK**, it creates a unified, locally queryable resource designed specifically for reproducible EV data reuse.

In standard EV bioinformatics workflows, researchers often face a practical limitation: existing repositories contain complementary but structurally heterogeneous information. For instance, Vesiclepedia and ExoCarta primarily report molecular cargo, whereas EV-TRACK captures study-level reporting metadata. The inherent differences in schemas, terminologies, annotation depths, and query behaviors make cross-repository searches notoriously difficult to reproduce and interpret.

To address this, EVisionary harmonizes these disparate sources conservatively. It standardizes selected key fields, retains all raw annotations, preserves repository identity, and strictly avoids unsupported biological inference. Any missing or ambiguous values are represented explicitly as `Unknown`.

> **Note:** EVisionary is **not** a live federated query engine. It operates on dated local snapshots to prioritize reproducibility, full auditability, and stable query behavior over time.

**Live Demo:** [https://evisionary.onrender.com/](https://evisionary.onrender.com/)

---

## Motivation

While EV repositories are incredibly valuable, they are often incomplete when utilized in isolation. Vital details such as cargo-level evidence, disease context, biofluid annotations, species information, and methodological metadata are not consistently captured across sources or at the same level of granularity.

A naive integration approach typically introduces two major issues:
1. **Simple concatenation** may duplicate existing evidence, fragment equivalent labels, or obscure the original source of a record.
2. **Over-harmonization** might collapse labels into unsupported biological equivalences, leading to inaccurate assumptions.

EVisionary takes a conservative middle path. It significantly improves cross-repository search capabilities while ensuring that data provenance, scientific uncertainty, and metadata sparsity remain fully transparent to the researcher.

---

## Key Features

| Feature | Description |
|---|---|
| **Snapshot-based integration** | Uses dated local exports rather than live, unpredictable repository API calls |
| **Provenance preservation** | Retains strict source identity throughout the normalization and deduplication pipelines |
| **Conservative harmonization** | Normalizes selected fields without making unsupported semantic inferences |
| **Multi-cargo support** | Seamlessly includes protein, mRNA, miRNA, lipid, and study-level EV-TRACK records |
| **Local query backend** | Leverages Apache Parquet and DuckDB for highly efficient local querying |
| **Web interface** | Provides robust search, filtering, summary plots, PubMed links, utility scores, and CSV exports |
| **Audit support** | Delivers comprehensive validation outputs for completeness, query stability, and source complementarity |

---

## Current Snapshot Statistics

| Metric | Value |
|---|---:|
| Source rows processed | 713,667 |
| Final harmonized records | 258,460 |
| Cargo-level records | 253,491 |
| Study-level EV-TRACK records | 4,969 |
| Vesiclepedia records | 195,488 |
| ExoCarta records | 58,003 |
| Missing or unusable method field | 16.87% |

---

## Molecular Cargo Composition

| Molecular Class | Total Records | Unique PMIDs |
|---|---:|---:|
| Protein | 207,623 | 569 |
| mRNA | 26,701 | 26 |
| miRNA | 16,131 | 120 |
| Lipid | 2,896 | 52 |

*Note: Disease annotations were available in only 4,949 records, corresponding to 1.92% of the harmonized snapshot. This highlights the persistent sparsity of disease and clinical-context metadata, even after comprehensive cross-repository integration.*

---

## Source Complementarity

| Molecular Class | Vesiclepedia | ExoCarta | Main Pattern |
|---|---:|---:|---|
| Protein | 160,806 | 46,817 | Vesiclepedia-dominant |
| mRNA | 23,307 | 3,394 | Vesiclepedia-dominant |
| miRNA | 10,091 | 6,040 | Shared coverage |
| Lipid | 1,283 | 1,613 | ExoCarta-dominant |

The integrated snapshot clearly demonstrates that EV repositories are complementary rather than interchangeable. Biofluid and disease annotations remain highly sparse and deeply source-dependent.

---

## Example Queries in Practice

| Use Case | Query Logic | Records | PMIDs | Interpretation |
|---|---|---:|---:|---|
| Protein cargo | `molecule_type = Protein` | 207,623 | 569 | Broad, high-volume cargo retrieval |
| miRNA cargo | `molecule_type = miRNA` | 16,131 | 120 | Canonical miRNA retrieval |
| Lipid cargo | `molecule_type = Lipid` | 2,896 | 52 | Demonstrates source-complementary coverage |
| Plasma context | `sample_name contains plasma` | 547 | 444 | Biofluid metadata are retrievable but source-dependent |
| Breast cancer | `disease contains breast cancer` | 12 | 11 | Highlights severe disease metadata sparsity |
| Constrained | Breast cancer + plasma | 6 | 6 | Reveals limited co-annotation overlap |
| Multi-factor | Breast cancer + plasma + miRNA | 0 | 0 | Demonstrates a distinct metadata granularity gap |

A zero result for the triple-constrained query should **not** be interpreted as biological absence. Instead, it indicates that the current repository snapshots simply do not connect cargo, disease, and biofluid annotations at a compatible level of granularity.

---

## Processing Workflow

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
    
    
  
  

Repository Structure

        
        text
        
    
  
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
    
    
  
  
Path	 | 	Purpose
----------------
app.py	 | 	Root-level Flask entry point retained for deployment compatibility
Scripts/app.py	 | 	Primary application execution script
evisionary_common.py	 | 	Shared helper functions utilized across the framework
ontology_terms.py	 | 	Controlled vocabulary and ontology-related logic
synonyms.py	 | 	Query normalization and advanced synonym resources
requirements.txt	 | 	Python dependency list
data/	 | 	Raw data inputs, processed snapshots, and validation audit outputs
docs/	 | 	Documentation and supporting manuscript material
static/	 | 	Static graphical assets and styling for the web interface
templates/	 | 	Flask HTML rendering templates

Data Model

EVisionary strictly maps heterogeneous source exports to a conservative canonical schema. The core fields include:

Field	 | 	Description
---------------------
pmid	 | 	PubMed publication identifier
sample_name	 | 	Original sample or biosource descriptor
working_id	 | 	Cargo-level identifier when available
molecule_type_raw	 | 	Original source-reported molecular label
molecule_type_norm	 | 	Normalized molecular label for searchability
molecule_type_group	 | 	Broad molecular class categorization
method	 | 	Isolation or methodological descriptor
species	 | 	Harmonized organism label
year	 | 	Publication year
disease	 | 	Disease or clinical condition annotation
vesicle	 | 	Vesicle subtype or EV-related annotation
ev_metric	 | 	EV-TRACK specific reporting metric
source	 | 	Strict repository provenance tracking
Any missing or ambiguous values are carefully assigned as Unknown. The framework explicitly avoids inferring missing biological or clinical annotations.


Utility Score

To support researchers in triaging results during exploratory searches, EVisionary calculates a record-level utility score. This score dynamically reflects metadata completeness, query-match quality, source-prioritization rules, and the recency of the publication.


Crucial Warning: The utility score is an auditing and triage tool, not a biological confidence score. It must never be interpreted as an indicator of evidence strength, experimental validity, or biological importance.



Installation

Clone the repository to your local machine:

        
        bash
        
    
  
      git clone https://github.com/Sogandste/EVisionary.git
cd EVisionary
    
    
  
  
Create and activate a Python 3.10 environment:

        
        bash
        
    
  
      python3.10 -m venv .venv
source .venv/bin/activate
    
    
  
  
Install the required dependencies:

        
        bash
        
    
  
      pip install -r requirements.txt
    
    
  
  

Running Locally

Execute the primary application script:

        
        bash
        
    
  
      python Scripts/app.py
    
    
  
  
Once running, navigate to the local server in your web browser:

        
        text
        
    
  
      http://127.0.0.1:5000
    
    
  
  
Depending on your specific deployment configuration, the root-level entry point may also be utilized:

        
        bash
        
    
  
      python app.py
    
    
  
  

Render Deployment

The public instance of EVisionary is hosted at:
https://evisionary.onrender.com/

If deploying via Scripts/app.py:

        
        text
        
    
  
      web: gunicorn Scripts.app:app
    
    
  
  
If deploying via the root-level app.py:

        
        text
        
    
  
      web: gunicorn app:app
    
    
  
  
Ensure that static/, templates/, and root deployment files remain in their respective directories unless Flask paths are explicitly updated.


Input Data Configuration

EVisionary is built to process local exports directly from Vesiclepedia, ExoCarta, and EV-TRACK.

We recommend the following internal directory organization:

        
        text
        
    
  
      data/raw/Vesiclepedia/
data/raw/ExoCarta/
data/raw/EV-TRACK/
data/processed/
data/audit/
    
    
  
  
Note: Raw source data must be obtained directly from the original repositories, adhering to their respective licensing and redistribution terms.


Programmatic Querying (Python)

For bioinformatics pipelines, EVisionary’s backend can be queried directly. Below is an example DuckDB query fetching canonical miRNA data:

        
        python
        
    
  
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
    
    
  
  
A clinically constrained example (searching for breast cancer and plasma markers):

        
        python
        
    
  
      query = f"""
SELECT source, disease, sample_name, pmid, year
FROM read_parquet('{parquet_path}')
WHERE regexp_matches(lower(disease), 'breast[-\\s]+cancer')
  AND regexp_matches(lower(sample_name), '\\bplasma\\b')
"""

results = con.execute(query).df()
print(results)
    
    
  
  

Framework Validation

A comprehensive validation suite supports EVisionary’s processing engine, including:


Field completeness auditing

Method-field missingness analysis

Syntax sensitivity testing

Source complementarity checks

miRNA presence and routing diagnostics

Record-to-PMID density analysis

Ablation testing and error taxonomy

Manual spot-checking samples

Clinically constrained query auditing

Local query speed benchmarking


Selected Validation Outcomes:

Validation Item	 | 	Result
--------------------------
Initial source rows processed	 | 	713,667
Final harmonized records generated	 | 	258,460
Canonical miRNA records successfully recovered	 | 	16,131
Missing or unusable method field rate	 | 	16.87%
Plasma retrieval post-syntax stabilization	 | 	547 records
Breast cancer retrieval post-syntax stabilization	 | 	12 records
Breast cancer + plasma + miRNA multi-query	 | 	0 records
The zero-result metric in triple-constrained queries reflects a systemic metadata co-annotation gap across public repositories, rather than a backend retrieval failure.


Guidelines for Reproducibility

To ensure complete reproducibility in downstream publications, users utilizing EVisionary should explicitly report:


Original source repositories utilized

Snapshot dates of the raw exports

Initial raw row counts

Applied preprocessing filters

Deduplication keys

Final harmonized row count

Software version or specific commit hash


Be aware that row counts and query outputs will dynamically change when updated repository exports are utilized.


Limitations

EVisionary serves as a robust harmonization and query layer. It is not intended to replace primary EV repositories. Current known limitations include:


Absolute dependence on the completeness of source repository data.

Severe sparsity within disease, biofluid, and clinical-context metadata.

EV-TRACK data is represented at the study level, rather than the individual cargo level.

Absence of default ontology-based semantic expansion (to prevent over-harmonization).

Utility scores are designed strictly for triage, not as metrics of biological validity.



Appropriate Use Cases

EVisionary is highly recommended for:


Rapid, exploratory lookup of EV cargo markers.

Conducting source-aware, transparent evidence reviews.

Pre-experimental candidate validation and checking.

Generating repository-informed biomarker hypotheses.

Identifying and documenting repository-specific metadata gaps.

Establishing reproducible workflows for EV data reuse.


EVisionary should NOT be used for:


Making definitive claims of biological absence based on zero-result queries.

Acting as a live, real-time federated repository.

Automated, unverified ontology-level entity resolution.

Direct clinical-grade interpretations without thorough expert review.



Citation

A comprehensive application note detailing EVisionary is currently in preparation. Until formal publication, please cite this framework as:

        
        text
        
    
  
      Sogand. EVisionary: a provenance-aware framework for harmonizing and querying extracellular vesicle repositories. GitHub repository, 2026.
    
    
  
  
Repository Link: https://github.com/Sogandste/EVisionary


Related Resources


Vesiclepedia: https://www.microvesicles.org/

ExoCarta: http://www.exocarta.org/

EV-TRACK: https://evtrack.org/

DuckDB: https://duckdb.org/

Apache Parquet: https://parquet.apache.org/

Flask: https://flask.palletsprojects.com/



Data Availability

Raw source datasets must be individually obtained from their original respective repositories under their established licensing terms. Derived harmonized outputs, audit tables, and benchmark query results generated by EVisionary will be formally released subject to data-source licensing constraints and manuscript publication status.


License

This project is open-sourced under the MIT License. See the LICENSE file for full details.

Please note: The MIT License applies exclusively to the source code developed within this repository. The individual licensing terms of the original EV data sources must be reviewed and adhered to independently prior to the redistribution of any raw or derived biological datasets.


Contact & Support

For scientific inquiries, feature suggestions, or collaboration requests, please contact:

Email: shayesteh222sowgand@gmail.com

To report bugs or technical issues, please utilize our Issue Tracker:
https://github.com/Sogandste/EVisionary/issues



  

```

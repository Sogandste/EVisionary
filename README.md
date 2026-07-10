        
        markdown
        
    
  
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

# EVisionary

**A snapshot-based, provenance-aware framework for harmonizing and querying extracellular vesicle repositories**

---

## Overview

EVisionary is a local, snapshot-based framework for harmonizing and querying extracellular vesicle (EV) repository data while preserving source provenance. It integrates dated exports from **Vesiclepedia**, **ExoCarta**, and **EV-TRACK** into a unified, locally queryable resource designed for reproducible EV data reuse.

The framework addresses a practical limitation in EV bioinformatics: existing EV repositories contain complementary but structurally heterogeneous information. Vesiclepedia and ExoCarta primarily report molecular cargo, whereas EV-TRACK captures study-level reporting metadata. Differences in schema, terminology, annotation depth, and query behavior make cross-repository searches difficult to reproduce and interpret.

EVisionary harmonizes these sources conservatively. It standardizes selected fields, retains raw annotations, preserves repository identity, and avoids unsupported biological inference. Missing or ambiguous values are represented explicitly as `Unknown`.

EVisionary is **not** a live federated query engine. It operates on dated local snapshots to prioritize reproducibility, auditability, and stable query behavior.

**Live demo:** [https://evisionary.onrender.com/](https://evisionary.onrender.com/)

---

## Motivation

EV repositories are valuable but incomplete when used in isolation. Cargo-level evidence, disease context, biofluid annotation, species information, and methodological metadata are not consistently captured across sources or at the same granularity.

Naive integration can introduce two major problems:

1. **Simple concatenation** may duplicate evidence, fragment equivalent labels, or obscure the source of a record.
2. **Over-harmonization** may collapse labels into unsupported biological equivalences.

EVisionary takes a conservative middle path: it improves cross-repository search while keeping provenance, uncertainty, and metadata sparsity visible.

---

## Key Features

| <font color="#228B22">Feature</font> | <font color="#228B22">Description</font> |
|---|---|
| **<font color="#1f4e79">Snapshot-based integration</font>** | Uses dated local exports rather than live repository calls |
| **<font color="#1f4e79">Provenance preservation</font>** | Retains source identity throughout normalization and deduplication |
| **<font color="#1f4e79">Conservative harmonization</font>**| Normalizes selected fields without unsupported semantic inference |
| **<font color="#1f4e79">Multi-cargo support</font>**       | Includes protein, mRNA, miRNA, lipid, and study-level EV-TRACK records |
| **<font color="#1f4e79">Local query backend</font>**       | Uses Apache Parquet and DuckDB for efficient local querying |
| **<font color="#1f4e79">Web interface</font>**             | Provides search, filtering, summary plots, PubMed links, utility scores, and CSV export |
| **<font color="#1f4e79">Audit support</font>**             | Includes validation outputs for completeness, query stability, and source complementarity |

---

## Current Snapshot

| <font color="#228B22">Metric</font> | <font color="#228B22">Value</font> |
|---|---:|
| **<font color="#1f4e79">Source rows processed</font>** | 713,667 |
| **<font color="#1f4e79">Final harmonized records</font>** | 258,460 |
| **<font color="#1f4e79">Cargo-level records</font>** | 253,491 |
| **<font color="#1f4e79">Study-level EV-TRACK records</font>** | 4,969 |
| **<font color="#1f4e79">Vesiclepedia records</font>** | 195,488 |
| **<font color="#1f4e79">ExoCarta records</font>** | 58,003 |
| **<font color="#1f4e79">EV-TRACK records</font>** | 4,969 |
| **<font color="#1f4e79">Missing or unusable method field</font>** | 16.87% |

---

## Molecular Cargo Composition

| <font color="#228B22">Molecular class</font> | <font color="#228B22">Records</font> | <font color="#228B22">Unique PMIDs</font> |
|---|---:|---:|
| **<font color="#1f4e79">Protein</font>** | 207,623 | 569 |
| **<font color="#1f4e79">mRNA</font>** | 26,701 | 26 |
| **<font color="#1f4e79">miRNA</font>** | 16,131 | 120 |
| **<font color="#1f4e79">Lipid</font>** | 2,896 | 52 |

Disease annotations were available in **4,949 records**, corresponding to **1.92%** of the harmonized snapshot. This highlights persistent sparsity of disease and clinical-context metadata even after cross-repository integration.

---

## Source Complementarity

| <font color="#228B22">Molecular class</font> | <font color="#228B22">Vesiclepedia</font> | <font color="#228B22">ExoCarta</font> | <font color="#228B22">Main pattern</font> |
|---|---:|---:|---|
| **<font color="#1f4e79">Protein</font>** | 160,806 | 46,817 | Vesiclepedia-dominant |
| **<font color="#1f4e79">mRNA</font>** | 23,307 | 3,394 | Vesiclepedia-dominant |
| **<font color="#1f4e79">miRNA</font>** | 10,091 | 6,040 | Shared coverage |
| **<font color="#1f4e79">Lipid</font>** | 1,283 | 1,613 | ExoCarta-dominant |

The integrated snapshot shows that EV repositories are complementary rather than interchangeable. In particular, disease and biofluid annotations remain sparse and source-dependent.

---

## Example Queries

| <font color="#228B22">Use case</font> | <font color="#228B22">Query logic</font> | <font color="#228B22">Records</font> | <font color="#228B22">Unique PMIDs</font> | <font color="#228B22">Interpretation</font> |
|---|---|---:|---:|---|
| **<font color="#1f4e79">Protein cargo</font>** | `molecule_type = Protein` | 207,623 | 569 | Broad cargo retrieval |
| **<font color="#1f4e79">miRNA cargo</font>** | `molecule_type = miRNA` | 16,131 | 120 | Canonical miRNA retrieval |
| **<font color="#1f4e79">Lipid cargo</font>** | `molecule_type = Lipid` | 2,896 | 52 | Source-complementary coverage |
| **<font color="#1f4e79">Plasma context</font>** | `sample_name contains plasma` | 547 | 444 | Biofluid metadata are retrievable but source-dependent |
| **<font color="#1f4e79">Breast cancer context</font>** | `disease contains breast cancer` | 12 | 11 | Disease metadata are sparse |
| **<font color="#1f4e79">Breast cancer + plasma</font>** | Combined constraint | 6 | 6 | Limited co-annotation |
| **<font color="#1f4e79">Breast cancer + plasma + miRNA</font>** | Triple constraint | 0 | 0 | Metadata granularity gap |

A zero result for the triple-constrained query should not be interpreted as biological absence. It indicates that the current snapshots do not connect cargo, disease, and biofluid annotations at compatible granularity.

---

## Workflow

```text
Repository exports (Vesiclepedia, ExoCarta, EV-TRACK)
                         |
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
              Parquet master snapshot
                         |
                         v
               DuckDB query backend
                         |
                         v
               Flask web interface
                         |
                         v
  Search results, summary plots, PubMed links, CSV
    
    
  
  

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
Scripts/app.py	 | 	Primary application script
evisionary_common.py	 | 	Shared helper functions used across the application
ontology_terms.py	 | 	Controlled vocabulary and ontology-related terms
synonyms.py	 | 	Query normalization and synonym resources
requirements.txt	 | 	Python dependency list
data/	 | 	Raw data, processed snapshots, and audit outputs
docs/	 | 	Documentation and supporting material
static/	 | 	Static assets for the web interface
templates/	 | 	Flask HTML templates

Data Model

EVisionary maps heterogeneous source exports to a conservative canonical schema. Core fields include:

Field	 | 	Description
---------------------
pmid	 | 	PubMed identifier
sample_name	 | 	Sample or biosource descriptor
working_id	 | 	Cargo-level identifier when available
molecule_type_raw	 | 	Original source-reported molecule label
molecule_type_norm	 | 	Normalized molecule label
molecule_type_group	 | 	Broad molecular class
method	 | 	Isolation or methodological descriptor
species	 | 	Harmonized organism label
year	 | 	Publication year
disease	 | 	Disease or condition annotation
vesicle	 | 	Vesicle subtype or EV-related annotation
ev_metric	 | 	EV-TRACK reporting metric
source	 | 	Repository provenance
Missing or ambiguous values are assigned Unknown. EVisionary does not infer missing biological or clinical annotations.


Utility Score

EVisionary provides a record-level utility score to support result triage during exploratory searches. The score reflects metadata completeness, query-match quality, source-prioritization rules, and publication year.

The utility score is not a biological confidence score. It should not be interpreted as evidence strength, experimental validity, or biological importance.


Installation

Clone the repository:

        
        bash
        
    
  
      git clone https://github.com/Sogandste/EVisionary.git
cd EVisionary
    
    
  
  
Create and activate a Python 3.10 environment:

        
        bash
        
    
  
      python3.10 -m venv .venv
source .venv/bin/activate
    
    
  
  
Install dependencies:

        
        bash
        
    
  
      pip install -r requirements.txt
    
    
  
  

Running Locally

Run the primary application script:

        
        bash
        
    
  
      python Scripts/app.py
    
    
  
  
Then open:

        
        text
        
    
  
      http://127.0.0.1:5000
    
    
  
  
Depending on deployment configuration, the root-level entry point may also be used:

        
        bash
        
    
  
      python app.py
    
    
  
  

Render Deployment

The public demo is available at:

https://evisionary.onrender.com/

If deployment uses Scripts/app.py:

        
        text
        
    
  
      web: gunicorn Scripts.app:app
    
    
  
  
If deployment uses root-level app.py:

        
        text
        
    
  
      web: gunicorn app:app
    
    
  
  
Do not move static/, templates/, or deployment-related root files without updating Flask paths and the Render start command.


Input Data

EVisionary expects local exports from:


Vesiclepedia

ExoCarta

EV-TRACK


Recommended local organization:

        
        text
        
    
  
      data/raw/Vesiclepedia/
data/raw/ExoCarta/
data/raw/EV-TRACK/
data/processed/
data/audit/
    
    
  
  
Raw source data should be obtained from the original repositories according to their licensing and redistribution terms.


Programmatic Querying

Example DuckDB query:

        
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
    
    
  
  
Clinically constrained example:

        
        python
        
    
  
      query = f"""
SELECT source, disease, sample_name, pmid, year
FROM read_parquet('{parquet_path}')
WHERE regexp_matches(lower(disease), 'breast[-\\s]+cancer')
  AND regexp_matches(lower(sample_name), '\\bplasma\\b')
"""

results = con.execute(query).df()
print(results)
    
    
  
  

Validation

The validation workflow includes:


field completeness auditing;

method-field missingness analysis;

syntax sensitivity testing;

source complementarity analysis;

miRNA presence and routing diagnostics;

record-to-PMID density analysis;

ablation analysis;

error taxonomy;

manual spot-checking;

clinically constrained query auditing;

local query benchmarking.


Selected validation results:

Validation item	 | 	Result
--------------------------
Source rows processed	 | 	713,667
Final harmonized records	 | 	258,460
Canonical miRNA records recovered	 | 	16,131
Missing or unusable method field	 | 	16.87%
Plasma retrieval after syntax stabilization	 | 	547 records
Breast cancer retrieval after syntax stabilization	 | 	12 records
Breast cancer + plasma + miRNA query	 | 	0 records
The zero-result triple-constrained query reflects a metadata co-annotation gap rather than a backend retrieval failure.


Reproducibility

For reproducible use, users should report:


source repositories;

snapshot dates;

raw row counts;

preprocessing filters;

deduplication key;

final harmonized row count;

software version or commit hash.


Row counts may change when newer repository exports are used.


Limitations

EVisionary is a harmonization and query layer, not a replacement for primary EV repositories.

Current limitations include:


dependence on source repository completeness;

sparse disease, biofluid, and clinical-context metadata;

study-level rather than cargo-level EV-TRACK records;

no default ontology-based semantic expansion;

zero-result queries may reflect metadata gaps rather than biological absence;

utility scores support triage, not biological confidence;

snapshot updates may change reported counts.



Appropriate Use Cases

EVisionary is suitable for:


exploratory EV cargo lookup;

source-aware evidence review;

pre-experimental candidate checking;

biomarker hypothesis generation;

identifying repository-specific metadata gaps;

preparing reproducible EV data-reuse workflows.


It is not intended for:


definitive biological absence claims;

live repository federation;

automated ontology-level entity resolution;

clinical-grade interpretation without expert review.



Citation

A manuscript describing EVisionary is currently in preparation. Until publication, please cite the repository as:

        
        text
        
    
  
      Sogand. EVisionary: a provenance-aware framework for harmonizing and querying extracellular vesicle repositories. GitHub repository, 2026.
    
    
  
  
Repository:

https://github.com/Sogandste/EVisionary


Related Resources


Vesiclepedia: https://www.microvesicles.org/

ExoCarta: http://www.exocarta.org/

EV-TRACK: https://evtrack.org/

DuckDB: https://duckdb.org/

Apache Parquet: https://parquet.apache.org/

Flask: https://flask.palletsprojects.com/



Data Availability

Raw source data should be obtained from the original repositories under their respective licensing terms.

Derived harmonized outputs, audit tables, and example query results will be released subject to data-source licensing constraints and manuscript status.


License

This project is released under the MIT License. See LICENSE for details.

The MIT License applies to the source code in this repository. Licensing terms of the original EV data sources should be checked separately before redistribution of raw or derived datasets.


Contact

For questions, suggestions, or collaboration requests:

        
        text
        
    
  
      shayesteh222sowgand@gmail.com
    
    
  
  
Issue tracker:

https://github.com/Sogandste/EVisionary/issues


Summary

EVisionary provides a reproducible, source-aware query layer for extracellular vesicle repository data. It harmonizes heterogeneous EV records into a local Parquet-based resource while preserving provenance and making metadata gaps explicit.


  

```

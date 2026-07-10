        
        markdown
        
    
  
      <div align="center">

🟦🟦🟦&nbsp;&nbsp;🟩🟩🟩&nbsp;&nbsp;⬜⬜⬜&nbsp;&nbsp;🟨🟨🟨

</div>

# EVisionary

**A snapshot-based, provenance-aware framework for harmonizing and querying extracellular vesicle repositories**

[![Python](https://img.shields.io/badge/Python-3.10-228B22?labelColor=1f4e79)](https://www.python.org/)
[![DuckDB](https://img.shields.io/badge/DuckDB-query%20engine-DAA520?labelColor=1f4e79)](https://duckdb.org/)
[![Flask](https://img.shields.io/badge/Flask-web%20interface-E0E0E0?labelColor=1f4e79)](https://flask.palletsprojects.com/)
[![Parquet](https://img.shields.io/badge/Apache%20Parquet-local%20snapshot-228B22?labelColor=1f4e79)](https://parquet.apache.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-DAA520?labelColor=1f4e79)](LICENSE)
[![Demo](https://img.shields.io/badge/Demo-Render-228B22?labelColor=1f4e79)](https://evisionary.onrender.com/)

---

## Overview

Extracellular vesicle (EV) research depends on three community repositories that serve complementary but structurally incompatible roles. **Vesiclepedia** and **ExoCarta** function as molecular cargo catalogues — indexing proteins, mRNAs, miRNAs, and lipids reported in EV isolates — while **EV-TRACK** captures study-level experimental reporting metadata. Each repository operates under a distinct schema, controlled vocabulary, and annotation granularity, which makes cross-repository querying a manual, error-prone exercise. A question as straightforward as *"which miRNAs have been reported in plasma-derived EVs from breast cancer cohorts"* cannot be answered by any single source and typically requires researchers to search each repository independently and reconcile identifiers by hand.

EVisionary addresses this gap by converting dated repository exports into a single, locally queryable snapshot — harmonized sufficiently to support unified search, but conservative enough to avoid introducing biological relationships that the source data does not substantiate. Source attribution is preserved at the record level throughout normalization and deduplication. Raw fields are retained alongside their normalized counterparts. Missing values are explicitly marked as `Unknown` rather than inferred.

A critical design distinction: **EVisionary is not a federated query engine.** It operates on static snapshots obtained on a specific date, processed once and queried locally. This architectural choice prioritizes reproducibility over currency — a trade-off that is appropriate for meta-analytical workflows and systematic evidence review, but means the snapshot will inevitably lag behind the live repositories.

A live demo is available for interactive exploration:

```text
https://evisionary.onrender.com/
    
    
  
  

Background and problem statement

The three repositories are not redundant — they answer fundamentally different questions. Vesiclepedia and ExoCarta report what molecular content was identified in an EV preparation. EV-TRACK reports how rigorously a study documented its isolation and characterization methodology. Neither cargo-centric repository reliably captures clinical co-annotation (disease, biofluid, cohort context) at the same granularity as cargo data, and EV-TRACK does not index cargo at all. Consequently, queries that require simultaneous cargo, disease, and biofluid annotation frequently return null results — not because the underlying biology is absent, but because the metadata required to connect those dimensions is sparse or distributed across repositories.

Two failure modes recur in naive integration attempts:



Unprincipled concatenation fragments semantically identical labels into numerous near-duplicate entries, inflates apparent evidence counts through cross-repository double-counting, and obscures the original source of each record.




Over-aggressive harmonization collapses heterogeneous labels into unified ontology terms, silently introducing biological equivalences that the source data never explicitly supported — a particularly dangerous failure mode in clinical contexts.




EVisionary occupies the middle ground: schema standardization with strict source attribution, lexical normalization without semantic inference, and transparent reporting of metadata gaps rather than their concealment.


Core functionality

Capability	 | 	Implementation
-----------------------------
Snapshot architecture	 | 	Local, dated exports replace live remote calls — ensuring reproducibility at the cost of currency
Provenance preservation	 | 	Source identity (🟦 Vesiclepedia / 🟩 ExoCarta / ⬜ EV-TRACK) survives all transformations
Schema harmonization	 | 	18 canonical fields mapped conservatively from source-specific schemas
Cargo coverage	 | 	Protein, mRNA, miRNA, lipid records plus study-level EV-TRACK entries
Deduplication	 | 	Seven-field composite key including source — prevents cross-repository collapse
Query backend	 | 	Apache Parquet storage + DuckDB execution — interactive performance on standard hardware
Missing data policy	 | 	Explicit Unknown labeling — no interpolation, no inference
The web interface supports free-text search, structured filtering, summary visualizations (source, molecular class, species, publication year), direct PubMed linking, a record-level utility score for result triage, and CSV export. A comprehensive validation suite (detailed below) audits field completeness, syntax sensitivity, source complementarity, and clinically constrained query behavior.


Snapshot statistics

Metric	 | 	Value
----------------
Source rows processed	 | 	713,667
Final harmonized records	 | 	258,460
Cargo-level records	 | 	253,491
Study-level EV-TRACK records	 | 	4,969
🟦 Vesiclepedia records	 | 	195,488
🟩 ExoCarta records	 | 	58,003
⬜ EV-TRACK records	 | 	4,969
Missing or unusable method field	 | 	16.87%
Molecular cargo distribution:

Molecular class	 | 	Records	 | 	Unique PMIDs
--------------------------------------------
Protein	 | 	207,623	 | 	569
mRNA	 | 	26,701	 | 	26
miRNA	 | 	16,131	 | 	120
Lipid	 | 	2,896	 | 	52
Disease annotation is present for 4,949 records (1.92% of the harmonized snapshot). Even with three-source integration, clinical-context metadata remains markedly sparse — a structural limitation of the source data rather than a processing deficiency.


Source complementarity analysis

Molecular class	 | 	🟦 Vesiclepedia	 | 	🟩 ExoCarta	 | 	Distribution pattern
----------------------------------------------------------------------------
Protein	 | 	160,806	 | 	46,817	 | 	Vesiclepedia-dominant
mRNA	 | 	23,307	 | 	3,394	 | 	Vesiclepedia-dominant
miRNA	 | 	10,091	 | 	6,040	 | 	Approximately balanced
Lipid	 | 	1,283	 | 	1,613	 | 	ExoCarta-dominant
Plasma and breast-cancer annotations exhibit strong source-dependency in the current snapshot. A null result from one repository does not preclude retrieval from another — a distinction that EVisionary surfaces explicitly, converting ambiguous zero-results into actionable “check alternative source” signals.


Representative query examples

Use case	 | 	Query logic	 | 	Records	 | 	Unique PMIDs	 | 	Interpretation
------------------------------------------------------------------------
Protein cargo	 | 	molecule_type = Protein	 | 	207,623	 | 	569	 | 	Broad retrieval, provenance preserved
miRNA cargo	 | 	molecule_type = miRNA	 | 	16,131	 | 	120	 | 	Stable canonical retrieval
Lipid cargo	 | 	molecule_type = Lipid	 | 	2,896	 | 	52	 | 	Source-complementary coverage
Plasma biofluid	 | 	sample_name contains plasma	 | 	547	 | 	444	 | 	Retrievable, source-dependent
Breast cancer	 | 	disease contains breast cancer	 | 	12	 | 	11	 | 	Sparse, repository-dependent
Breast cancer + plasma	 | 	Combined constraint	 | 	6	 | 	6	 | 	Co-annotation exists but minimal
Breast cancer + plasma + miRNA	 | 	Triple constraint	 | 	0	 | 	0	 | 	Metadata granularity gap
The final row warrants emphasis: a zero-result return does not indicate biological absence. It indicates that the current snapshots do not connect cargo, disease, and biofluid annotations at mutually compatible granularity — a metadata limitation, not a query-engine failure.


Pipeline architecture

        
        text
        
    
  
      Repository exports (Vesiclepedia, ExoCarta, EV-TRACK)
        │
        ▼
Source-specific ingestion
        │
        ▼
Canonical field mapping (18-column schema)
        │
        ▼
Conservative normalization (no semantic inference)
        │
        ▼
Provenance-preserving deduplication (7-field composite key)
        │
        ▼
Parquet master snapshot
        │
        ▼
DuckDB query backend
        │
        ▼
Flask web interface
        │
        ▼
Interactive tables, summary plots, PubMed links, utility scores, CSV export
    
    
  
  

Repository structure

        
        text
        
    
  
      EVisionary/
├── app.py                          # Render-compatible entry point
├── evisionary_common.py            # Shared helper functions
├── ontology_terms.py               # Controlled vocabulary definitions
├── synonyms.py                     # Query normalization logic
├── requirements.txt
├── LICENSE
├── README.md
├── Procfile                        # Render deployment configuration
├── Scripts/
│   └── app.py                      # Primary application script
├── data/                           # Raw exports, processed snapshots, audit tables
├── docs/                           # Documentation
├── static/                         # Flask static assets
└── templates/                      # Flask HTML templates
    
    
  
  
The root-level app.py exists primarily for Render deployment compatibility. The functional application resides in Scripts/app.py. Shared logic is distributed across evisionary_common.py (utilities), ontology_terms.py (controlled vocabulary), and synonyms.py (query normalization).


Data model

Eighteen canonical fields, mapped conservatively from source schemas:

Field	 | 	Description
---------------------
pmid	 | 	PubMed publication identifier
sample_name	 | 	Sample / biosource descriptor
working_id	 | 	Cargo-level identifier (where available)
molecule_type_raw	 | 	Original source label (preserved verbatim)
molecule_type_norm	 | 	Normalized canonical label
molecule_type_group	 | 	Broader molecular classification
method	 | 	Isolation / methodology descriptor
species	 | 	Harmonized organism label (curated dictionary)
year	 | 	Publication year
disease	 | 	Disease / condition annotation
vesicle	 | 	Vesicle subtype (where annotated)
ev_metric	 | 	EV-TRACK experimental reporting metric
source	 | 	Repository of origin (🟦 Vesiclepedia / 🟩 ExoCarta / ⬜ EV-TRACK)
Missing or ambiguous values are explicitly assigned Unknown. No field is populated by inference, interpolation, or external ontology mapping.


Design boundaries

Implemented functionality:


Schema harmonization across heterogeneous source structures

Lexical normalization of free-text fields

Species-label standardization against a curated reference dictionary

Source-aware deduplication preventing cross-repository entity collapse

Syntax-tolerant query behavior stable against minor input variation


Deliberately excluded:


Live federated querying against remote repositories

Automatic ontology-based synonym expansion

Cross-repository entity resolution into unsupported biological equivalences

Inference of cargo-level facts from study-level metadata

Confidence scoring of underlying biological claims


The exclusion list is arguably the more scientifically important specification. Integration tools that silently fill metadata gaps risk producing results that appear more complete than the source data warrants — EVisionary is designed to resist this failure mode.


Utility score

Each record receives a composite score intended to support result triage during exploratory search. The score integrates metadata completeness, query-match quality, source-prioritization rules, and publication recency.

Important caveat: The utility score is a sorting heuristic, not a validation metric. It carries no implication regarding biological significance, experimental rigor, or evidentiary strength. A high-utility record should be interpreted as “prioritized for manual review,” not “prioritized for citation.”


Installation and execution

Clone the repository:

        
        bash
        
    
  
      git clone https://github.com/Sogandste/EVisionary.git
cd EVisionary
    
    
  
  
Configure Python environment (3.10):

        
        bash
        
    
  
      python3.10 -m venv .venv
source .venv/bin/activate
    
    
  
  
Windows alternative: python -m venv .venv followed by .venv\Scripts\activate

Install dependencies:

        
        bash
        
    
  
      pip install -r requirements.txt
    
    
  
  
Launch the application:

        
        bash
        
    
  
      python Scripts/app.py
    
    
  
  
The interface will be available at http://127.0.0.1:5000. The root-level app.py may also serve as an entry point (python app.py), retained primarily for Render deployment compatibility.


Render deployment

The public demo is hosted at https://evisionary.onrender.com/. The Procfile configuration depends on the active entry point:

If using Scripts/app.py:

        
        text
        
    
  
      web: gunicorn Scripts.app:app
    
    
  
  
If using root-level app.py:

        
        text
        
    
  
      web: gunicorn app:app
    
    
  
  

Warning: Relocating static/, templates/, or root deployment files without correspondingly updating Flask path configurations and the Render start command will cause silent deployment failure.



Expected input data

Raw exports from Vesiclepedia, ExoCarta, and EV-TRACK, obtained directly from the source repositories under their respective licensing terms. Recommended local directory structure:

        
        text
        
    
  
      data/raw/Vesiclepedia/
data/raw/ExoCarta/
data/raw/EV-TRACK/
data/processed/
data/audit/
    
    
  
  
Large data files are excluded from the GitHub repository for size and licensing considerations and are distributed through alternative channels.


Direct DuckDB querying

Basic cargo retrieval:

        
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
    
    
  
  
Clinically constrained query:

        
        python
        
    
  
      query = f"""
SELECT source, disease, sample_name, pmid, year
FROM read_parquet('{parquet_path}')
WHERE regexp_matches(lower(disease), 'breast[-\\s]+cancer')
  AND regexp_matches(lower(sample_name), '\\bplasma\\b')
"""

results = con.execute(query).df()
print(results)
    
    
  
  

Validation framework

The audit suite encompasses:


Field completeness analysis

Method-field missingness quantification

Syntax sensitivity testing

Gain-provenance analysis (empirical contribution of multi-source integration)

miRNA routing diagnostics

Source complementarity assessment

Record-to-PMID density evaluation

Ablation analysis

Error taxonomy classification

Manual spot-check validation

Clinically constrained query testing


Selected validation results:

Metric	 | 	Result
-----------------
Source rows processed	 | 	713,667
Final harmonized records	 | 	258,460
miRNA records recovered via multi-cargo integration	 | 	16,131
Records with missing/unusable method field	 | 	16.87%
Plasma retrieval (exact-string → syntax-stabilized)	 | 	2 → 547
Breast cancer retrieval (exact-string → syntax-stabilized)	 | 	8 → 12
Triple-constrained query (breast cancer + plasma + miRNA)	 | 	0 results
The 16,131 canonical miRNA records were recoverable specifically because of multi-cargo integration — none would have surfaced from a single-source search. The triple-constrained null result persists despite individual-term retrievability, empirically confirming the metadata granularity gap rather than a backend deficiency.


Reproducibility guidelines

Given that source repositories undergo continuous updates, reproducible analysis requires documentation of:


Source repositories and snapshot acquisition dates

Raw row counts per source

Filtering criteria applied during preprocessing

Deduplication key specification

Final harmonized row count

Code commit hash or version tag


Reported statistics will drift as new source exports become available. This is expected behavior, not a defect.


Limitations


EVisionary is a harmonization and query layer, not a replacement for primary repositories

It inherits all metadata gaps present in source exports

Disease, biofluid, and clinical-context annotation remain sparse regardless of integration quality

EV-TRACK contributes study-level metadata only — it cannot fill cargo-level gaps

No ontology-based semantic expansion is performed by default

Zero-result queries may indicate metadata gaps rather than biological absence

The utility score supports triage, not evidentiary assessment

Future snapshots will shift reported statistics



Appropriate use cases

Suitable applications:


Exploratory EV cargo interrogation

Pre-experimental candidate validation

Evidence review with preserved source attribution

Biomarker hypothesis generation

Metadata gap identification across repositories

Systematic EV data-reuse workflow preparation


Unsuitable applications:


Definitive claims of biological absence

Workflows requiring live repository federation

Automated cross-ontology entity resolution

Clinical-grade interpretation replacing expert curation



Citation

A manuscript is currently in preparation. Pending publication, please cite as:

        
        text
        
    
  
      Sogand. EVisionary: a provenance-aware framework for harmonizing and querying extracellular vesicle repositories. GitHub repository, 2026.
    
    
  
  
        
        text
        
    
  
      https://github.com/Sogandste/EVisionary
    
    
  
  

Related resources


Vesiclepedia — https://www.microvesicles.org/

ExoCarta — http://www.exocarta.org/

EV-TRACK — https://evtrack.org/

DuckDB — https://duckdb.org/

Apache Parquet — https://parquet.apache.org/

Flask — https://flask.palletsprojects.com/



Data availability

Raw source data are available from the original repositories under their respective licensing terms. Derived harmonized outputs, audit tables, and example query results will be released contingent upon licensing review and manuscript publication status.


License

MIT License — see LICENSE file.


Note: This license covers the source code only. Licensing terms of the original EV data sources must be verified independently before redistribution of raw or derived datasets.



Contact

        
        text
        
    
  
      shayesteh222sowgand@gmail.com
    
    
  
  
Issue tracker: https://github.com/Sogandste/EVisionary/issues


Summary

EVisionary is a local, snapshot-based framework that harmonizes extracellular vesicle repository exports into an auditable Parquet resource, preserves source provenance throughout all transformations, and renders cross-repository metadata gaps visible rather than concealing them — enabling reproducible, source-aware querying for the EV research community.


🟨🟨🟨  ⬜⬜⬜  🟩🟩🟩  🟦🟦🟦



```

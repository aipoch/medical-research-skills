# Medical Research Agent Skills

[![License](https://img.shields.io/badge/License-MIT-ff6b6b?style=for-the-badge)](./LICENSE)
![Skills Count](https://img.shields.io/badge/Skills-500%2B-4dabf7?style=for-the-badge)
[![Follow on X](https://img.shields.io/badge/Follow%20on%20X-%40aipoch__ai-212529?style=for-the-badge&logo=x&logoColor=white)](https://x.com/aipoch_ai)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-AIPOCH-0a66c2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/company/pochai)
[![YouTube](https://img.shields.io/badge/YouTube-%40AIPOCH__AI-ff0000?style=for-the-badge&logo=youtube&logoColor=white)](https://www.youtube.com/@AIPOCH_AI)

A curated library of 550+ medical research agent skills created by [AIPOCH](https://www.aipoch.com), designed to work with **Claude Code, Codex**, and other `SKILL.md`-compatible agent platforms. It supports the research workflow across four core areas: Evidence Insights, Protocol Design, Data Analysis, and Academic Writing. Built exclusively for medical and biomedical researchers.

[**AIPOCH Open-Science**](https://github.com/aipoch/open-science), AIPOCH's open-source AI research workbench, includes a selection of the skills from this library for use within its research workspace.

Every skill in this library is reviewed and evaluated through [**MedSkillAudit**](https://www.aipoch.com/benchmark) — A Domain-Specific Audit Framework for Medical Research Agent Skills — before going live. Equip your AI agent with AIPOCH medical research skills, and turn it into a capable medical research assistant.

> ⭐ **Star this repo** — the library is actively maintained and grows with new skills, improvements, and fixes regularly. Hit the star button to keep it close, stay current with the latest releases, and help more researchers discover Medical Research Agent Skills. Every star directly supports the continued development of this library.

<br>

<a href="https://www.aipoch.com/">
    <img src="https://github.com/user-attachments/assets/1a6a7005-d9fc-49d5-8dba-3cb822d7e71d" alt="AIPOCH Demo GIF" width="800"/>
  </a>

---

> 💡 **Use selected skills in AIPOCH Open-Science:** Work with scientific agents, Python/R notebooks, and research files in one open-source, model-agnostic workspace. AIPOCH Open-Science includes a subset of this library. [Get started with AIPOCH Open-Science](https://github.com/aipoch/open-science#-quick-start).

> **MedSkillAudit** - a domain-specific audit framework for medical research agent skills. [Try skill-auditor here.](https://github.com/aipoch/medical-research-skills/tree/main/skill-auditor)

## 🗂️ Skills Overview

All skills in AIPOCH are ​**originally designed and developed in-house**​, built to reflect medical research workflows and standards. The library is primarily organized into five categories: ​**Evidence Insights, Protocol Design, ​Data Analysis, Academic Writing**​, and Others.

| 📚**Category**                        | **Highlights**                                                                                                                                    |
| ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| 🔍 **Evidence Insight**               | e.g., search strategy design, database selection, evidence-level prioritization, critical appraisal, literature synthesis and gap identification. |
| 🧪 **Protocol Design**                | e.g., experimental design generation, study type selection, causal inference planning, statistical power calculation, validation strategy.        |
| 📊 **Data Analysis**                  | e.g., R/Python bioinformatics code generation, statistical modeling, data cleaning pipelines, machine learning workflows, result visualization.   |
| ✍️ **Academic Writing**               | e.g., SCI manuscript drafting, methods/results/discussion writing, meta-analysis narrative, cover letters, abstract generation.                   |
| 🌍 **Other (General / Non-Research)** | all general skills that do not fall into categories 1–4.                                                                                          |

## 🗂️ Browse by Research Stage

### 🔍 Literature \& Evidence Discovery — 79 skills

Before a study begins, researchers need to know what is already established, where the evidence is weak, and where the genuine gaps are\. This category covers the full evidence pipeline: building precision search strategies across PubMed and multiple databases, screening literature at scale, reading papers with methodological depth, mapping the evidence landscape around a disease or biomarker, and identifying research gaps with an evidence audit trail\.

- **Search \& retrieval** — PubMed Boolean query builder, multi\-database search strategy designer, preprint surveillance across bioRxiv and medRxiv, weekly research digest by keyword, literature filtering by study design and relevance, clinical question clarifier
- **Structured paper reading** — close reading with structured annotation, extensive reading for rapid topic coverage, figure\-first reading workflow, methods reverse\-engineering, result reliability assessment, evidence level ranking by study design, high\-value paper screener, full research literature reading pipeline, academic paper reading and research development system
- **Evidence landscape** — disease mechanism evidence mapper, biomarker landscape scanner by type and validation level, drug and target evidence organizer, research hotspot and trend analysis, emerging topic scout, keyword velocity tracker, topic evidence mapper
- **Gap identification** — evidence\-audited medical research gap finder, population gap detector, method gap detector, unmet clinical need extractor, basic\-to\-clinical translational opportunity finder, bioinformatics\-to\-clinical translational opportunity finder, topic saturation and whitespace checker, novelty vs feasibility assessor
- **Citation \& integrity** — citation network builder and visualizer, citation chasing and lineage mapping, retraction watcher, paper\-to\-claim verifier, contradictory findings resolver, target novelty scorer, translational gap analyzer
- **Research intelligence** — systematic review screener with PRISMA workflow support, clinical study information extractor from PMIDs, experimental protocol extractor from publications, methodology extractor for batch protocol comparison, funding trend forecaster, NIH grant funding scout, study design identifier, research paper downloader from open\-access sources

### 🧪 Study Design \& Protocol Development — 68 skills

Moving from a research question to a submission\-ready protocol requires choosing the right study architecture, controlling for bias sources, and justifying every design decision to reviewers and ethics boards\. This category provides hypothesis formulation tools, study design selectors, sample size calculators, and 30\+ disease\- and method\-specific study planners that generate full protocol drafts grounded in current methodological standards\.

- **Core design tools** — hypothesis generator, aim and hypothesis designer, study objective refiner, primary plan recommender, feasibility\-aware study planner, inclusion and exclusion criteria builder, endpoint definition designer, sample size and power planning assistant, confounder and bias control planner, validation strategy designer, basic research design advisor, clinical research design advisor, automated LLM\-driven hypothesis generation and testing for tabular datasets
- **Translational pathway** — mechanism\-to\-validation planner, translational study blueprint, animal and cell validation planner, gap\-to\-study design converter, research algorithm matcher for data modality and resource constraints
- **Clinical study planners** — clinical cohort protocol designer, case\-control study planner, real\-world evidence study designer using EHR, claims, or registry data, prognostic biomarker protocol designer, treatment response predictor planner, Mendelian randomization protocol designer, QTL colocalization study planner, drug repurposing study planner, single\-cell research planner, bulk omics integrative planner, multi\-omics clinical integration planner
- **Specialized study planners** — two\-sample Mendelian randomization, bidirectional multi\-phenotype MR, MR and scRNA\-seq integration, NHANES biomarker study, FAERS pharmacovigilance disproportionality, FAERS multi\-drug single\-SOC safety comparison, single\-drug FAERS safety profile, active comparator FAERS safety comparison, network toxicology and molecular docking, dual\-disease transcriptomic ML, dual\-disease shared transcriptome biomarker, tumor immune infiltration diagnostic ML, conventional oncology hub\-gene, conventional non\-oncology hub\-gene, non\-tumor ML, non\-tumor mechanism\-guided diagnostic ML, cross\-disease shared biomarker network, comorbidity common immune biomarker, PCD immune oncology, single\-gene oncology reference\-grounded, generic phenotype scoring, process\-related diagnostic biomarker nomogram, pathway\-anchored network pharmacology, hub\-first network pharmacology, single\-compound network toxicology disease link, comparative network toxicology shared mechanism, two\-sample MR exposure screening
- **Regulatory \& registration** — PROSPERO systematic review protocol writer, INPLASY registration helper, IRB application assistant, IACUC protocol drafter, meta\-analysis protocol writer, protocol standardization for reproducible SOPs, research proposal generator from existing literature, competitive research proposal writer for NSF/NIH/DOE/DARPA

### 🧬 Omics \& Bioinformatics Analysis — 52 skills

From raw sequencing files to interpretable biological findings, these skills cover single\-cell RNA\-seq, bulk transcriptomics, multi\-omics integration, genomics, proteomics, and microbiome workflows — with outputs formatted for direct inclusion in manuscript figures and methods sections\.

- **Single\-cell RNA\-seq** — end\-to\-end Scanpy QC\-to\-clustering pipeline, AnnData data structure operations, scVI\-tools probabilistic batch integration, automated cell type annotation, spatial transcriptomics mapping for 10x Visium and Xenium, CELLxGENE portal data access
- **Bulk RNA\-seq \& differential expression** — PyDESeq2 differential expression analysis, volcano plot and clustered heatmap gene screening, differential expression with limma/DESeq2/edgeR support, sequencing batch effect correction, gene and protein expression matrix normalization
- **Pathway \& network analysis** — GO and KEGG enrichment analysis with visualization, GSEA gene set enrichment, GSVA pathway scoring with limma differential analysis, immune pathway GSVA/ssGSEA, WGCNA co\-expression network, ceRNA regulatory network, database\-driven lncRNA\-mRNA regulatory network, TF–target gene regulatory network, STRING\-based PPI network, gene–pathway Sankey diagram
- **Immune infiltration** — CIBERSORT\-style immune cell deconvolution for 22 immune cell types, ssGSEA immune infiltration scoring, ESTIMATE immune and stromal scoring
- **Genomics \& sequence analysis** — Biopython toolkit for alignment, phylogenetics, structure, and sequence I/O, NCBI BLAST sequence alignment, SAM/BAM/CRAM/VCF file handling, CRISPR screen analysis for essential gene identification, FASTQC report interpretation with actionable recommendations, Circos plot generation for circular genomics visualization, sequence motif logo generation, deepTools for BAM\-to\-bigWig, QC, and heatmaps, machine learning toolkit for genomic interval data, high\-performance genomic interval analysis
- **Dimensionality reduction \& clustering** — PCA, UMAP and t\-SNE, hierarchical clustering dendrogram, consensus clustering molecular subtyping, KNN missing data imputation
- **Microbiome \& other modalities** — scikit\-bio for diversity and ordination metrics, FlowIO FCS file parsing, pyOpenMS computational mass spectrometry, Neuropixels electrophysiology analysis including Kilosort4 spike sorting, gene regulatory network inference

### 📊 Clinical Research \& Meta\-Analysis — 61 skills

Clinical and translational research demands statistical rigor across every phase — from systematic review registration and literature screening through survival modeling, diagnostic accuracy evaluation, and clinical prediction model validation\. This category covers the complete meta\-analysis workflow with 15\+ figure types, plus the full range of clinical statistical methods used in SCI\-indexed medical journals\.

- **Meta\-analysis pipeline** — PICOS and PIECS generator, eligibility criteria generator, PubMed\-powered search title generator, abstract screener, full\-text screener, meta\-analysis feasibility assessor, forest plots for binary outcomes, continuous outcomes, and survival data, funnel plot with Egger and Begg publication bias testing, Baujat plot for heterogeneity and outlier identification, radial/Galbraith plot, ROB2 traffic light and summary bar plots, leave\-one\-out sensitivity plot, baseline characteristics section writer, methods section generator, results section analyzers, manuscript drafting assistant with automatic PubMed reference retrieval
- **Survival \& time\-to\-event analysis** — Kaplan–Meier survival curves from tabular data, time\-dependent ROC analysis, univariate and multivariable Cox regression, scikit\-survival Python pipeline for censored outcomes
- **Diagnostic \& predictive modeling** — ROC diagnostic performance analysis, nomogram construction, model calibration curve analysis, decision curve analysis for clinical net benefit, external model validation, LASSO logistic regression with cross\-validation, elastic net feature selection, machine learning modeling with feature importance for random forest, SVM, decision tree, XGBoost, and LightGBM
- **Risk of bias \& critical appraisal** — ROB2 for RCTs, NOS for cohort studies, NOS for case\-control studies, QUADAS\-2 for diagnostic accuracy, QUADAS\-C for comparative diagnostic accuracy, PROBAST for prediction models, QUAPAS for prognosis studies, automated study design scale selector, general quality assessment and critical appraisal
- **Data preparation** — clinical data cleaner for FDA/EMA\-ready datasets, baseline characteristics extraction from trial publications, outcome data extraction for meta\-analysis, Table 1 generator for baseline characteristics, statistical analysis with test selection and APA\-style reporting, statistical analysis advisor for test selection, experimental data analysis, EBM diagnostic test calculator

### 💊 Drug Discovery \& Cheminformatics — 26 skills

Computational workflows for medicinal chemistry, molecular biology, and translational pharmacology research — from virtual screening and molecular docking through network pharmacology and systems toxicology\.

- **Molecular screening \& property prediction** — Lipinski Rule of Five filtering for oral bioavailability, medicinal chemistry screening filters including PAINS and structural alerts, chemical structure interconversion between IUPAC, SMILES, and molecular formula, RDKit\-based molecular processing and standardization
- **Molecular docking \& structure** — DiffDock diffusion\-based blind docking with confidence scoring, photorealistic rendering scripts for PyMOL and UCSF ChimeraX, cloud\-based quantum chemistry and protein\-ligand docking via Rowan, ESM protein language models for sequence\-to\-function analysis
- **Systems pharmacology \& toxicology** — network toxicology and molecular docking planner, pathway\-anchored network pharmacology planner, hub\-first network pharmacology planner, 3D animation scripts and lay explanations for drug mechanisms, comprehensive academic introductions for biological pathways, phenotype introduction generator, metabolic network modeling with COBRApy
- **Spectral \& chemical data** — MS/MS spectra processing and library matching, computational mass spectrometry for proteomics and metabolomics, GNN framework for drug discovery and protein modeling
- **Drug \& chemical databases** — ChEMBL, DrugBank, PubChem, ZINC 230M\+ compounds, HMDB, Therapeutics Data Commons

### ✍️ Manuscript Writing \& Publication — 66 skills

Structured writing assistance for every stage of a medical manuscript — from first draft through peer review response and resubmission\. These skills support researchers in organizing their findings, meeting reporting standards, and preparing submission\-ready documents\. All outputs require researcher review and judgment before use\.

- **Manuscript sections** — introduction logic builder and section writer, methods section writing assistant for CONSORT/STROBE/PRISMA compliance, results section structurer and writer, discussion composer, title and abstract optimizer for information density and submission fit, abstract summarizer to 250\-word structured format, abstract trimmer for word limits, SCI\-style bilingual abstract refiner
- **Figures \& tables** — publication\-grade figure legend writer, table narrative writer, graphical abstract generator, graph and chart interpretation for publications, visual content description for accessibility
- **Submission readiness** — target journal matcher by topic, design, and evidence strength, reporting guideline compliance checker for CONSORT, STROBE, PRISMA, TRIPOD, STARD, and CARE, reference integrity checker, claim strength calibrator to prevent overstating findings, consistency checker across title, abstract, methods, results, and figures, LaTeX manuscript format converter for target journal templates, arXiv submission preflight checker, submission\-ready Elsevier/SCI highlights generator, authorship credit assignment following ICMJE and CRediT taxonomy
- **Peer review preparation** — structured peer review self\-evaluation tool, paper sprint review for revise\-and\-resubmit preparation, reviewer comment response drafter, author response builder for point\-by\-point responses, revision strategy planner for major/minor revisions, response letter with change\-location mapping, response tone polisher, blind review sanitizer for double\-blind submission
- **Grants \& funding** — NIH Specific Aims drafting assistant, NIH Biosketch builder compliant with 2022 OMB format, NIH study section preparation tool for grant applicants
- **Dissemination** — conference abstract writer, poster storyline builder, lay summary writer for general audiences, university press release writer, lab meeting slide deck builder, paper knowledge network and web presentation generator, medical English precision editor

### 🏥 Research Documentation \& Medical Education

Built for clinical researchers and educators who need structured research\-context documentation, data privacy tools, and medical education content\.

- **Research documentation** — EHR semantic compressor for summarizing clinical records in research contexts, referral letter generator for research coordination, clinical report writer for case reports, diagnostic studies, and trial documentation
- **Medical education** — anatomy quiz generator, USMLE Step 1 and Step 2 clinical case generator, radiology image quiz creator, OSCE\-style virtual standardized patient for history\-taking practice, genetics mentor covering Mendelian laws and inheritance
- **Data privacy** — HIPAA and PHI de\-identification checker for research datasets, DICOM image anonymizer with audit logging, runtime PHI prompt guardrail
- **Clinical calculation** — BMI and BSA calculator with multiple formulas and pediatric support, medical unit converter for glucose, cholesterol, creatinine, and hemoglobin, EBM diagnostic test calculator for sensitivity, specificity, PPV, NPV, and likelihood ratios, medical date and gestational age calculator

### ⚙️ Research Workflow \& Lab Management — 77 skills

The operational layer of a medical research lab — from reagent tracking and figure production to reproducibility auditing, document generation, and research administration\.

- **Reproducibility \& QC** — research code refactoring for publication\-ready reproducibility, methods completeness checker for replication readiness, result and figure consistency checker across manuscript sections, protocol deviation classifier for clinical trials, academic norm reviewer for citation and abbreviation standards, content proofreader for Chinese and English manuscripts
- **Lab operations** — reagent expiry scanner and multi\-level alert system, lab inventory depletion predictor with purchase alerts, experiment preparation and lab calculation generator, buffer and dilution calculator for PBS, RIPA, and TAE, CO₂ tank depletion monitor for cell culture facilities, cold chain transport risk calculator, chemical hazard storage sorter for OSHA/NFPA compliance, chemical waste disposal guide, equipment calibration and maintenance log, SDS/MSDS hazard code extractor
- **Scientific visualization** — heatmap beautifier with clustering trees and annotation tracks, volcano plot script generator for R and Python, UpSet plot converter for 4\+ set comparisons, multi\-panel figure assembler for A–F composites at publication DPI, microscopy scale bar adder, mechanism flowchart generator in Mermaid, scientific schematic generator for journal and poster visuals, scientific SVG generator from natural\-language descriptions, Western blot band quantifier with densitometry, Seaborn statistical visualization, Matplotlib figure scripting, Plotly interactive charts
- **Computational pathology \& imaging** — HistoLab WSI tiling and preprocessing for digital pathology, PathML advanced WSI analysis with multiplexed immunofluorescence support, pyDICOM for reading, writing, and anonymizing DICOM files, DNAnexus cloud genomics platform integration, Benchling R\&D registry integration, Adaptyvbio automated protein testing and validation, LaminDB biological data versioning and FAIR compliance, image batch processor and converter, image OCR with Tesseract, DPI checker for journal submission standards
- **Document production** — PDF processor for merge, split, extract, and annotation, PDF to PowerPoint literature report converter, PowerPoint deck builder and editor, Word document generator and editor, Markdown file converter, HTML\-to\-PDF renderer, spreadsheet operations for CSV and Excel, academic research poster generator from PDF literature, poster designer with image generation
- **Research administration** — academic CV generator with bilingual output to Word, journal recommender by topic, abstract, and impact factor, citation style converter for RIS, BibTeX, and CSL\-JSON, manuscript formatting checker for journal templates, chart style unifier across Word tables and figures, literature management with offline deduplication and tagging, bibliography organizer by theme, method, and conclusion, meeting minutes generator from transcripts, meeting assistant for decisions and action items, schedule management with conflict detection, task reminder with exportable MD/CSV outputs, resubmission deadline tracker with phase\-appropriate task breakdown, mind map generator, postdoc fellowship matcher by nationality, years since PhD, and field, conflict of interest checker for peer review assignments

## 🚀 How to Start?

Use this library with **Claude Code**, **Codex**, or another agent platform that supports `SKILL.md` skills.

1. Browse the [`scientific-skills`](./scientific-skills) and [`awesome-med-research-skills`](./awesome-med-research-skills) directories to choose a skill.
2. Download the selected skill folder, or clone this repository with Git:

   ```bash
   git clone https://github.com/aipoch/medical-research-skills.git
   ```

3. Follow your agent platform's skill installation instructions to add the complete skill folder, including its `SKILL.md` and supporting files.
4. Review the skill's requirements, configure any dependencies or credentials it needs, and follow your platform's instructions to enable and use it.

## What is Awesome Med Research Skills?

**Awesome ​Med Research Skills** is a curated collection of medical research Agent Skills, currently including **140 high-quality skills**.

We aim to help researchers more effectively organize questions, connect evidence, and advance research. To achieve this, we encode professional medical research logic into these agent skills:

- **Literature ​authenticity constraints**​: Implementing hard rules
- ​**Research type identification**​: We first determine the study type, then execute different logical pathways
- **Medical-specific prompt logic**

### Key Features of Awesome Med Research Skills

#### Modular Skill Architecture for Team Scaling

- Skills are **composable, replaceable, and extensible**, suitable for both individual use and team collaboration
- Can be assembled from single-task execution to multi-step workflow pipelines

#### Built for Real Medical Research Scenarios

- Covers real workflows: **topic selection, literature search, study design, writing, graphical abstracts**, and more
- Not adapted from generic content templates — designed specifically for **medical research contexts**.

### Represent Selected Skills

The examples below represent selected skills from each category.

#### Academic Writing

- [arXiv Preflight](https://github.com/aipoch/medical-research-skills/tree/main/awesome-med-research-skills/Academic%20Writing/arxiv-preflight)
- [Target Journal Matcher](https://github.com/aipoch/medical-research-skills/tree/main/awesome-med-research-skills/Academic%20Writing/target-journal-matcher)
- [Reporting Guideline Compliance Checker](https://github.com/aipoch/medical-research-skills/tree/main/awesome-med-research-skills/Academic%20Writing/reporting-guideline-compliance-checker)
- [Medical English Precision Editor](https://github.com/aipoch/medical-research-skills/tree/main/awesome-med-research-skills/Academic%20Writing/medical-english-precision-editor)

#### Evidence Insights

##### Literature Discovery

- [Biomedical Search Strategy Builder](https://github.com/aipoch/medical-research-skills/tree/main/awesome-med-research-skills/Evidence%20Insight/biomedical-search-strategy-builder)
- [Multi-Database Literature Collector](https://github.com/aipoch/medical-research-skills/tree/main/awesome-med-research-skills/Evidence%20Insight/multi-database-literature-collector)
- [High-Value Paper Screener](https://github.com/aipoch/medical-research-skills/tree/main/awesome-med-research-skills/Evidence%20Insight/high-value-paper-screener)
- [Preprint Surveillance Finder](https://github.com/aipoch/medical-research-skills/tree/main/awesome-med-research-skills/Evidence%20Insight/preprint-surveillance-finder)

##### Evidence Mapping & Topic Exploration

- [Biomarker Landscape Scanner](https://github.com/aipoch/medical-research-skills/tree/main/awesome-med-research-skills/Evidence%20Insight/biomarker-landscape-scanner)
- [Topic Evidence Mapper](https://github.com/aipoch/medical-research-skills/tree/main/awesome-med-research-skills/Evidence%20Insight/topic-evidence-mapper)
- [Disease Mechanism Evidence Map](https://github.com/aipoch/medical-research-skills/tree/main/awesome-med-research-skills/Evidence%20Insight/disease-mechanism-evidence-map)
- [Drug-Target Evidence Landscape](https://github.com/aipoch/medical-research-skills/tree/main/awesome-med-research-skills/Evidence%20Insight/drug-target-evidence-landscape)

##### Scientific Reading & Interpretation

- [Study Design Identifier](https://github.com/aipoch/medical-research-skills/tree/main/awesome-med-research-skills/Evidence%20Insight/study-design-identifier)
- [Result Reliability Checker](https://github.com/aipoch/medical-research-skills/tree/main/awesome-med-research-skills/Evidence%20Insight/result-reliability-checker)
- [Figure-First Paper Reader](https://github.com/aipoch/medical-research-skills/tree/main/awesome-med-research-skills/Evidence%20Insight/figure-first-paper-reader)
- [Contradictory Findings Resolver](https://github.com/aipoch/medical-research-skills/tree/main/awesome-med-research-skills/Evidence%20Insight/contradictory-findings-resolver)
- [Paper-to-Claim Verifier](https://github.com/aipoch/medical-research-skills/tree/main/awesome-med-research-skills/Evidence%20Insight/paper-to-claim-verifier)

##### Research Gap Discovery

- [Medical Research Gap Finder](https://github.com/aipoch/medical-research-skills/tree/main/awesome-med-research-skills/Evidence%20Insight/medical-research-gap-finder)
- [Unmet Clinical Need Extractor](https://github.com/aipoch/medical-research-skills/tree/main/awesome-med-research-skills/Evidence%20Insight/unmet-clinical-need-extractor)
- [Population Gap Detector](https://github.com/aipoch/medical-research-skills/tree/main/awesome-med-research-skills/Evidence%20Insight/population-gap-detector)
- [Method Gap Detector](https://github.com/aipoch/medical-research-skills/tree/main/awesome-med-research-skills/Evidence%20Insight/method-gap-detector)

#### Protocol Design

##### Clinical & Translational Study Design

- [Aim and Hypothesis Designer](https://github.com/aipoch/medical-research-skills/tree/main/awesome-med-research-skills/Protocol%20Design/aim-and-hypothesis-designer)
- [Translational Study Blueprint](https://github.com/aipoch/medical-research-skills/tree/main/awesome-med-research-skills/Protocol%20Design/translational-study-blueprint)
- [Validation Strategy Designer](https://github.com/aipoch/medical-research-skills/tree/main/awesome-med-research-skills/Protocol%20Design/validation-strategy-designer)
- [Clinical Cohort Protocol Designer](https://github.com/aipoch/medical-research-skills/tree/main/awesome-med-research-skills/Protocol%20Design/clinical-cohort-protocol-designer)
- [Real-World Evidence Study Designer](https://github.com/aipoch/medical-research-skills/tree/main/awesome-med-research-skills/Protocol%20Design/real-world-evidence-study-designer)

##### Biomarker, Omics & Genetics Planning

- [Prognostic Biomarker Protocol Designer](https://github.com/aipoch/medical-research-skills/tree/main/awesome-med-research-skills/Protocol%20Design/prognostic-biomarker-protocol-designer)
- [Single Cell Research Planner](https://github.com/aipoch/medical-research-skills/tree/main/awesome-med-research-skills/Protocol%20Design/single-cell-research-planner)
- [Bulk Omics Integrative Planner](https://github.com/aipoch/medical-research-skills/tree/main/awesome-med-research-skills/Protocol%20Design/bulk-omics-integrative-planner)
- [Multi-Omics Clinical Integration Planner](https://github.com/aipoch/medical-research-skills/tree/main/awesome-med-research-skills/Protocol%20Design/multi-omics-clinical-integration-planner)

##### Research Execution Planning

- [Inclusion-Exclusion Criteria Builder](https://github.com/aipoch/medical-research-skills/tree/main/awesome-med-research-skills/Protocol%20Design/inclusion-exclusion-criteria-builder)
- [Endpoint Definition Designer](https://github.com/aipoch/medical-research-skills/tree/main/awesome-med-research-skills/Protocol%20Design/endpoint-definition-designer)
- [Sample Size and Power Planning Assistant](https://github.com/aipoch/medical-research-skills/tree/main/awesome-med-research-skills/Protocol%20Design/sample-size-and-power-planning-assistant)
- [Feasibility-Aware Study Planner](https://github.com/aipoch/medical-research-skills/tree/main/awesome-med-research-skills/Protocol%20Design/feasibility-aware-study-planner)

#### Data Analysis

##### Differential Expression & Data Processing

- [Differential Expression Analysis](https://github.com/aipoch/medical-research-skills/tree/main/awesome-med-research-skills/Data%20Analysis/differential-expression-analysis)
- [Batch Effect Correction](https://github.com/aipoch/medical-research-skills/tree/main/awesome-med-research-skills/Data%20Analysis/batch-effect-correction)
- [Gene-Protein Expression Matrix Normalization](https://github.com/aipoch/medical-research-skills/tree/main/awesome-med-research-skills/Data%20Analysis/gene-protein-expression-matrix-normalization)

##### Machine Learning & Feature Selection

- [LightGBM-analysis](https://github.com/aipoch/medical-research-skills/tree/main/awesome-med-research-skills/Data%20Analysis/LightGBM-analysis)
- [XGBoost-analysis](https://github.com/aipoch/medical-research-skills/tree/main/awesome-med-research-skills/Data%20Analysis/XGBoost-analysis)
- [rf-model-importance-analysis](https://github.com/aipoch/medical-research-skills/tree/main/awesome-med-research-skills/Data%20Analysis/rf-model-importance-analysis)
- [decision-tree-analysis](https://github.com/aipoch/medical-research-skills/tree/main/awesome-med-research-skills/Data%20Analysis/decision-tree-analysis)
- [svm-model-importance-analysis](https://github.com/aipoch/medical-research-skills/tree/main/awesome-med-research-skills/Data%20Analysis/svm-model-importance-analysis)
- [Elastic Net Feature Selection](https://github.com/aipoch/medical-research-skills/tree/main/awesome-med-research-skills/Data%20Analysis/elastic-net-feature-selection)
- [LASSO Logistic Regression Analysis](https://github.com/aipoch/medical-research-skills/tree/main/awesome-med-research-skills/Data%20Analysis/lasso-logistics-analysis)

##### Clustering & Dimensionality Reduction

- [Consensus Clustering Analysis](https://github.com/aipoch/medical-research-skills/tree/main/awesome-med-research-skills/Data%20Analysis/consensus-clustering-analysis)
- [PCA Dimensionality Reduction](https://github.com/aipoch/medical-research-skills/tree/main/awesome-med-research-skills/Data%20Analysis/pca-dimensionality-reduction)
- [UMAP and t-SNE Analysis](https://github.com/aipoch/medical-research-skills/tree/main/awesome-med-research-skills/Data%20Analysis/umap-tsne-analysis)

##### Functional Enrichment & Pathway Analysis

- [GO/KEGG Enrichment Analysis and Visualization](https://github.com/aipoch/medical-research-skills/tree/main/awesome-med-research-skills/Data%20Analysis/gokegg)
- [GSEA Analysis and Visualization](https://github.com/aipoch/medical-research-skills/tree/main/awesome-med-research-skills/Data%20Analysis/gsea)
- [GSVA Analysis and Visualization](https://github.com/aipoch/medical-research-skills/tree/main/awesome-med-research-skills/Data%20Analysis/gsva-analysis-and-visualization)

##### Immune Infiltration Analysis

- [CIBERSORT Immune Infiltration Analysis](https://github.com/aipoch/medical-research-skills/tree/main/awesome-med-research-skills/Data%20Analysis/cibersort-immune-infiltration-analysis)
- [ESTIMATE Immune Score Analysis](https://github.com/aipoch/medical-research-skills/tree/main/awesome-med-research-skills/Data%20Analysis/estimate-immune-score-analysis)
- [ssGSEA Immune Infiltration Analysis](https://github.com/aipoch/medical-research-skills/tree/main/awesome-med-research-skills/Data%20Analysis/ssgsea-immune-infiltration-analysis)
- [Immune Pathway Analysis](https://github.com/aipoch/medical-research-skills/tree/main/awesome-med-research-skills/Data%20Analysis/immune-pathway-analysis)

##### Network Biology & Regulatory Analysis

- [WGCNA Analysis](https://github.com/aipoch/medical-research-skills/tree/main/awesome-med-research-skills/Data%20Analysis/wgcna-analysis)
- [PPI Network Analysis](https://github.com/aipoch/medical-research-skills/tree/main/awesome-med-research-skills/Data%20Analysis/ppi-network-analysis)
- [TF-Target Gene Regulatory Network Analysis](https://github.com/aipoch/medical-research-skills/tree/main/awesome-med-research-skills/Data%20Analysis/tf-target-gene-regulatory-network)
- [ceRNA Analysis](https://github.com/aipoch/medical-research-skills/tree/main/awesome-med-research-skills/Data%20Analysis/cerna-analysis)

##### Survival & Statistical Modeling

- [Kaplan-Meier Survival Curve Analysis](https://github.com/aipoch/medical-research-skills/tree/main/awesome-med-research-skills/Data%20Analysis/km-survival-curve)
- [Univariate and Multivariable Cox Regression Analysis](https://github.com/aipoch/medical-research-skills/tree/main/awesome-med-research-skills/Data%20Analysis/univariate-multivariable-cox-regression)
- [ROC Diagnostic Performance Analysis](https://github.com/aipoch/medical-research-skills/tree/main/awesome-med-research-skills/Data%20Analysis/roc-diagnostic-performance)
- [Nomogram Construction](https://github.com/aipoch/medical-research-skills/tree/main/awesome-med-research-skills/Data%20Analysis/nomogram-construction)

## Star History

<a href="https://www.star-history.com/?repos=aipoch%2Fmedical-research-skills&type=date&legend=top-left">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=aipoch/medical-research-skills&type=date&theme=dark&legend=top-left&sealed_token=KD3FdQQ_-RyhAT_jv034hc_lK-Vi0rDl4hcJbGBzdlRzh1WwOQAruUm0NjwY-UBJ0L100W6lkf1SOudZl64-8qB4KRCFHo9MFPm_q-58HrvXF4PMzxpF_jO6_aJwWeyu8GzqOABML6pXrPJnyL3IVlsTArYvdk9u94u9U5mMER0w8tsWQ33mVdNeywvT" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=aipoch/medical-research-skills&type=date&legend=top-left&sealed_token=KD3FdQQ_-RyhAT_jv034hc_lK-Vi0rDl4hcJbGBzdlRzh1WwOQAruUm0NjwY-UBJ0L100W6lkf1SOudZl64-8qB4KRCFHo9MFPm_q-58HrvXF4PMzxpF_jO6_aJwWeyu8GzqOABML6pXrPJnyL3IVlsTArYvdk9u94u9U5mMER0w8tsWQ33mVdNeywvT" />
   <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=aipoch/medical-research-skills&type=date&legend=top-left&sealed_token=KD3FdQQ_-RyhAT_jv034hc_lK-Vi0rDl4hcJbGBzdlRzh1WwOQAruUm0NjwY-UBJ0L100W6lkf1SOudZl64-8qB4KRCFHo9MFPm_q-58HrvXF4PMzxpF_jO6_aJwWeyu8GzqOABML6pXrPJnyL3IVlsTArYvdk9u94u9U5mMER0w8tsWQ33mVdNeywvT" />
 </picture>
</a>

# Analysis Module Library
# mr-scrna-research-planner

---

## Single-Cell Core Modules

| Module | Purpose | When Required |
|---|---|---|
| QC filtering | Remove low-quality cells and doublets (DoubletFinder, scrublet) | Always |
| Normalization | Library-size correction, log transformation | Always |
| PCA / UMAP / clustering | Dimensionality reduction and visualization | Always |
| Cell type annotation | Label clusters via markers or reference (SingleR) | Always |
| Cell composition comparison | Disease vs control abundance shifts | Standard+ |
| Module scoring | Score cells for mechanism gene-set activity | Pattern A |
| High vs low score subgrouping | Create comparison groups for DEG | Pattern A |
| DEG analysis | Differentially expressed genes between conditions or groups | Always |
| Pseudobulk validation | Aggregate per-sample counts for statistically robust DEG | Advanced+ |
| GSVA / ssGSEA | Pathway activity scoring per cell cluster | Standard+ |
| Pseudotime / trajectory | Cell-state transition modeling along a biological axis | Standard+ |
| Cell-cell communication | Ligand-receptor interaction inference between cell types | Advanced+ |
| TF / regulon network | Transcription factor activity inference (SCENIC/pySCENIC) | Advanced+ |
| Cell-state transition analysis | Branch comparison at trajectory decision points | Advanced+ |

### Module Scoring Method Comparison

| Method | Approach | Best When |
|---|---|---|
| AUCell | Rank-based enrichment per cell | Robust to library-size variation; preferred for heterogeneous datasets |
| UCell | Rank-based, integrated in Seurat/Scanpy | Easier to implement; similar robustness to AUCell |
| AddModuleScore | Mean expression minus control background | Simple; fast; less robust in sparse data — avoid with small gene sets |

---

## MR Core Modules

| Module | Purpose | When Required |
|---|---|---|
| Instrument extraction | Select independent genome-wide significant SNPs (p < 5×10⁻⁸, r² < 0.001) | Always |
| Clumping & LD pruning | Remove correlated instruments (PLINK or TwoSampleMR) | Always |
| Univariable MR | Test causal effect of single exposure → outcome | Always |
| Multivariable MR | Control for correlated exposures (MVMR package) | Standard+ |
| Sensitivity analysis | Heterogeneity (Cochran's Q), pleiotropy (MR-Egger intercept), leave-one-out | Standard+ |
| Steiger directionality | Confirm causal direction; filter instruments explaining more variance in outcome | Standard+ |
| Colocalization | Test whether same causal variant drives both eQTL and GWAS signals (coloc) | Advanced+ |
| SMR + HEIDI | Summary-based MR with pleiotropy test using HEIDI | Advanced+ |
| Bidirectional MR | Test reverse causality where biologically plausible | Publication+ |
| Stratified MR | By sex, age, disease subtype | Publication+ |

### MR Method Comparison

| Method | Assumption | Best When |
|---|---|---|
| IVW | No pleiotropy (all instruments valid) | Primary method; most powerful |
| Weighted Median | 50%+ instruments valid | Robustness check; common in sensitivity |
| MR-Egger | Directional pleiotropy allowed (InSIDE assumption) | Pleiotropy test; low power if few instruments |
| Weighted Mode | Most instruments share true causal effect | Supplementary check |

---

## External Validation Modules

| Module | Purpose | When Recommended |
|---|---|---|
| Bulk transcriptomic validation | Independent GEO / TCGA dataset for causal gene expression | Standard+ |
| Tissue-level expression validation | GTEx or HPA expression confirmation | Standard+ |
| Disease subgroup validation | Subtype, severity, or stage stratification | Advanced+ |
| Independent cohort replication | Second independent scRNA or GWAS population | Publication+ |
| Clinical prediction model | ROC curve, nomogram, survival model | If translational angle requested |

---

## Mechanism Support Modules

| Module | Purpose | Config Level |
|---|---|---|
| Pathway enrichment (GSEA, GO, KEGG) | Functional annotation of DEGs and causal genes | Standard+ |
| Gene set scoring (AUCell, UCell) | Activity of curated biological programs per cell | Standard+ |
| Protein interaction networks (STRING, GeneMANIA) | Physical/functional interaction context | Standard+ |
| Cell communication (CellChat, NicheNet) | Ligand-receptor signaling inference between cell types | Advanced+ |
| TF-mRNA regulatory network (SCENIC) | Upstream transcription factor drivers of causal genes | Advanced+ |
| Integrated mechanistic model figure | Synthesize all evidence into one schematic | All configs |

# Modules and Methods Reference

Full module list and tool library. Read when building the step-by-step workflow in Step 4.

---

## Module Groups

### 1. Dataset & Preprocessing
- Dataset search and selection (GEO / ArrayExpress)
- Platform compatibility check (microarray vs RNA-seq)
- Probe annotation / gene symbol mapping
- Normalization (quantile, RMA, TMM, VST)
- Batch effect handling (sva / ComBat)
- Training / validation designation
- Phenotype grouping (case vs control, severity)
- Feature matrix standardization

### 2. Differential Expression & Screening
- DEG analysis (limma, DESeq2, edgeR)
- Overlap across datasets (Venn intersection)
- Mechanism gene-set intersection
- Volcano plot visualization
- Heatmap (top DEGs)
- Gene prioritization criteria (logFC, adj. p-value thresholds)

### 3. Enrichment & Mechanism
- GO enrichment (BP, MF, CC)
- KEGG pathway enrichment
- GSEA (hallmark or custom gene sets, MSigDB)
- Pathway scoring
- High-risk vs low-risk group GSEA
- Biological narrative synthesis

### 4. Machine Learning & Modeling
- Univariate logistic regression screening
- Random forest (variable importance)
- LASSO (glmnet, λ selection via 10-fold CV)
- Elastic net
- SVM / SVM-RFE
- XGBoost / gradient boosting
- Multivariate logistic regression
- Nomogram (rms package)
- Calibration curve (Hosmer-Lemeshow, calibration plot)
- Decision curve analysis (DCA)
- ROC + AUC (pROC)
- AUC comparison across models
- Model coefficient interpretation

### 5. Immune & Network
- ssGSEA (immune cell quantification, 28-cell panel or TIMER2)
- CIBERSORT / xCell (alternative infiltration methods)
- Immune infiltration comparison (disease vs control)
- Gene–immune cell correlation (Spearman)
- PPI network (STRING, GeneMANIA, NetworkAnalyst)
- mRNA–miRNA network (ENCORI / StarBase)
- mRNA–TF network (CHIPBase / hTFtarget)
- Functional similarity analysis (GOSemSim)
- Chromosomal localization (RCircos)

### 6. Validation
- External dataset validation (expression + model performance)
- ROC in validation cohort
- Calibration consistency check
- DCA in training cohort
- Expression-level validation (box plots, paired plots)
- qPCR follow-up suggestion
- Clinical sample follow-up suggestion

---

## Tool / Package Reference

### R — Expression & Enrichment
| Purpose | Package |
|---|---|
| GEO data access | GEOquery |
| Normalization + DEG | limma, DESeq2, edgeR |
| Batch correction | sva, ComBat |
| Enrichment | clusterProfiler, enrichplot |
| GSEA | fgsea, GSEA desktop, MSigDB |
| Visualization | ggplot2, pheatmap, ComplexHeatmap |

### R — Machine Learning & Modeling
| Purpose | Package |
|---|---|
| Random forest | randomForest, ranger |
| LASSO / elastic net | glmnet |
| SVM | e1071, caret |
| XGBoost | xgboost |
| Logistic regression | base R glm |
| Nomogram | rms |
| ROC | pROC |
| Calibration | CalibrationCurves, rms |
| DCA | ggDCA, rmda, dcurves |

### R — Immune & Network
| Purpose | Package / Tool |
|---|---|
| ssGSEA | GSVA (gsva function) |
| Immune deconvolution | CIBERSORT, xCell, TIMER2 |
| Correlation | cor.test (Spearman) |
| Functional similarity | GOSemSim |
| Chromosomal map | RCircos |
| Network visualization | Cytoscape, igraph |

### Databases
| Purpose | Resource |
|---|---|
| Gene sets | MSigDB, GeneCards, KEGG |
| miRNA targets | ENCORI / StarBase, miRTarBase |
| TF targets | CHIPBase, hTFtarget, JASPAR |
| PPI | STRING, GeneMANIA, NetworkAnalyst |
| Immune | TIMER2, ImmPort |

---

## Module Selection by Tier

| Module group | Lite | Standard | Advanced | Publication+ |
|---|---|---|---|---|
| Dataset & Preprocessing | 1 dataset | 2 datasets | 2–3 datasets | Multi-cohort |
| DEG & Screening | ✓ | ✓ | ✓ | ✓ + consensus |
| Enrichment | Optional | GO+KEGG+GSEA | Full | Full + subgroup GSEA |
| ML & Modeling | 1–2 methods | RF + LASSO + logistic | + SVM/XGBoost comparison | Ensemble / compare ≥3 |
| Validation | ROC only | ROC + calibration + DCA | + external cohort | ≥2 external cohorts |
| Immune & Network | — | ssGSEA | + PPI + correlation | Full network suite |
| Translational | — | Optional | Suggested | Required |

---

## Validation Strategy — Required Layer Separation

Every plan must explicitly separate these five layers and state what each proves and does not prove:

### 1. Feature-Discovery Robustness
- DEG consistency across datasets (if >1)
- Overlap stability: how many shared DEGs under alternate thresholds?
- Mechanism-gene restriction logic: state source and curation quality
- **Proves:** transcriptomic dysregulation in disease context
- **Does not prove:** causality; genes may reflect downstream effects

### 2. Model Robustness
- Cross-validation or repeated screening where possible
- RF + LASSO agreement (both methods nominate same genes = stronger)
- Coefficient stability across bootstrap samples
- Validation cohort performance (AUC, calibration)
- **Proves:** predictive signal reproducible in held-out data
- **Does not prove:** generalizability to clinical populations without prospective study

### 3. Clinical Utility Support
- ROC + AUC with 95% CI (pROC)
- Calibration curve (Hosmer-Lemeshow + calibration plot)
- DCA (net benefit vs treat-all / treat-none)
- Nomogram (if used): visual clinical decision aid
- **Proves:** diagnostic utility in studied cohort under specific threshold
- **Does not prove:** clinical translation; prospective validation required

### 4. Biological Support
- GO/KEGG enrichment consistency with known disease biology
- Immune cell infiltration differences (ssGSEA / CIBERSORT)
- Gene–immune correlation (Spearman)
- PPI / miRNA / TF network context
- **Proves:** pathway and immune associations in dataset
- **Does not prove:** mechanistic causality — all results are associational

### 5. Optional Strengthening
- Independent validation cohort (not used in training)
- qPCR or protein-level follow-up suggestion
- Alternate algorithm comparison for model robustness
- Different phenotype definition sensitivity check
- **Proves:** cross-cohort and cross-platform reproducibility
- **Does not prove:** clinical utility without prospective design

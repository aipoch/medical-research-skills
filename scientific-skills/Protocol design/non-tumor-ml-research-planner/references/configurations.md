# Workload Configuration Reference

Full specifications for the four tiers. Read when generating Step 3 of the research plan.

---

## Lite

**Goal:** Fast, minimal, public-data-only non-tumor ML design.  
**Target:** Quick project launch, preliminary manuscript skeleton.  
**Timeline:** 2–4 weeks

**Must include:**
- One training dataset (GEO)
- DEG analysis
- Optional mechanism-gene intersection
- One or two feature selection methods (RF or LASSO, not both required)
- One simple diagnostic model (logistic regression)
- ROC validation

**Avoid:**
- Multiple feature selection algorithms
- Extensive network modules
- Overcomplicated validation layers
- Multi-dataset consensus logic

**Expected figures:** 4–6  
**Strengths:** Fast, feasible, clearly bounded  
**Weaknesses:** Limited robustness, no external validation, low reviewer defense

---

## Standard *(default recommendation)*

**Goal:** Balanced, publication-oriented design.  
**Target:** Conventional bioinformatics paper in mid-tier journals.  
**Timeline:** 4–8 weeks

**Must include:**
- All Lite components
- Two-dataset design when available (training + validation)
- GO / KEGG / GSEA enrichment
- Combined feature selection: RF + LASSO
- Multivariate logistic or equivalent diagnostic model
- ROC + calibration + DCA
- Immune infiltration (ssGSEA) or equivalent pathway strengthening
- External validation set when feasible

**Reference benchmark:** DEGs + mechanism gene set, GO/KEGG, GSEA, RF, LASSO, multivariate logistic regression, ROC, calibration, DCA, ssGSEA immune infiltration, external validation cohort.

**Expected figures:** 8–12  
**Strengths:** Publication-ready, meets reviewer expectations for this paper type  
**Weaknesses:** May require some dataset search; calibration/DCA requires adequate sample size

---

## Advanced

**Goal:** Stronger paper with enhanced robustness and biological depth.  
**Target:** More competitive journals; reviewers likely to request extended validation.  
**Timeline:** 8–14 weeks

**Must include:**
- All Standard components
- More careful training/validation split logic (explicit rationale)
- Multiple model comparisons or stability analysis (e.g., RF vs LASSO vs SVM)
- External validation in an independent cohort
- Expanded immune / pathway / regulatory interpretation
- Network strengthening: PPI, TF, miRNA
- Alternative feature selection or model robustness checks
- Reviewer-risk pre-emption in manuscript framing

**Expected figures:** 12–18  
**Strengths:** Defensible against most reviewer challenges  
**Weaknesses:** Higher workload; requires additional datasets and bioinformatics tools

---

## Publication+

**Goal:** High-workload, publication-maximizing design.  
**Target:** Ambitious manuscripts, stronger translational claims.  
**Timeline:** 14+ weeks

**Must include:**
- All Advanced components
- Multi-cohort consensus logic (Venn / meta-analysis)
- Stricter phenotype engineering (subgroup, severity, treatment status)
- Multiple algorithm comparison or ensemble modeling
- Stronger external validation strategy (≥2 external cohorts if feasible)
- Manuscript-grade figure logic (consistent color palette, panel layout)
- Explicit reviewer-risk mitigation in every section
- Optional wet-lab follow-up suggestion (qPCR, protein validation)

**Expected figures:** 16–24+  
**Strengths:** Maximizes publication defensibility  
**Weaknesses:** Very high workload; wet-lab extensions require resources

---

## Article Pattern Coverage Matrix

Plans must address these patterns when relevant:

| Pattern | Requirement |
|---|---|
| DEG → ML feature selection → diagnostic model | Required |
| Mechanism gene set ∩ DEG → ML | Required when mechanism theme provided |
| Multi-dataset overlap → training/validation | Required when ≥2 datasets available |
| GO/KEGG/GSEA + ML | Required (Standard+) |
| RF + LASSO dual feature selection | Required (Standard+) |
| Logistic model + ROC | Required baseline |
| Calibration + DCA | Recommended (Standard+) |
| Immune infiltration + gene correlation | Recommended (Standard+) |
| Regulatory network (miRNA / TF) | Recommended (Advanced+) |
| External validation | Required whenever a second dataset exists |
| qPCR / wet-lab suggestion | Optional (Publication+ or translational) |

---

## Reviewer Risk Register (applies to all tiers)

Every plan must flag relevant risks from this list:

| Risk | Mitigation |
|---|---|
| Small validation set | Report 95% CI on AUC; note limitation explicitly |
| Platform heterogeneity | State normalization and batch strategy per dataset |
| Overfitting from chained feature selection | Report cross-validation; avoid > 2 sequential screens |
| Inflated AUC in small datasets | Add calibration + DCA; report confidence intervals; flag if n < 50 per group |
| No independent real-world validation | Acknowledge; suggest qPCR or future cohort |
| Biological overinterpretation of networks | Use hedged language; note associational nature |
| Missing clinical metadata | Note as limitation; frame as discovery study |
| High AUC (> 0.9) in small cohort | Do not emphasize without external replication; report CI width |
| Mechanism-gene set quality | State source and curation method for gene set |
| Phenotype grouping ambiguity | Define case/control criteria explicitly; note severity or treatment status if relevant |

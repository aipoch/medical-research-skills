# Workflow Step Template
# mr-scrna-research-planner

---

## 8-Field Step Template

Every step in the workflow output (Section D) must include all 8 fields. Do not omit any field. Do not replace detailed method descriptions with bare tool name lists.

```
Step Name:        Short descriptive label
Purpose:          What this step accomplishes in the overall pipeline
Input:            Exact data / files / outputs from prior steps needed
Method:           Specific tool(s) and algorithm(s) — explain WHY this choice
                  over the main alternative(s)
Key Parameters /
Decision Rules:   Thresholds, cutoffs, acceptance criteria — be specific
Expected Output:  File format + content description + what "success" looks like
Failure Points:   What could go wrong; how to detect it; what it looks like
Alternative
Approaches:       Backup tool/method if primary fails or data doesn't support it
```

---

## Standard Step Sequence (adapt to selected pattern and config)

### Single-Cell Block

1. **scRNA Dataset Selection and Download**
2. **QC Filtering** (doublet removal, cell viability thresholds)
3. **Normalization and Feature Selection** (highly variable genes)
4. **Dimensionality Reduction** (PCA → UMAP)
5. **Clustering** (Louvain/Leiden)
6. **Cell Type Annotation** (marker-based or SingleR)
7. **Cell Composition Analysis** (disease vs control, if applicable)
8. **Module Scoring** (Pattern A) or **Key-Cell DEG** (Pattern B)
9. **Comparison Group Definition** (high vs low score, or disease vs control)
10. **DEG Analysis** (FindMarkers or pseudobulk)
11. **GSVA / Pathway Scoring**
12. **Pseudotime / Trajectory Analysis**
13. *[Advanced+]* **Cell-Cell Communication** (CellChat/NicheNet)
14. *[Advanced+]* **Regulon / TF Network** (SCENIC/pySCENIC)

### MR Block

15. **GWAS Data Retrieval** (outcome + exposure if applicable)
16. **Instrument Extraction** (SNP selection, clumping/pruning)
17. **Univariable MR** (IVW primary + secondary methods)
18. *[Standard+]* **Multivariable MR** (MVMR)
19. *[Standard+]* **Sensitivity Analysis** (heterogeneity, pleiotropy, LOO, Steiger)
20. *[Advanced+]* **Colocalization** (coloc) or **SMR + HEIDI**
21. *[Publication+]* **Bidirectional MR** (reverse causality check)

### Integration and Validation Block

22. **Causal Gene scRNA Localization** (where do MR-prioritized genes express?)
23. *[Standard+]* **External Bulk Validation** (independent GEO/TCGA cohort)
24. *[Standard+]* **Tissue-Level Expression Check** (GTEx/HPA)
25. **Integrated Mechanistic Model** (summary figure synthesizing all evidence)

---

## Step Ordering Rules

- Single-cell block runs first (data-driven; informs candidate gene list)
- MR block runs on candidates derived from single-cell DEG or module analysis
- Integration block connects MR results back to single-cell resolution
- Pattern D (Exposure-Driven) reverses order: MR first, then scRNA to localize effect

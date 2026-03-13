# Study Patterns Reference

Five core non-tumor ML study patterns. Read this file when selecting the appropriate pattern in Step 2.

---

## A. DEG-to-Diagnostic Model Design

**Use when:** user wants to identify disease-associated genes and build a diagnostic model from the transcriptome, without a pre-defined mechanism restriction.

**Disease examples:** diabetic foot ulcer, osteoarthritis, chronic kidney disease, heart failure

**Logic:**
1. Collect one or more public disease datasets (GEO)
2. DEG analysis (limma / DESeq2)
3. Optionally intersect with a mechanism-related gene set
4. GO / KEGG / GSEA enrichment
5. Feature selection via ML (RF + LASSO or similar)
6. Construct diagnostic model (multivariate logistic / nomogram)
7. Validate: ROC → calibration → DCA → external dataset
8. Add immune or regulatory layer for biological depth

**Reference pattern:** two GEO datasets, DEGs intersected with pyroptosis-related genes, RF + LASSO → 6 key genes → multivariate logistic model → ROC + calibration + DCA + ssGSEA immune infiltration.

---

## B. Mechanism Gene-Set Restricted ML Design

**Use when:** user starts from a curated mechanism gene set and wants a biologically focused ML paper with mechanistic framing.

**Disease × mechanism examples:**
- pyroptosis × diabetic wound healing
- ferroptosis × diabetic nephropathy
- apoptosis × lupus nephritis
- mitophagy × atherosclerosis

**Logic:**
1. Define mechanism-related genes (literature / databases)
2. DEG analysis in disease datasets
3. Intersect DEGs with mechanism genes → candidate set
4. GO / KEGG / GSEA on candidate set
5. RF / LASSO / SVM → key genes
6. Diagnostic model construction
7. Strengthen with immune infiltration + regulatory networks

**Key constraint:** the biological narrative must stay anchored to the mechanism theme; do not drift into generic biomarker framing.

---

## C. Multi-Dataset Consensus + ML Design

**Use when:** user wants stronger reproducibility and robustness by drawing consensus from multiple independent cohorts.

**Use cases:** common biomarkers across multiple DKD cohorts, robust genes across autoimmune datasets, integrated wound-healing signatures.

**Logic:**
1. Identify ≥2 compatible GEO datasets for the same disease
2. Normalize / process separately
3. DEG analysis in each dataset
4. Take overlap / meta-signature (Venn or meta-analysis)
5. Feature selection on training set
6. Validate in held-out or external dataset
7. Optional: batch correction, stability analysis, consensus scoring

**Key constraint:** explicitly state dataset sources, batch handling strategy, and overlap criteria. Multi-dataset designs are more robust but require careful preprocessing documentation.

---

## D. Immune + ML Biomarker Design

**Use when:** immune infiltration context is central to the biological story, not just an add-on.

**Use cases:** immune-related diagnostic genes in DKD, inflammatory markers in chronic wounds, immune infiltration + biomarker in autoimmune disease.

**Logic:**
1. Identify candidate genes (DEG or mechanism-restricted)
2. Quantify immune infiltration (ssGSEA / CIBERSORT / TIMER)
3. Correlate candidate genes with immune cell subtypes
4. Feature selection with ML to identify immune-correlated key genes
5. Build diagnostic model
6. Interpret biomarker–immune axis as the core story

**Key constraint:** the immune correlation must be biologically meaningful, not just a correlation heatmap. Justify why immune context matters for the disease.

---

## E. Translational Biomarker + Network Strengthening Design

**Use when:** user wants a more complete publication story with regulatory network interpretation and explicit translational value.

**Use cases:** clinically useful diagnostic genes in diabetic wound healing, regulatory biomarkers for diabetic complications, multi-layer biomarker story in non-tumor chronic disease.

**Logic:**
1. Identify key genes (from any upstream pattern)
2. Build and validate diagnostic model (ROC + calibration + DCA)
3. Add network layers: PPI, mRNA–miRNA, mRNA–TF
4. Add functional similarity analysis and/or chromosomal localization
5. Optionally include immune interpretation
6. Suggest downstream qPCR or clinical validation

**Key constraint:** network results provide biological context, not mechanistic proof. Do not overstate regulatory conclusions from bioinformatics networks alone.

---

## Pattern Combinations

Patterns can be combined in a single study. Common pairings:

| Base | Add-on | Result |
|---|---|---|
| A (DEG-to-Diagnostic) | B (Mechanism restriction) | More focused, biologically anchored |
| A or B | D (Immune) | Immune context adds depth and novelty |
| C (Multi-dataset) | A or B | Stronger reproducibility claim |
| Any | E (Network) | Publication-grade strengthening |

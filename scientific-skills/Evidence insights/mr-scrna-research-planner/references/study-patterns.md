# Study Patterns — Detailed Logic
# mr-scrna-research-planner

---

## Pattern A — Mechanism Gene-Set Driven

**Use when:** User starts from a biological mechanism or curated gene set.

**Canonical examples:** ferroptosis + colorectal cancer, pyroptosis + diabetic nephropathy,
necroptosis + osteoarthritis, senescence + pulmonary fibrosis

**Logic chain:**
1. Collect mechanism genes (MSigDB, literature, curated databases: FerrDb, PYROPTOSIS database, etc.)
2. scRNA-seq QC, normalization, dimensionality reduction, cell annotation
3. Score cells using module scoring (AUCell / UCell / AddModuleScore)
4. Define high-score vs low-score comparison groups
5. Identify DEGs between groups
6. Use DEG-derived candidates as MR exposures (eQTL or pQTL instruments)
7. Localize MR-prioritized causal genes back to specific cell types
8. Strengthen with pathway enrichment, pseudotime, cell communication, regulon analysis

**Key design decision:** Module scoring method choice matters — AUCell/UCell are
rank-based and more robust to library size variation than AddModuleScore.

---

## Pattern B — Key-Cell Driven

**Use when:** User wants to identify which cell type drives disease or mechanism.

**Canonical examples:** Which immune cell drives disease progression? Which stromal cell
carries the mechanism signal? Which cell type harbors the causal biomarker?

**Logic chain:**
1. Cell annotation (marker-based or SingleR reference-based)
2. Compare cell composition across disease vs control (scCODA, propeller, or simple proportion test)
3. Prioritize key cell populations (differential abundance, enrichment scores)
4. Within key cells: module scoring or pseudobulk DEG
5. MR on candidate genes derived from key-cell DEGs
6. Pseudotime, cell-state analysis, and communication analysis to support causal cell story

**Key design decision:** Cell abundance analysis requires matching case/control samples —
verify the scRNA dataset has balanced disease/control design before committing to this pattern.

---

## Pattern C — Candidate-Gene Reverse Validation

**Use when:** User already has candidate genes and needs causal + cellular validation.

**Canonical examples:** "I have a list of biomarkers — build MR + scRNA validation."
"Validate whether these genes are causal and which cells express them."

**Logic chain:**
1. Input candidate gene list (from prior GWAS, literature, or user-provided)
2. eQTL/pQTL-based MR for each candidate (IVW primary + sensitivity)
3. Identify causally supported subset (p < 0.05 IVW; consistent direction across methods)
4. Return to scRNA data for expression localization of supported candidates
5. Pathway, trajectory, and communication analysis to strengthen mechanistic narrative

**Key design decision:** If few candidates survive MR filtering, consider whether the
original candidate list was derived from an independent population — reuse bias risk.

---

## Pattern D — Exposure–Disease–Cell Triangulation

**Use when:** User starts from a risk factor, exposure, or upstream trait.

**Canonical examples:** Obesity → disease through specific cell states; inflammation-related
exposure driving disease through causal genes; metabolite or immune trait influencing
disease and cell programs.

**Logic chain:**
1. Define exposure GWAS (BMI, inflammatory trait, metabolite) and outcome GWAS
2. Univariable MR: exposure → disease (confirm causal effect exists)
3. Multivariable MR: control for correlated traits (e.g., BMI + waist circumference)
4. Connect MR result to relevant genes or pathways (mediation analysis or colocalization)
5. Use scRNA-seq to locate effects in cell types or cell states (pathway activity by cell)
6. Pseudotime, communication, and pathway activity analysis to build mechanistic model

**Key design decision:** Requires a plausible biological link between the exposure and
the disease's cell-level mechanism — state this link as an explicit assumption.

---

## Pattern E — Translational Biomarker

**Use when:** User wants clinically meaningful biomarkers or druggable targets.

**Canonical examples:** Find causal diagnostic biomarkers; identify druggable targets with
cell-type localization; build a publication-ready biomarker pipeline.

**Logic chain:**
1. Identify causal biomarkers via MR (protein pQTL or gene expression eQTL instruments)
2. Localize in scRNA data by cell type and expression level
3. Validate in independent bulk datasets (GEO, TCGA)
4. Optional: ROC analysis, clinical prediction modeling, subgroup stratification
5. Pathway and mechanism support to explain the biomarker's biological role

**Key design decision:** pQTL instruments (deCODE, UKB-PPP) produce stronger causal
inference than eQTL instruments alone — prefer pQTL when protein targets are the goal.

---

## Pattern Combination Rules

| Combination | When Appropriate |
|---|---|
| A + B | Mechanism gene set *and* key-cell question in same study (score + cell abundance) |
| A + E | Mechanism-derived causal genes → translational biomarker pipeline |
| D + B | Exposure effect → cell-type-specific mediation |
| C + A | Pre-defined candidates → scored against a mechanism gene set for context |

Combining > 2 patterns typically requires Advanced or Publication+ workload.

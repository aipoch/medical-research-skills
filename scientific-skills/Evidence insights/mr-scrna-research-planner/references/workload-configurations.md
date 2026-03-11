# Workload Configurations
# mr-scrna-research-planner

---

## Lite

| Attribute | Detail |
|---|---|
| **Goal** | Rapid preliminary study; proof-of-concept; feasibility check |
| **Timeline** | 2–4 weeks |
| **Data** | 1 public scRNA dataset (GEO) + 1 outcome GWAS (IEU OpenGWAS) |
| **Core Modules** | QC + annotation, module scoring (1 mechanism), basic DEG, univariable MR only |
| **MR** | IVW primary; Weighted Median + MR-Egger as secondary; basic sensitivity |
| **Validation** | Within-dataset consistency check only |
| **Figure complexity** | 4–5 figures: UMAP, scoring heatmap, DEG volcano, MR forest plot, localization |
| **Strengths** | Executable fast; low barrier; establishes basic concept |
| **Weaknesses** | No multivariable MR; no external validation; unlikely to pass competitive journals alone |
| **Typical target** | Preliminary data for grant; pilot report; early submission to lower-tier journals |

---

## Standard

| Attribute | Detail |
|---|---|
| **Goal** | Complete conventional bioinformatics paper |
| **Timeline** | 1–2 months |
| **Data** | 1–2 scRNA datasets + outcome GWAS + 1 independent bulk GEO/TCGA validation cohort |
| **Core Modules** | All Lite modules + multivariable MR, sensitivity suite, Steiger, key-cell prioritization, GSVA/ssGSEA pathway scoring, pseudotime (Monocle3/Slingshot), bulk transcriptomic validation |
| **MR** | IVW + full sensitivity (heterogeneity, pleiotropy, leave-one-out, Steiger) |
| **Validation** | Cross-method MR consistency + independent bulk cohort expression validation |
| **Figure complexity** | 7–8 figures (see figure plan) |
| **Strengths** | Meets typical reviewer expectation for bioinformatics mechanism papers |
| **Weaknesses** | No colocalization; limited multi-population generalizability |
| **Typical target** | Mid-tier journals (Frontiers, IJMS, BMC Genomics, etc.) |

---

## Advanced

| Attribute | Detail |
|---|---|
| **Goal** | Competitive journals; stronger causal and mechanistic evidence |
| **Timeline** | 2–3 months |
| **Data** | 2+ scRNA datasets (ideally different cohorts) + GWAS + bulk validation + GTEx/HPA |
| **Core Modules** | All Standard + pseudobulk DEG (edgeR/DESeq2), CellChat/NicheNet (cell communication), SCENIC/pySCENIC (regulon), colocalization (coloc R) or SMR + HEIDI, disease-subgroup stratification |
| **MR** | Standard suite + colocalization for top hits + SMR HEIDI test |
| **Validation** | Multi-dataset scRNA consistency + multi-bulk-cohort + tissue-level (GTEx/HPA) |
| **Figure complexity** | 8–10 figures; complex network and trajectory figures |
| **Strengths** | Substantially stronger causal evidence; mechanism depth satisfies rigorous reviewers |
| **Weaknesses** | Higher computational demand; colocalization requires aligned GWAS/eQTL loci |
| **Typical target** | Mid-to-high tier (Theranostics, JHematol Oncol, Aging, etc.) |

---

## Publication+

| Attribute | Detail |
|---|---|
| **Goal** | High-ambition manuscript with maximum reviewer defensibility |
| **Timeline** | 3–6 months |
| **Data** | Multi-ancestry GWAS + multiple scRNA datasets + bulk cohorts + clinical data if possible |
| **Core Modules** | All Advanced + bidirectional MR (where biologically justified), multi-ancestry/ethnic stratification, stratified MR (by sex, age, disease subtype), translational enhancement (ROC, prediction model, drug target annotation), manuscript-level figure logic with integrated mechanistic model |
| **MR** | Full suite + bidirectional + stratified + replication in second GWAS population |
| **Validation** | Maximum: multi-cohort, multi-ancestry, cross-tissue, functional if possible |
| **Figure complexity** | 10–12 figures; publication-quality integrated mechanistic schematic |
| **Strengths** | Reviewer-proof structure; suitable for top-tier submission |
| **Weaknesses** | Major time investment; requires high-quality multi-ancestry GWAS availability |
| **Typical target** | High-tier (iScience, Cell Reports, EBioMedicine, eLife, etc.) |

---

## Config Selection Decision Tree

```
User wants results in < 1 month, public data only?
  → Lite (or Standard if output quality is critical)

User wants a conventional bioinformatics mechanism paper?
  → Standard (primary); Advanced (if timeline allows)

User mentions colocalization, SCENIC, multi-dataset, or competitive journal?
  → Advanced

User mentions bidirectional MR, multi-ancestry, translational angle, or top-tier journal?
  → Publication+

User doesn't specify?
  → Default: Standard as primary, Lite as minimum, Advanced as upgrade path
```

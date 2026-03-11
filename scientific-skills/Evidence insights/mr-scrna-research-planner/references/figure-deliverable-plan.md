# Figure and Deliverable Plan
# mr-scrna-research-planner

---

## Standard Figure Set (7–8 figures)

| Figure | Content | Required From |
|---|---|---|
| **Fig 1** | Overall study workflow schematic | All configs |
| **Fig 2** | scRNA-seq QC metrics, UMAP by cell type, annotation markers | All configs |
| **Fig 3** | Key-cell / module-score stratification (high vs low, or disease vs control cell abundance) | All configs |
| **Fig 4** | DEG analysis — volcano plot, heatmap of top DEGs, candidate gene list | All configs |
| **Fig 5** | MR results — forest plots for causal genes; sensitivity summary table | All configs |
| **Fig 6** | Causal gene localization in scRNA — UMAP feature plots + violin plots | All configs |
| **Fig 7** | Pathway enrichment + GSVA / pseudotime trajectory | Standard+ |
| **Fig 8** | Cell communication network or regulon summary (Advanced+) | Advanced+ |

---

## Advanced / Publication+ Extensions

| Figure | Content | Required From |
|---|---|---|
| **Fig 9** | Colocalization locus plot or SMR Manhattan | Advanced+ |
| **Fig 10** | External validation — expression in independent bulk cohort | Standard+ (can be supplementary) |
| **Fig 11** | Integrated mechanistic model schematic | All configs (can be simple for Lite) |
| **Fig 12** | Translational enhancement: ROC curve, nomogram, or drug target annotation | Publication+ (translational angle) |

---

## Supplementary Figure Expectations

| Supplementary Content | Notes |
|---|---|
| Full sensitivity analysis forest plots (leave-one-out, MR-Egger) | Standard reviewer expectation |
| scRNA QC per-sample statistics | Required for methods transparency |
| WGCNA soft-threshold power plot (if used) | Methodological checkpoint |
| Additional UMAP facets (by sample, by condition) | Common reviewer request |
| Pseudotime branch statistics | Supports trajectory claims |
| Full DEG tables | Supplementary table |
| Full MR result tables | Supplementary table |

---

## Intermediate Deliverable Checklist

Use as a gate before moving to the next analysis phase.

**Phase 1 — scRNA Setup**
- [ ] Dataset downloaded and loaded (Seurat/Scanpy object)
- [ ] QC metrics computed (nFeature, nCount, MT%)
- [ ] Doublets removed (DoubletFinder / scrublet)
- [ ] Normalized and variable features selected
- [ ] PCA + UMAP computed + clusters defined
- [ ] Cell type annotation complete (UMAP labeled figure ready)

**Phase 2 — scRNA Analysis**
- [ ] Cell composition comparison (if applicable)
- [ ] Module scoring or key-cell DEG complete
- [ ] Comparison groups defined + justified
- [ ] DEG table (gene, logFC, p.adj, direction)
- [ ] Volcano plot and heatmap ready
- [ ] Pathway enrichment (GSVA / clusterProfiler) complete

**Phase 3 — MR**
- [ ] GWAS data retrieved (IEU OpenGWAS / FinnGen / UKB)
- [ ] eQTL / pQTL instruments extracted
- [ ] SNPs clumped and pruned
- [ ] Univariable MR run (IVW + Egger + WM + WMode)
- [ ] Sensitivity suite complete (heterogeneity, pleiotropy, LOO, Steiger)
- [ ] Multivariable MR run (if Standard+)
- [ ] Colocalization / SMR run (if Advanced+)

**Phase 4 — Integration**
- [ ] MR-prioritized genes localized in scRNA (UMAP + violin plots)
- [ ] Pseudotime trajectory complete
- [ ] Cell communication analysis complete (if Advanced+)
- [ ] Regulon / SCENIC analysis complete (if Advanced+)
- [ ] External bulk validation complete
- [ ] Mechanistic model figure drafted

**Phase 5 — Manuscript**
- [ ] Full figure set finalized
- [ ] Supplementary tables compiled
- [ ] Methods section drafted (tool versions, parameter values)
- [ ] Results section aligned with figure order

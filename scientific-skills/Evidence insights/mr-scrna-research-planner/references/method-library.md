# Method Library
# mr-scrna-research-planner

---

## Single-Cell Analysis Tools

### Primary Pipelines
| Tool | Language | Use Case |
|---|---|---|
| Seurat | R | Most common; best integration with downstream R packages |
| Scanpy | Python | Preferred for large datasets; memory-efficient |

### QC and Doublet Detection
| Tool | Purpose |
|---|---|
| DoubletFinder | Doublet detection for Seurat workflows |
| scrublet | Python-based doublet detection for Scanpy |
| scuttle / scran | Per-cell QC metrics; adaptive QC thresholds |

### Cell Annotation
| Tool | Approach |
|---|---|
| SingleR | Automated reference-based annotation (HumanPrimaryCellAtlasData, etc.) |
| Marker-based | Manual curation using canonical cell-type marker lists |
| Azimuth | Atlas-based mapping for common tissues |

### Pseudotime and Trajectory
| Tool | Strength |
|---|---|
| Monocle3 | Good for continuous trajectories; graph-based |
| Slingshot | Multiple lineages; integrates well with Seurat/Bioconductor |

### Cell Communication
| Tool | Strength |
|---|---|
| CellChat | Curated ligand-receptor database; quantitative signaling strength |
| CellPhoneDB | Validated human L-R pairs; well-cited |
| NicheNet | Prioritizes ligands by downstream target gene activity |

### Regulon / TF Network
| Tool | Language |
|---|---|
| SCENIC | R — standard; well-established |
| pySCENIC | Python — faster for large datasets |

### Pathway Scoring
| Tool | Method |
|---|---|
| GSVA | Gene Set Variation Analysis (per-sample) |
| ssGSEA | Single-sample GSEA |
| fgsea | Fast GSEA (R); good for ranked gene lists |
| clusterProfiler | GO/KEGG enrichment for gene sets |

---

## MR Tools

| Tool | Purpose |
|---|---|
| TwoSampleMR (R) | Primary MR package; IVW, Egger, Weighted Median, sensitivity |
| MVMR (R) | Multivariable MR |
| coloc (R) | Colocalization of two GWAS signals at a locus |
| SMR + HEIDI | Summary-based MR; binary pleiotropy test |
| MendelianRandomization (R) | Additional methods; contamination mixture model |
| PLINK | LD clumping and pruning |

---

## GWAS / eQTL / pQTL Data Resources

### Outcome GWAS
| Resource | Coverage |
|---|---|
| IEU OpenGWAS | Thousands of traits; R API via TwoSampleMR |
| FinnGen | Finnish population; deep phenotyping |
| UK Biobank | Large European cohort; broad trait coverage |
| GWAS Catalog | Curated significant associations |

### eQTL Instruments
| Resource | Tissue Coverage |
|---|---|
| eQTLGen | Blood cis-eQTL (n > 30,000) — preferred for blood traits |
| GTEx v8 | 49 tissues; available via TwoSampleMR |
| PsychENCODE | Brain tissue eQTL |

### pQTL Instruments (preferred for protein targets)
| Resource | Platform |
|---|---|
| deCODE pQTL | SomaScan; ~4,900 proteins; Icelandic population |
| UKB-PPP | Olink; ~2,900 proteins; UK Biobank |
| INTERVAL | SomaScan; blood proteins |

### Single-Cell Reference Datasets
| Resource | Content |
|---|---|
| GEO | Primary public scRNA repository; use GSE search by tissue + disease |
| TISCH2 | Tumor immune single-cell atlas; pre-annotated |
| CellxGene | Curated annotated single-cell datasets |
| Human Cell Atlas | Normal tissue reference |

---

## Parameter Defaults and Decision Rules

| Parameter | Default | Notes |
|---|---|---|
| GWAS significance | p < 5×10⁻⁸ | Genome-wide; relax to p < 1×10⁻⁵ if instruments are sparse |
| LD clumping r² | < 0.001 | Window 10,000 kb |
| Instrument count minimum | ≥ 3 SNPs | IVW requires ≥ 2; prefer ≥ 10 for robust sensitivity |
| scRNA QC — min genes/cell | 200–500 | Tissue-dependent; verify with distribution plot |
| scRNA QC — max MT% | 10–25% | Tissue-dependent; neurons tolerate higher |
| Clustering resolution | 0.4–1.0 | Start at 0.6; adjust to biological expectation |
| WGCNA soft threshold | β where R² ≥ 0.85 | Scale-free fit |
| DEG adjusted p cutoff | FDR < 0.05 | Use Benjamini-Hochberg; log2FC > 0.25 for scRNA |
| Colocalization H4 threshold | PP.H4 > 0.75 | Strong colocalization evidence |

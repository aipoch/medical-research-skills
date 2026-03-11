# Implementation Outline
# tcm-biomedical-research-strategist

Practical code/software outline for executing the analytical plan. Not full code — enough to demonstrate executability.

Label each step: **[Computational]**, **[Manual Curation]**, or **[Experimental]**.

```
Phase 1: Compound & Target Data (Python / R / manual curation)           [Computational + Manual]
  - TCMSP API or manual download → parse compound table
  - Filter: OB ≥ 30%, DL ≥ 0.18 (or stated alternative thresholds)
  - Swiss Target Prediction batch query

Phase 2: Disease Targets (R / manual)                                     [Computational + Manual]
  - GeneCards search export
  - DisGeNET R package query: disgenet2r::disease2gene(disease = "...", database = "CURATED")

Phase 3: Transcriptomics (R)                                              [Computational]
  - GEOquery::getGEO("GSEXXXXX") → ExpressionSet
  - limma (microarray) or DESeq2 (RNA-seq) for DEG
  - WGCNA::blockwiseModules() for co-expression modules

Phase 4: Network (R / Python / Cytoscape)                                 [Computational]
  - STRINGdb::STRINGdb$new(score_threshold = 400) → PPI network
  - igraph → degree, betweenness, closeness centrality
  - Cytoscape for visualization and CytoHubba plugin for hub scoring

Phase 5: ML Hub Gene Ranking (R / Python)                                 [Computational]
  - randomForest::randomForest() with importance scoring
  - glmnet::cv.glmnet() for LASSO feature selection
  - e1071::svm() with RFE for SVM-RFE
  - Cross-validate on held-out samples (70/30 split)

Phase 6: Immune Analysis (R)                                              [Computational]
  - CIBERSORT via TIMER2.0 web interface (LM22 signature matrix)
  - OR: GSVA::gsva(expr, gene.sets, method = "ssgsea")
  - Spearman correlation: hub gene expression vs infiltrate score
  - Visualization: corrplot / ggplot2 heatmap

Phase 7: Molecular Docking (AutoDock Vina / PyMOL)                       [Computational]
  - Retrieve target PDB structure or AlphaFold model
  - Prepare receptor: remove water, add hydrogens, define grid box
  - Prepare ligand: PubChem SDF → Open Babel → .pdbqt format
  - Run: vina --config config.txt --ligand ligand.pdbqt --out out.pdbqt
  - Score threshold: ΔG < −5 kcal/mol; visualize top poses in PyMOL
```

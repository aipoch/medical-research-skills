# Analysis Modules & Method Library

## Toxicant Target Retrieval
- PubChem → SMILES / structure retrieval
- CTD → toxicant–gene associations
- SwissTargetPrediction → SMILES-based prediction
- TargetNet → SMILES-based prediction
- Target merging, deduplication, STRING/UniProt normalization

## Disease Target Retrieval
- GeneCards (relevance score filter, e.g. ≥1)
- DisGeNET (GDA score filter, e.g. ≥0.1)
- DrugBank (disease "indications")
- Merged, deduplicated disease target library

## Overlap & Network
- Venn analysis (R: VennDiagram or ggVennDiagram)
- STRING PPI construction (confidence threshold ≥ 0.7 for Standard+)
- Cytoscape import + layout
- CytoHubba → hub gene screening (MCC algorithm default; Degree / Betweenness as alternatives)
- Network visualization

## Enrichment & Mechanism
- Entrez ID conversion (clusterProfiler)
- GO enrichment (BP / CC / MF)
- KEGG enrichment
- Visualization: bar plots, bubble plots
- Threshold: p.adjust < 0.05, q < 0.05
- Tools: clusterProfiler, enrichplot, ggplot2, org.Hs.eg.db

## Expression Validation
- GEO dataset search (keywords: disease name + "Homo sapiens")
- Disease vs. control group definition
- Core gene expression comparison (t-test or Wilcoxon)
- Boxplot visualization
- Acknowledge sample-size limits explicitly

## Molecular Docking
- Ligand: PubChem SDF download → format conversion
- Receptor: UniProt accession → PDB structure retrieval
- Docking tool: CB-Dock2 (primary) or AutoDock Vina
- Score interpretation: binding energy (kcal/mol); lower = stronger affinity
- Pose visualization: CB-Dock2 3D viewer or PyMOL
- 2D interaction mapping: Discovery Studio Visualizer
- Target selection: top hub genes with available high-resolution PDB structures

## Selection Rules for Docking Targets
1. Must be in the hub gene list
2. Must have a high-quality PDB structure (resolution < 3.0 Å preferred)
3. Prioritize targets with known ligand-binding pockets
4. If no structure available, use AlphaFold model with explicit caveat

---

## Minimum Viable Overlap Thresholds & Zero-Overlap Recovery

### Thresholds

| Tier | Minimum overlap genes to proceed |
|---|---|
| Lite | ≥ 3 genes |
| Standard | ≥ 5 genes |
| Advanced / Publication+ | ≥ 5 genes (≥ 10 recommended for robust PPI) |

### Zero-Overlap Recovery Sequence

If the toxicant–disease overlap falls below the minimum threshold, apply the following steps **in order** before declaring infeasibility:

1. **Loosen disease target filter**: reduce GeneCards relevance score cutoff from ≥1 to ≥0.5; reduce DisGeNET GDA score from ≥0.1 to ≥0.05
2. **Expand toxicant target sources**: if only 2 prediction sources used, add a third (e.g., TargetNet, SEA — see Toxicant Target Retrieval module)
3. **Manual literature curation**: search PubMed for direct toxicant–gene associations; add up to 10 curated targets with source citations; label as "manually curated — lower confidence"
4. **Switch enrichment strategy**: if overlap < 3 genes after steps 1–3, pivot to pathway-level overlap (KEGG pathway → gene list expansion) rather than direct gene overlap
5. **If still empty after all steps**: inform the user that no computationally recoverable overlap was found; recommend (a) broader disease phenotype re-specification (e.g., switch from a specific disease subtype to the parent disease), (b) a different toxicant from the same chemical class, or (c) a literature-only mechanism review as an alternative study format

**Activate this sequence whenever Hard Rule 11 fires.** Document all recovery steps taken in Part G (Validation & Robustness) of the output.

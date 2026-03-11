# Data Sources Reference
# tcm-biomedical-research-strategist

## Herbal Compounds + Targets
- TCMSP (https://tcmsp-e.com) — primary source; OB ≥ 30%, DL ≥ 0.18 default thresholds
- HERB (http://herb.ac.cn) — broader compound coverage for less-studied herbs
- SymMap (https://www.symmap.org) — symptom-mapped TCM network
- UNPD / ChEMBL — fallback for rare herbs absent in TCMSP

## Target Prediction
- Swiss Target Prediction (http://www.swisstargetprediction.ch) — preferred for batch query
- SEA (Similarity Ensemble Approach) — chemical similarity-based
- SuperPred (https://prediction.charite.de)

## Disease Target Databases
- GeneCards (https://www.genecards.org) — primary disease gene set
- OMIM (https://www.omim.org) — Mendelian disease genes
- DisGeNET (https://www.disgenet.org) — R package available; curated + inferred evidence
- TTD (Therapeutic Target Database) — drug-target validation context

## Transcriptomics Datasets
- GEO (https://www.ncbi.nlm.nih.gov/geo) — primary repository; select ≥ 30 samples per group
- TCGA (https://portal.gdc.cancer.gov) — TCGA-COAD/READ for CRC; TCGA-LIHC for HCC; TCGA-LUAD/LUSC for NSCLC
- Preferred platforms: Illumina RNA-seq or Affymetrix microarray (known normalization methods)

## Protein–Protein Interaction Networks
- STRING (https://string-db.org) — STRINGdb R package for programmatic access; combined score ≥ 0.4 default
- BioGRID (https://thebiogrid.org) — experimental PPI fallback
- IntAct (https://www.ebi.ac.uk/intact) — curated interactions

## Protein Structures
- PDB (https://www.rcsb.org) — primary crystal structure source
- AlphaFold DB (https://alphafold.ebi.ac.uk) — predicted structures for targets lacking PDB entry
- UniProt (https://www.uniprot.org) — canonical protein sequences + domain annotations

## Ligand Structures
- PubChem (https://pubchem.ncbi.nlm.nih.gov) — SDF downloads for docking prep
- ChEMBL (https://www.ebi.ac.uk/chembl) — bioactivity data + structures
- ZINC (https://zinc.docking.org) — pre-prepared ligand libraries

## Immune Deconvolution
- TIMER2.0 (http://timer.comp-genomics.org) — web-based immune infiltrate estimation
- ESTIMATE — stromal/immune score from bulk RNA
- xCell (https://xcell.ucsf.edu) — multi-cell enrichment
- TISCH2 (http://tisch.comp-genomics.org) — single-cell immune deconvolution reference

## Pathway Annotations
- MSigDB (https://www.gsea-msigdb.org) — hallmark and curated gene sets
- Reactome (https://reactome.org) — mechanistic pathway maps
- KEGG (https://www.kegg.jp) — pathway IDs for clusterProfiler

## Docking Software
- AutoDock Vina — free; standard ΔG < −5 kcal/mol threshold
- PyMOL — visualization and binding site analysis
- Open Babel — ligand format conversion (SDF → PDBQT)

# Study Patterns (A–E)

## A. Single Toxicant–Single Disease Design
**When**: one toxicant + one disease/phenotype.  
**Examples**: triclosan + PMOP · BPA + endometriosis · cadmium + CKD · PFAS + metabolic syndrome.  
**Logic**: retrieve toxicant targets → retrieve disease targets → calculate overlap → construct PPI → identify hub genes → GO/KEGG enrichment → expression validation (if available) → dock to core proteins.

## B. Endocrine Disruptor Mechanism Design
**When**: toxicant is an EDC; user wants endocrine-focused interpretation.  
**Examples**: triclosan + bone metabolism · parabens + thyroid dysfunction · BPA + reproductive disorders.  
**Logic**: collect EDC targets → retrieve endocrine-related disease targets → identify overlapping targets → enrich endocrine/metabolic pathways → dock to hormone-related and signaling targets → emphasize endocrine disruption + metabolic signaling.

## C. Network Toxicology + Random Dataset Validation
**When**: user wants a lightweight expression validation layer.  
**Logic**: identify toxicant–disease overlap → screen hub genes → retrieve one relevant GEO dataset → compare core gene expression control vs. disease → boxplots/t-tests as supportive validation → enrichment + docking.

## D. PPI Hub Gene + Docking-Centered Design
**When**: user wants compact but publishable workflow focused on hub genes and docking.  
**Examples**: environmental pollutant + disease risk · food contaminant + organ toxicity.  
**Logic**: predict toxicant targets → collect disease genes → intersect → build PPI → top hub genes → dock to top 3–5 hubs → pathway interpretation.

## E. Publication-Oriented Network Toxicology Design
**When**: user wants a stronger mechanism paper with full validation.  
**Logic**: target prediction → disease genes → overlap → PPI + hub identification → GO/KEGG → expression validation → docking → integrated mechanism model → limitations + follow-up suggestions.

## F. Multi-Toxicant Comparative Design
**When**: user provides 2–3 toxicants + one shared disease/phenotype and wants a comparative analysis.  
**Examples**: chlorpyrifos + atrazine + glyphosate + cardiovascular disease · BPA + phthalates + endometriosis · cadmium + lead + CKD.  
**Constraints**: maximum 3 toxicants for Standard tier; 2 toxicants for Lite tier; unlimited for Publication+.  
**Logic**:
1. Run single-toxicant target retrieval (CTD + SwissTargetPrediction) for each toxicant independently
2. Retrieve shared disease targets once (GeneCards + DisGeNET)
3. Compute per-toxicant overlap with disease targets → individual overlap gene lists
4. Generate comparative Venn: all-toxicant shared core · pairwise overlaps · toxicant-exclusive targets
5. Construct unified PPI from the all-toxicant shared core genes (String, confidence ≥ 0.7)
6. Hub gene identification from unified PPI → hub overlap analysis across toxicants
7. GO/KEGG enrichment on shared core + per-toxicant comparison
8. Optional: comparative docking — dock each toxicant to the top shared hub(s); compare binding affinity profiles
9. Mechanism interpretation: shared pathway vulnerability vs. toxicant-specific mechanisms

**Key output additions vs. Pattern A**:
- Comparative Venn figure (3-set or 2-set for each toxicant pair)
- Per-toxicant vs. shared hub gene table
- Comparative docking score table (if docking included)
- Explicit statement: parallel single-toxicant analyses; no interaction/synergy claims between toxicants

**Hard constraints for Pattern F**:
- Never infer synergistic or additive toxicity from target overlap alone
- Always run each toxicant retrieval independently before merging
- If one toxicant returns 0 overlap with disease targets, apply zero-overlap recovery sequence (see `modules.md`) for that toxicant only; do not conflate with other toxicants

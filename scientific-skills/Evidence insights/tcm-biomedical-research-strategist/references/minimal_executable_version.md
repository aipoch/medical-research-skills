# Minimal Executable Version
# tcm-biomedical-research-strategist — Section 10 Reference

> For researchers who need results in 2–4 weeks using only public databases and free
> computational tools — no wet-lab experiments, no institutional resources beyond a
> standard laptop or free cloud compute.

---

## Day-by-Day Plan

| Step | Tool / Resource | Time Estimate | Output |
|---|---|---|---|
| Compound collection | TCMSP / HERB (web) | Day 1–2 | Screened compound list with ADME values |
| Target prediction | SwissTargetPrediction (batch upload) | Day 2–3 | Compound–target table |
| Disease genes | GeneCards search + DisGeNET web | Day 3 | Disease gene list with source annotation |
| Intersection | R `intersect()` or Excel | Day 4 | Candidate target set + Venn figure |
| PPI network | STRING web → Cytoscape | Day 5–6 | Network image + hub candidate list |
| Transcriptomics | GEO (1 dataset) + limma R | Day 7–10 | DEG table + volcano plot |
| Enrichment | clusterProfiler R | Day 10–12 | GO/KEGG dot plots |
| Immune infiltration | TIMER2.0 web tool | Day 12–14 | Immune correlation table |
| Molecular docking | AutoDock Vina (free) | Week 3–4 | Top 3–5 compound–target docking scores |

---

## Capability Boundaries

### What this version CANNOT claim:
- **Causal mechanism** — no siRNA knockdown, no overexpression rescue
- **Dynamic binding stability** — no molecular dynamics simulation
- **In vivo or clinical relevance** — no animal models, no patient cohorts
- **Drug-likeness beyond ADME filters** — no ADMET profiling, no toxicity prediction

### What this version CAN contribute:
- Hypothesis generation for experimental follow-up
- Compound–target prioritization list with multi-evidence support
- Pathway-level mechanistic rationale
- Immune microenvironment association hypothesis
- Preliminary docking evidence for top compound–target pairs
- **Publishable as a preliminary/pilot study** in journals accepting computational NP designs

---

## Minimum Viable Output for Publication

A minimal NP paper typically requires:
1. Screened compound table (ADME values)
2. Venn intersection figure (compound targets ∩ disease targets)
3. PPI network figure with labeled hub genes
4. GO/KEGG enrichment plots (top 20 terms)
5. Molecular docking table (top 3–5 pairs, ΔG values, binding pose figures)
6. Cross-validation in ≥ 1 independent GEO dataset

This version produces all 6 within the 4-week timeline.

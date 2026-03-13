# Workload Configurations

## Lite
**Best for**: quick launch · 2–4 week execution · preliminary manuscript skeleton.  
**Must include**: toxicant target retrieval · disease target retrieval · overlap analysis · PPI network · hub gene identification · basic GO/KEGG enrichment · docking to top targets.  
**Avoid**: excessive validation layers · complicated transcriptomic validation · overinflated network add-ons.

## Standard ← Default Primary Recommendation
**Best for**: mainstream toxicology mechanism papers · endocrine or chronic disease studies.  
**Must include**: all Lite components + high-confidence PPI (STRING score > 0.7) · hub ranking with explicit algorithm (MCC preferred) · GO/KEGG interpretation · one expression validation layer (if available) · docking to top 3–5 core targets · integrated mechanism model.

## Advanced
**Best for**: competitive journals · reviewers asking for stronger biological plausibility.  
**Must include**: all Standard components + multiple target-prediction sources with harmonization · careful disease target filtering · explicit docking selection strategy · secondary validation dataset or alternative phenotype support · stronger pathway ranking logic · sensitivity analysis on hub-selection algorithm.

## Publication+
**Best for**: ambitious environmental toxicology manuscripts · multi-layer mechanism papers.  
**Must include**: all Advanced components + multiple disease/subtype comparisons (if justified) · alternative hub-identification algorithm comparison · docking comparison across multiple targets or chemicals · integrated network-to-docking figure logic · explicit wet-lab follow-up suggestions.

---

## Article Pattern Coverage Matrix

| Pattern | Requirement | Notes |
|---|---|---|
| Toxicant target prediction + disease target intersection | Required | Core structure |
| PPI + hub gene discovery | Required | Core network layer |
| GO / KEGG + docking | Required | Most common mechanism workflow |
| GEO / random expression validation | Recommended (Standard+) | When dataset available |
| Docking of top hub genes | Required | Core strengthening module |
| Endocrine/metabolic pathway interpretation | Recommended | If biologically relevant |
| Multiple target-prediction databases (≥2) | Required (Standard+) | Reduces prediction noise |
| High-confidence STRING + Cytoscape + CytoHubba | Required | Standard published pattern |
| Integrated mechanism model figure | Required | Publication-oriented output |
| Wet-lab follow-up suggestions | Optional | Publication+ or translational |

---

## Reviewer Risk Register

| Risk | Mitigation |
|---|---|
| Toxicant target prediction noise | Use ≥2 independent prediction sources; report union and intersection counts |
| Disease target database bias (GeneCards keyword sensitivity) | Apply score filters (GeneCards ≥1, DisGeNET ≥0.1); use ≥2 disease databases |
| Hub-gene instability across algorithms | Report MCC results; optionally run Degree or Betweenness as sensitivity check |
| Weak transcriptomic validation (small GEO cohort) | Acknowledge sample size; label as supportive only; avoid over-interpreting t-test p-values |
| Docking overinterpretation | State binding energy is computational only; in vitro confirmation required for causal claims |
| No in vivo / in vitro validation | Acknowledge as major limitation; suggest qPCR, cell viability, or animal model follow-up |
| Pathway enrichment as causal mechanism | Use hedged language; note enrichment is associational, not mechanistic proof |
| AlphaFold structure used for docking | Flag explicitly; prefer experimental PDB structures (resolution < 3.0 Å) |

---

## Configuration Comparison Table (output as table in response)

| Dimension | Lite | Standard | Advanced | Publication+ |
|---|---|---|---|---|
| Target sources | 2 | ≥2 | ≥3 + harmonization | ≥3 + harmonization |
| Hub algorithm | 1 | MCC | MCC + sensitivity | MCC + ≥1 alternative |
| Validation | None | GEO (if available) | GEO + secondary | Multi-dataset |
| Docking targets | Top 3 | Top 3–5 | Top 5 + rationale | Multi-target comparison |
| Workload | 2–4 wk | 4–6 wk | 6–10 wk | 10–16 wk |

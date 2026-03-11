# Expert Deep Review Extensions

Load this file when running Expert Deep Review mode (in addition to the standard track
modules from tracks.md). These extensions expand the analysis depth on five dimensions.

---

## Extension 1: Detailed Methodological Appraisal

For each major methodological choice in the paper, address:
1. **What was chosen** — the specific method, tool, or algorithm
2. **Why it was likely chosen** — historical convention, computational cost, interpretability
3. **What the better alternative would be** — and why it was not used
4. **What bias or error this choice introduces** — and whether it affects the conclusions

Cover at minimum: primary analysis method, validation strategy, and statistical approach.

---

## Extension 2: Hybrid Evidence-Chain Judgment

*For multi-track papers only.*

Map the complete evidence chain from discovery to claim:

```
[Data source / experimental system]
    ↓ [What was found]
[Validation layer 1] → strength: High / Medium / Low
    ↓ [What was confirmed]
[Validation layer 2] → strength: High / Medium / Low
    ↓ ...
[Central claim]
    ↓
[Gap between evidence and claim — if any]
```

Then provide: which layer is strongest, which is weakest, and what single piece of
evidence would most change the overall credibility of the paper's central claim.

---

## Extension 3: Translational Significance Assessment

Address all applicable questions:
1. Does this finding have a plausible path from bench to bedside (or database to clinic)?
2. What development stage is this finding at (target identification / lead validation / clinical hypothesis / clinical evidence)?
3. What are the three most important translational gaps?
4. Is the proposed biomarker / target / intervention already being tested in clinical trials (NCT registry)? If so, is this paper consistent with that trajectory?
5. What patient population would benefit first if the finding holds?

---

## Extension 4: Reproducibility and Open Science Assessment

1. **Data availability** — are all data accessible? GEO/TCGA accessions confirmed? Raw data shared?
2. **Code availability** — is the analysis code publicly available and documented?
3. **Parameter transparency** — are all key thresholds, seeds, and pipeline parameters reported?
4. **Reagent transparency** — antibody catalogue numbers, cell line sources, oligonucleotide sequences?
5. **Reproducibility estimate** — on a scale of Low / Medium / High, how reproducible is this paper in another laboratory, and why?

---

## Extension 5: Next-Step Research Design Suggestions

Generate 2–3 concrete follow-up study designs that would:
- Address the weakest link in the current paper's evidence chain
- Increase the evidence level by one step (e.g., from association to causation, or from in vitro to in vivo)
- Be feasible within a 2-year research programme

For each design suggestion, state:
- Study type and system
- Primary endpoint
- Why this design addresses the identified gap
- Estimated feasibility (resource requirements, timeline, key risks)

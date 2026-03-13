# Mandatory Output Structure

Every response must contain Parts A–I in order.

## Part A — Core Research Question
- One-sentence research question
- 2–4 specific aims
- Why network toxicology + docking is appropriate for this topic

## Part B — Configuration Overview
Comparison table: Lite · Standard · Advanced · Publication+  
Columns: goal · required data · main modules · workload · strengths · weaknesses

## Part C — Recommended Primary Plan
- Name the best-fit configuration
- Explain why it fits
- Explain why others are less suitable for this specific case

## Part D — Step-by-Step Workflow
For every step:
- Step Name
- Purpose
- Input
- Method
- Key Parameters / Decision Rules
- Expected Output
- Failure Points
- Alternative Methods

## Part E — Target & Dataset Framework
- Toxicant definition
- Disease definition
- Toxicant target sources + rationale
- Disease target sources + rationale
- Overlap logic
- Validation dataset logic (if used)
- Docking target selection logic

## Part F — Figures & Deliverables
Recommended figure set:
1. Overall workflow schematic
2. Toxicant + disease target collection / Venn overlap
3. PPI network + hub gene results
4. Expression validation boxplots (if applicable)
5. GO enrichment bar/bubble plot
6. KEGG enrichment bar/bubble plot
7. Docking 3D poses + 2D interaction maps
8. Integrated toxic mechanism model

Deliverables list: toxicant target table · disease target table · overlap gene list · hub gene list · GO/KEGG results · validation summary · docking score summary · mechanism interpretation · reviewer-facing limitation notes.

## Part G — Validation & Robustness

Explicitly separate all five layers. For each layer state what it proves AND what it does not prove:

1. **Target-source robustness**
   - Multi-database toxicant target coverage (≥2 sources)
   - Multi-database disease target coverage (≥2 sources)
   - Overlap size and consistency
   - *Proves*: shared molecular target space exists
   - *Does not prove*: toxicant engages these targets in vivo

2. **Network robustness**
   - STRING confidence threshold (≥0.7 for Standard+)
   - Hub algorithm choice (MCC default) + optional sensitivity
   - *Proves*: network centrality of candidate hubs
   - *Does not prove*: hub genes are causal drivers of toxicity

3. **Expression support**
   - GEO dataset selection logic + sample size
   - Disease vs. control comparison of core genes
   - Boxplot + t-test (acknowledge limits)
   - *Proves*: core genes are dysregulated in disease context
   - *Does not prove*: dysregulation is caused by the specific toxicant

4. **Docking support**
   - Ligand/receptor preprocessing (PDB quality, resolution)
   - Binding energy range and pose selection
   - 3D/2D visualization
   - *Proves*: computational binding feasibility
   - *Does not prove*: direct biological activity or in vivo binding

5. **Enrichment support**
   - GO/KEGG pathway associations (p.adjust < 0.05)
   - Pathway narrative consistency with known toxicant biology
   - *Proves*: pathway-level associations in target set
   - *Does not prove*: causal mechanism — associational only

6. **Reviewer risk points**: list ≥4 likely criticisms with responses
7. **Overclaim risks**: what the design cannot prove

## Part H — Minimal Executable Version
2–4 week version using only essential modules.  
Public data only · one toxicant · one disease · ≥2 target-prediction sources · overlap analysis · high-confidence PPI · one hub algorithm · GO/KEGG · docking of top 3 targets.

## Part I — Publication Upgrade Version
Show exactly what to add beyond Standard:
- Which additions improve publication strength most
- Which improve rigor vs. which mostly increase complexity
- Typical upgrade modules: GEO validation · second validation dataset · alternative hub algorithm · stronger docking rationale · disease subtype refinement · wet-lab suggestions

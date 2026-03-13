---
name: network-tox-docking-research-planner
description: Generates complete network toxicology + molecular docking research designs from a user-provided toxicant and disease/phenotype. Always use this skill when users want to investigate how an environmental toxicant, endocrine disruptor, heavy metal, food contaminant, pharmaceutical residue, or consumer product chemical may contribute to a disease through shared molecular targets, hub genes, pathways, and docking evidence. Trigger for: "network toxicology study", "toxicology mechanism paper", "target prediction + PPI + docking", "environmental pollutant and disease mechanism", "hub genes and docking for toxicant", "Lite/Standard/Advanced toxicology plan", "CTD + SwissTargetPrediction + GeneCards + STRING", "CB-Dock2 docking study", "triclosan/BPA/cadmium/PFAS + disease". Also triggers for Chinese phrasings: "网络毒理学研究设计"、"毒物机制论文"、"靶点预测+PPI+对接"、"环境污染物与疾病机制". Trigger even for casual phrasings like "I want to study how chemical X affects disease Y" or "help me design a toxicology paper". Always output four workload configurations (Lite / Standard / Advanced / Publication+) with a recommended primary plan, step-by-step workflow, figure plan, validation strategy, minimal executable version, and publication upgrade path.
license: MIT
skill-author: AIPOCH
---

# Network Toxicology + Molecular Docking Research Planner

Generates a complete network toxicology + molecular docking study design from a user-provided toxicant and disease/phenotype. Always outputs four workload configurations and a recommended primary plan.

## Input Validation

This skill accepts: a toxicant (environmental chemical, endocrine disruptor, heavy metal, food contaminant, pharmaceutical residue, or consumer product chemical) paired with a disease or phenotype, for which the user wants to generate a network toxicology + molecular docking research design.

If the user's request does not involve a toxicant–disease pair for network toxicology research design — for example, asking to execute a STRING query, download GEO datasets, write production code, answer a clinical pharmacology question, or design a non-toxicology study — do not proceed with the workflow. Instead respond:
> "Network Toxicology + Molecular Docking Research Planner is designed to generate computational research designs for toxicant–disease mechanism studies. Please provide a toxicant and a disease or phenotype. If you want to run the analysis directly, use a data-execution tool; if you need a different study type, use the appropriate planner skill."

**Minimum required input:** one toxicant + one disease or phenotype.  
If workload is unspecified, default to: **Standard** as primary · **Lite** as minimal · **Advanced** as upgrade.

---

## Step 1 — Infer Study Context

Read → `references/decision-logic.md`

Identify: toxicant class · disease type · whether docking is central or supportive · validation feasibility · resource constraints · publication ambition · whether input involves multiple toxicants (→ Pattern F in Step 2).

---

## Step 2 — Select Study Pattern

Read → `references/study-patterns.md`

Match to one of six canonical design styles (A–F). State which pattern applies and why.

| Pattern | When to use |
|---|---|
| A. Single Toxicant–Single Disease | Core design, any toxicant + disease pair |
| B. Endocrine Disruptor Mechanism | EDC + hormone/metabolic/reproductive disease |
| C. Network Tox + Random Dataset Validation | Light GEO expression support layer |
| D. PPI Hub Gene + Docking-Centered | Compact publishable hub+docking focus |
| E. Publication-Oriented Integrated | Full pipeline, stronger mechanism story |
| F. Multi-Toxicant Comparative | 2–3 toxicants + one disease, comparative overlap analysis |

---

## Step 3 — Generate Four Configurations

Read → `references/configurations.md`

Always output all four tiers — **except** when the user explicitly requests only one tier AND the request is time- or resource-constrained (e.g., "2-week Lite only"). In that case, output the requested tier in full and include a collapsed one-row summary for the other three tiers labeled "Other Configurations (summary only)."

Recommend one tier. Justify the choice.

| Tier | Best for | Workload | Target sources | Docking targets |
|---|---|---|---|---|
| **Lite** | Quick launch, skeleton paper | 2–4 wk | 2 | Top 3 |
| **Standard** | Mainstream publication *(default)* | 4–6 wk | ≥2 | Top 3–5 |
| **Advanced** | Competitive journals | 6–10 wk | ≥3 + harmonization | Top 5 + rationale |
| **Publication+** | High-impact, multi-layer | 10–16 wk | ≥3 + harmonization | Multi-target comparison |

---

## Step 4 — Expand Primary Workflow

For each step follow the **step-level standard** (every step must include):  
`Step Name / Purpose / Input / Method / Key Parameters / Expected Output / Failure Points / Alternative Methods`

Draw modules from → `references/modules.md`

---

## Step 5 — Mandatory Output Sections

Read → `references/output-standard.md`

Every response must contain all nine parts (A–I):

1. **Core research question** (one sentence + 2–4 specific aims)
2. **Configuration overview** (4-tier table)
3. **Recommended primary plan** + rationale
4. **Step-by-step workflow** (expanded for recommended tier)
5. **Target & dataset framework**
6. **Figure & deliverable list**
7. **Validation & robustness plan** — five evidence layers with proves/does-not-prove (see `references/output-standard.md` Part G)
8. **Minimal executable version** (Lite-level, 2–4 weeks)
9. **Publication upgrade path**

---

## Article Pattern Coverage

Plans must address these patterns when relevant:

| Pattern | Requirement |
|---|---|
| Toxicant target prediction + disease target intersection | Required |
| PPI + hub gene discovery (STRING + Cytoscape + CytoHubba) | Required |
| GO / KEGG enrichment | Required |
| Docking of top hub genes (CB-Dock2 or AutoDock Vina) | Required |
| GEO / random expression validation | Recommended (Standard+, when dataset available) |
| Endocrine/metabolic pathway interpretation | Recommended (if biologically relevant) |
| Multiple target-prediction databases | Required (Standard+) |
| Integrated mechanism model figure | Required |
| Wet-lab follow-up suggestion | Optional (Publication+) |

---

## Hard Rules

1. Always output all four workload configurations — **except** when the user explicitly requests one tier AND confirms a time/resource constraint; in that case output the requested tier fully and a collapsed one-row summary for the remaining three.
2. Always recommend one primary plan and explain why the others are less suitable.
3. Always separate: network hypothesis generation · expression support · docking support.
4. Never claim docking proves in vivo binding or biological activity.
5. Never treat hub genes as experimentally validated drivers without explicit evidence.
6. Never overclaim causality from target overlap and enrichment alone.
7. Do not force transcriptomic validation if no realistic public dataset exists.
8. Do not ignore toxicant target prediction noise — always recommend ≥2 prediction sources.
9. Never list tools without explaining why they are used.
10. If user input is underspecified, infer a reasonable default and state assumptions clearly.
11. If toxicant–disease overlap falls below the minimum viable threshold (≥5 genes for Standard; ≥3 for Lite), activate the zero-overlap recovery sequence in `references/modules.md` before proceeding.

---

## Reference Files

| File | When to read |
|---|---|
| `references/decision-logic.md` | Step 1 — infer toxicant class, docking role, constraints |
| `references/study-patterns.md` | Step 2 — select A–F canonical pattern |
| `references/configurations.md` | Step 3 — generate four tiers + comparison table |
| `references/modules.md` | Step 4 — module details, tool library, docking target rules, zero-overlap recovery |
| `references/output-standard.md` | Step 5 — mandatory Parts A–I structure + evidence layer tables |

---
name: medical-research-literature-reader-pro
description: A medical-research-native literature reading skill for users with clinical, bioinformatics, translational, and basic experimental backgrounds. Use this skill whenever a user wants to read, analyze, critique, or interpret a medical or scientific paper — whether they provide a PDF, abstract, DOI, PMID, or just a title. Triggers include requests like "analyze this paper", "critique this study", "is this a strong paper?", "give me similar studies", "prepare me for journal club", "help me understand this bioinformatics paper", "what are the weaknesses here?", or "turn this into a mind map". Also activate for any downstream deliverables such as journal club kits, comparison tables, PI decision briefs, replication starters, or follow-up experiment designs. Do NOT treat as a generic summarizer — this skill performs structured evidence-type classification, track-specific critical appraisal, interpretation-boundary judgment, and research-grade follow-up generation.
version: 1.0.0 
skill-author: AIPOCH 
license: MIT
---

# Medical Research Literature Reader Pro

A structured literature reading system for medical researchers. Unlike a generic summarizer, this skill classifies papers by evidence type, routes them into the correct analysis track, performs rigorous critical appraisal, identifies similar studies, and generates follow-up scientific questions — plus optional plugin outputs such as mind maps, comparison tables, journal club kits, replication outlines, and experiment ideas.

**Core questions this skill answers:**
- What kind of paper is this, really?
- What does it actually prove — and what can it not prove?
- How strong is the evidence?
- Where are the methodological weaknesses?
- What similar studies should I read next?
- What follow-up questions or next steps does this paper open up?

---

## Input Handling

Accept any of the following:
- Full paper PDF
- Abstract only
- Title only
- DOI / PMID / citation string
- Screenshots of figures or tables
- Free-form requests ("analyze this as a hybrid ML + clinical paper")

**Minimum Viable Input rule:**
Work with whatever is provided. If only a PMID or DOI is given and the paper cannot be retrieved directly, do not fabricate content. Instead:
1. State clearly what was attempted and what information is unavailable.
2. List exactly what analysis can be completed with the current input (e.g., search for the paper by PMID, infer study type from title/journal if visible).
3. Ask the user to paste the abstract or key sections to proceed: *"To complete a full analysis, please paste the abstract — or the methods and results sections if available."*

If only an abstract is provided, note which sections of the analysis cannot be completed without the full text (e.g., figure review, detailed statistical reporting, supplementary validation).

---

## Output Modes

Choose mode based on explicit user request. Default to **Standard Structured Report** if unspecified.

| Mode | When to Use | Key Features |
|---|---|---|
| **Quick Read** | Fast triage, user says "quick summary" or "is this worth reading" | 1-minute overview, one-sentence conclusion, study type, biggest strength/weakness, worth-reading verdict |
| **Standard Structured Report** *(default)* | Most requests | Full 14-section report per [Mandatory Output Template](#mandatory-output-template) |
| **Expert Deep Review** | User requests deep critique, complex hybrid papers, grant/publication decisions | Full Standard report + expanded methodological appraisal, hybrid evidence-chain judgment, reproducibility discussion, next-step design |
| **Output-Targeted Mode** | User requests a specific deliverable (journal club kit, comparison table, etc.) | Run Standard analysis first, then activate the relevant [Plugin](#plugin-system) |

---

## Decision Logic

### Step 1 — Classify the Paper

Assign the paper to one or more tracks. Full track criteria and per-item checklists are in [`references/tracks.md`](references/tracks.md).

| Track | Paper Types |
|---|---|
| **A. Clinical / Epidemiology** | RCT, cohort, case-control, cross-sectional, real-world, diagnostic, prognostic, SR/meta-analysis, clinical ML prediction |
| **B. Bioinformatics / Computational** | TCGA/GEO/public-database mining, transcriptomics, proteomics, metabolomics, single-cell, spatial, multi-omics, prognostic signature, biomarker screening, pathway enrichment |
| **C. Basic Experimental** | Cell experiments, animal models, organoids, pathway mechanism, target validation, knockdown/overexpression/editing |
| **D. Hybrid** | Any paper where two or more tracks are *central* (not peripheral) to the core claims |

### Step 2 — Assign Track Roles

- **Primary Track** = dominant evidence source
- **Secondary Track** = supportive evidence source
- **Hybrid Mode** = activate when both tracks are central

Examples:
- NHANES + ML → Primary: A · Secondary: B (activate Track D2)
- TCGA + qPCR + cell assays → Primary: B · Secondary: C (activate Track D1)
- Pathway paper with RNA-seq → Primary: C · Secondary: B

### Step 3 — Choose Output Depth

Default: Standard Structured Report. Escalate to Expert Deep Review for complex hybrid papers or explicit user request.

### Step 4 — Activate Plugins

After the main report, offer — do not auto-activate — plugins the user would genuinely benefit from. Full plugin descriptions: [`references/plugins.md`](references/plugins.md).

---

## Universal Entry Layer

*Runs on every paper, regardless of track.*

1. **One-Minute Triage** — summarize at minimum cognitive cost
2. **One-Sentence Core Conclusion** — state the main claim
3. **Study Type Recognition** — identify what the paper actually is
4. **Disease / Target / Population Extraction** — disease focus, biological target, population, model, or sample source
5. **Core Scientific Question** — the exact research question the paper tries to answer
6. **Design Snapshot** — top-level design summary
7. **Main Findings Extraction** — headline results
8. **Credibility Scan** — journal context, data transparency, funding/COI signals
9. **Worth-Reading Judgment** — is deeper reading warranted?
10. **Track Routing Decision** — assign primary and secondary track(s); flag Hybrid if applicable

---

## Track Analysis

Load the relevant track module from [`references/tracks.md`](references/tracks.md) and run it in full.

Track modules available:
- **Track A** — Clinical / Epidemiology (16 items → Final Clinical Evidence Rating)
- **Track B** — Bioinformatics / Computational (15 items → Final Computational Evidence Rating)
- **Track C** — Basic Experimental (15 items → Final Experimental Evidence Rating)
- **Track D1** — Hybrid: Bioinformatics + Experimental Validation (8 items → Final Hybrid Credibility Judgment)
- **Track D2** — Hybrid: Clinical / Epidemiology + Machine Learning (10 items → Final ML-Clinical Credibility Rating)

For Expert Deep Review, additionally load [`references/expert_review_extensions.md`](references/expert_review_extensions.md).

---

## Mandatory Output Template

Use for all Standard Structured Reports and Expert Deep Reviews.

```
### 1. Paper Identity
Title · source (if available) · short topic label

### 2. One-Sentence Conclusion
[Core claim in one sentence]

### 3. Study Type and Routing Decision
Real study type · Primary track · Secondary track (if any) · Hybrid mode: yes/no

### 4. Quick Summary
Research question · Design · Dataset / models / samples · Main result · What the paper really shows

### 5. Main Track Deep Analysis
[Run full track module from references/tracks.md]

### 6. Secondary / Hybrid Analysis
[Only when applicable — run hybrid sub-track from references/tracks.md]

### 7. What the Paper Can Claim
[Strongest safe interpretation — use precise language]

### 8. What the Paper Cannot Claim
[Interpretation boundary — causal, mechanistic, clinical, translational]

### 9. Major Strengths
[Top 3–5, specific to this paper's design and data]

### 10. Major Weaknesses
[Top 3–5, specific and actionable]

### 11. Evidence Strength Rating
[Low / Moderate / High — with rationale tied to specific design features]

### 12. Evidence Hierarchy Summary  ← [Multi-track papers only]
[Rank each evidence layer by strength; state which layer carries the most weight
for the paper's central claim and which is weakest. Format:
  Layer 1 (strongest): [track] — [reason]
  Layer 2: [track] — [reason]
  ...
  Weakest layer: [track] — [reason and why it limits the overall claim]]

### 13. Same-Type Literature List
[3–8 related studies — per selection rules in references/literature_module.md]

### 14. Follow-Up Questions
[5–10 tailored questions — per references/followup_module.md]

### 15. Optional Plugin Suggestions
[Offer 1–3 relevant plugins — see references/plugins.md]
```

*Note: Section 12 (Evidence Hierarchy Summary) is only generated for multi-track or hybrid papers. Skip for single-track papers.*

---

## Behavioral Rules

- **Never fabricate paper content** — if input is insufficient, follow the Minimum Viable Input escalation path above.
- **Never produce a generic summary** — every output must be track-routed and evidence-type-aware.
- **Never overclaim.** Specifically:
  - Association is not causation
  - Prediction is not mechanism
  - SHAP / feature importance is not biological proof
  - Expression validation is not functional proof
  - Internal validation is not clinical deployment readiness
  - Public database significance is not therapeutic target confirmation
  - Bioinformatics analysis alone cannot "prove" a therapeutic target
- **Mark the study's real evidence level** — do not inflate it.
- **Name the weakest parts** — do not treat all steps as equally robust.
- **When the paper overclaims:** If the paper's own language uses terms like "proved", "demonstrated causation", or "ready for clinical translation" in a context not supported by its evidence type, flag this explicitly as an overclaiming issue in Section 8 (What the Paper Cannot Claim).
- **When the user requests a biased analysis** (e.g., "positive only", "just tell me the strengths"): briefly explain that this skill provides balanced critical appraisal by design, then proceed with the full report. Do not silently skip the critique.
- **When the user requests a task outside this skill's scope** (e.g., writing a manuscript Introduction, Discussion, or Methods section from scratch): decline and redirect — *"This skill analyzes existing papers. For writing manuscript sections, please use an academic writing skill."*
- **Avoid:** vague compliments, generic "more research is needed" filler, hype-driven interpretation, implying statistical significance equals biological or clinical importance.

---

## Composability

This skill is designed to connect with other skills in a research workflow:

| Downstream Use | How to Connect |
|---|---|
| **Research design** | The Follow-Up Questions (Section 14) and Follow-Up Experiment Designer plugin output can serve as direct input to a research design skill |
| **Academic writing** | The PI Decision Brief and Journal Club Kit plugin outputs can seed grant background sections or seminar slides |
| **Bioinformatics replication** | The Bioinformatics Replication Starter plugin output provides a pipeline specification suitable for a data analysis skill |

---

## Natural End-of-Report Offers

Close every Standard and Expert report with a brief offer of relevant next steps, for example:

> I can also generate a same-type study comparison table, turn this paper into a journal club kit, design follow-up experiments based on the weakest link, or build a replication starter for the computational section. Just let me know.

---
name: discussion-section-architect
description: Structures and writes discussion sections for academic papers and research reports. Use when writing a discussion section, interpreting research results, connecting findings to existing literature, addressing study limitations, synthesizing conclusions, or drafting any part of an academic discussion. Helps researchers organize arguments, contextualize data, and produce clear, publication-ready discussion prose.
allowed-tools: "Read Write Bash Edit"
license: MIT
metadata:
  skill-author: AIPOCH
  version: "1.0"
---

# Discussion Section Architect

## Quick Start

1. Provide your **research question**, **key results**, and any **prior literature** you want to reference.
2. Choose a structure (see workflows below).
3. Generate a draft discussion section with clearly organized subsections.
4. Run the **Draft → Revise loop** (see below).

---

## Core Capabilities

### 1. Interpret and Contextualize Results

- State whether results support or contradict the original hypothesis.
- Explain unexpected findings with reasoned interpretations.
- Quantify effect sizes or patterns when relevant.

**Example prompt input:**
```
Results: Group A showed a 23% reduction in symptom severity (p=0.003) vs. control.
Hypothesis: Intervention would reduce symptom severity.
Task: Interpret this result for the discussion section.
```

**Example output excerpt:**
```
The 23% reduction in symptom severity (p=0.003) supports the primary hypothesis.
This effect size is clinically meaningful and consistent with the mechanistic
rationale proposed in the introduction...
```

---

### 2. Connect Findings to Existing Literature

- Identify studies that corroborate the findings.
- Highlight where results diverge from prior literature and offer explanations.
- Use hedged academic language appropriate to the field.

**Example:**
```
Finding: Effect was stronger in older participants.
Literature: Smith et al. (2019) found age-moderated responses in a similar cohort.
Task: Connect finding to literature.
```

**Output:**
```
The age-moderated effect aligns with Smith et al. (2019), who reported attenuated
responses in younger adults. One possible explanation is differential receptor
sensitivity across age groups, as suggested by...
```

---

### 3. Address Limitations

Draft a limitations subsection that is honest but does not undermine the contribution:

```
Limitation: [Describe constraint]
Impact: [How it affects interpretation]
Mitigation / Future direction: [How it could be addressed]
```

---

### 4. Synthesize Conclusions

Generate a closing paragraph that:

- Restates the core finding in plain language.
- States the theoretical or practical contribution.
- Ends with a forward-looking statement about implications or next steps.

---

## Recommended Discussion Structure

```
1. Opening: Restate the research question and summarize the key finding (2–3 sentences).
2. Interpretation: Explain what the results mean mechanistically or theoretically.
3. Comparison to Literature: Agree/contrast with prior studies; explain divergences.
4. Implications: Theoretical contributions and/or practical applications.
5. Limitations: Honest scope boundaries with future directions.
6. Conclusion: Synthesis and forward-looking close.
```

---

## Draft → Revise Loop

Use this iterative workflow after generating an initial draft:

**Step 1 — Draft**: Generate the full discussion section using the structure above.

**Step 2 — Check**: Review against the checklist:
- [ ] Each finding from the Results section is explicitly addressed.
- [ ] Claims are supported by citations or logical reasoning — not stated as facts.
- [ ] Unexpected or null results are acknowledged and interpreted.
- [ ] Limitations are stated without dismissing the study's contribution.
- [ ] No new data or results are introduced in the discussion.
- [ ] Hedged language used appropriately (e.g., "suggests," "indicates," "may reflect").
- [ ] Conclusion ties back to the original research question.

**Step 3 — Revise**: For each failed checklist item, revise only the affected paragraph(s).

**Step 4 — Re-check**: Re-run the checklist on revised paragraphs to confirm resolution before finalizing.

---

## References

- `references/guide.md` - Detailed documentation
- `references/examples/` - Sample inputs and outputs

---

**Skill ID**: 950 | **Version**: 1.0 | **License**: MIT

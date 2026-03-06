---
name: cross-disciplinary-bridge-finder
description: Use when identifying collaboration opportunities across fields, finding experts in complementary disciplines, translating methodologies between scientific domains, or building interdisciplinary research teams. Identifies synergies between scientific disciplines, matches researchers with complementary expertise, and facilitates cross-domain collaborations. Supports interdisciplinary grant applications and innovative research team formation.
allowed-tools: "Read Write Bash Edit"
license: MIT
metadata:
  skill-author: AIPOCH
  version: "1.0"
---

# Cross-Disciplinary Research Collaboration Finder

## When to Use This Skill

- identifying collaboration opportunities across fields
- finding experts in complementary disciplines
- translating methodologies between scientific domains
- building interdisciplinary research teams
- discovering funding for interdisciplinary projects
- mapping knowledge transfer pathways

## Quick Start

```python
from scripts.interdisciplinary import CollaborationFinder

finder = CollaborationFinder()

# Find collaborators in different field
collaborators = finder.find_experts(
    my_expertise="machine_learning",
    target_field="immunology",
    collaboration_type="co_authorship",
    min_publications=10,
    h_index_threshold=15
)

if not collaborators:
    print("No collaborators found — try lowering min_publications or h_index_threshold.")
else:
    # Validate quality before proceeding: only consider complementarity_score > 0.7
    qualified = [e for e in collaborators if e.complementarity_score > 0.7]
    print(f"Found {len(collaborators)} candidates; {len(qualified)} meet quality threshold (score > 0.7):")
    for expert in qualified[:5]:
        print(f"  - {expert.name} ({expert.institution})")
        print(f"    Research: {expert.research_focus}")
        print(f"    Complementarity score: {expert.complementarity_score}")

# Identify transferable methods
methods = finder.identify_transferable_methods(
    from_field="physics",
    to_field="biology",
    application_area="systems_modeling"
)

if not methods:
    print("No transferable methods found — consider broadening the application_area.")
else:
    # Validate applicability before proceeding: review transfer_potential
    for method in methods:
        print(f"Method: {method.name}")
        print(f"  Success in source field: {method.success_rate}")
        print(f"  Application potential: {method.transfer_potential}")
        if method.transfer_potential < 0.6:
            print(f"  ⚠ Low transfer potential — consider a different application_area.")

# Find interdisciplinary funding
grants = finder.find_interdisciplinary_funding(
    fields=["AI", "medicine", "ethics"],
    funder_types=["NIH", "NSF", "private_foundation"],
    deadline_within_months=6
)

if not grants:
    print("No grants found — try extending deadline_within_months or broadening funder_types.")

# Generate collaboration proposal outline
proposal_outline = finder.generate_collaboration_proposal(
    partner_expertise="clinical_trial_design",
    my_expertise="data_science",
    research_question="precision_medicine"
)
```

## Command Line Usage

```bash
python scripts/main.py --my-field machine_learning --target-field immunology --find-collaborators --output matches.json
```

## Handling Poor Results

- **Empty collaborator list**: Lower `min_publications` or `h_index_threshold`; broaden `collaboration_type`.
- **No transferable methods**: Widen `application_area` to a higher-level domain (e.g., `"modeling"` instead of `"systems_modeling"`).
- **No funding results**: Extend `deadline_within_months` or add more entries to `funder_types`.
- **Weak proposal outline**: Ensure `research_question` is a descriptive string rather than a short keyword.

## References

- `references/guide.md` - Comprehensive user guide
- `references/examples/` - Working code examples
- `references/api-docs/` - Complete API documentation

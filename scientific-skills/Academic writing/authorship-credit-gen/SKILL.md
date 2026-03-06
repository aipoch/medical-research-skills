---
name: authorship-credit-gen
description: Use when determining author order on research manuscripts, assigning CRediT contributor roles for transparency, documenting individual contributions to collaborative projects, or resolving authorship disputes in multi-institutional research. Generates fair and transparent authorship assignments following ICMJE guidelines and CRediT taxonomy. Helps research teams document contributions, resolve disputes, and ensure equitable credit distribution in academic publications.
allowed-tools: "Read Write Bash Edit"
license: MIT
metadata:
  skill-author: AIPOCH
  version: "1.0"
---

# Research Authorship and Contributor Credit Generator

## When to Use This Skill

- determining author order on research manuscripts
- assigning CRediT contributor roles for transparency
- documenting individual contributions to collaborative projects
- resolving authorship disputes in multi-institutional research
- preparing contributor statements for journal submissions
- evaluating contribution equity in research teams

## Quick Start

```python
from scripts.main import AuthorshipCreditGen

# Initialize the tool
tool = AuthorshipCreditGen()

from scripts.authorship_credit import AuthorshipCreditGenerator

generator = AuthorshipCreditGenerator(guidelines="ICMJEv4")

# Document contributions
contributions = {
    "Dr. Sarah Chen": [
        "Conceptualization",
        "Methodology", 
        "Writing - Original Draft",
        "Supervision"
    ],
    "Dr. Michael Roberts": [
        "Data Curation",
        "Formal Analysis",
        "Writing - Review & Editing"
    ],
    "Dr. Lisa Zhang": [
        "Investigation",
        "Resources",
        "Validation"
    ]
}

# Generate fair authorship order
authorship = generator.determine_order(
    contributions=contributions,
    criteria=["intellectual_input", "execution", "writing", "supervision"],
    weights={"intellectual_input": 0.4, "execution": 0.3, "writing": 0.2, "supervision": 0.1}
)

print(f"First author: {authorship.first_author}")
print(f"Corresponding: {authorship.corresponding_author}")
print(f"Author order: {authorship.ordered_list}")

# Generate CRediT statement
credit_statement = generator.generate_credit_statement(
    contributions=contributions,
    format="journal_submission"
)

# Check for disputes
dispute_check = generator.check_equity_issues(authorship)
if dispute_check.has_issues:
    print(f"Recommendations: {dispute_check.recommendations}")
```

## Core Capabilities

### 1. Generate Fair Authorship Orders

Analyze contributions using weighted criteria to determine equitable author ranking.

```python
# Define weighted contribution criteria
weights = {
    "conceptualization": 0.25,
    "methodology_design": 0.20,
    "data_collection": 0.15,
    "analysis": 0.15,
    "manuscript_writing": 0.15,
    "supervision": 0.10
}

# Calculate contribution scores
scores = tool.calculate_contribution_scores(
    contributions=team_contributions,
    weights=weights
)

# Generate ordered author list
authorship_order = tool.generate_author_order(scores)
print(f"Recommended order: {authorship_order}")
```

### 2. Assign CRediT Roles

Map contributions to official CRediT (Contributor Roles Taxonomy) categories.

```python
# Map contributions to CRediT roles
credit_roles = tool.assign_credit_roles(
    contributions=contributions,
    version="CRediT_2021"
)

# Generate CRediT statement for journal
statement = tool.generate_credit_statement(
    roles=credit_roles,
    format="JATS_XML"
)

# Validate role assignments
validation = tool.validate_credit_roles(credit_roles)
if validation.is_valid:
    print("CRediT roles properly assigned")
```

### 3. Detect Contribution Inequities

Identify potential authorship disputes before submission.

```python
# Analyze contribution distribution
equity_analysis = tool.analyze_equity(
    contributions=contributions,
    thresholds={"min_substantial": 0.15}
)

# Flag potential issues
if equity_analysis.has_inequities:
    for issue in equity_analysis.issues:
        print(f"Warning: {issue.description}")
        print(f"Recommendation: {issue.recommendation}")

# Generate equity report
report = tool.generate_equity_report(equity_analysis)
```

### 4. Generate Journal-Ready Statements

Create formatted contributor statements for various journal requirements.

```python
# Generate for Nature-style statement
nature_statement = tool.generate_contributor_statement(
    style="Nature",
    include_competing_interests=True
)

# Generate for Science-style statement  
science_statement = tool.generate_contributor_statement(
    style="Science",
    include_author_contributions=True
)

# Export in multiple formats
tool.export_statement(
    statement=nature_statement,
    formats=["docx", "pdf", "txt"]
)
```

## Command Line Usage

```bash
python scripts/main.py --contributions contributions.json --guidelines ICMJE --output authorship_order.json
```

## Best Practices

- Discuss authorship expectations at project inception
- Document contributions continuously throughout project
- Review and agree on author order before submission
- Include non-author contributors in acknowledgments

## Quality Checklist

Before using this skill, ensure you have:
- [ ] Clear understanding of your objectives
- [ ] Necessary input data prepared and validated
- [ ] Output requirements defined
- [ ] Reviewed relevant documentation

After using this skill, verify:
- [ ] Results meet your quality standards
- [ ] Outputs are properly formatted
- [ ] Any errors or warnings have been addressed
- [ ] Results are documented appropriately

## References

- `references/guide.md` - Comprehensive user guide
- `references/examples/` - Working code examples
- `references/api-docs/` - Complete API documentation

---

**Skill ID**: 766 | **Version**: 1.0 | **License**: MIT

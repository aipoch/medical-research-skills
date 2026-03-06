---
name: citation-formatter
description: Use when formatting references for journal submission, converting between citation styles (APA, MLA, Vancouver, Chicago), generating bibliographies for manuscripts, or ensuring consistent reference formatting. Automatically formats citations and bibliographies in 1000+ academic styles. Ensures reference accuracy, completeness, and compliance with journal requirements. Supports batch conversion and integration with reference managers.
allowed-tools: "Read Write Bash Edit"
license: MIT
metadata:
  skill-author: AIPOCH
  version: "1.0"
---

# Academic Citation Style Formatter and Converter

## When to Use This Skill

- formatting references for journal submission
- converting between citation styles (APA, MLA, Vancouver, Chicago)
- generating bibliographies for manuscripts
- ensuring consistent reference formatting
- checking reference completeness and accuracy
- preparing grant proposal reference sections

## Quick Start

```python
from scripts.main import CitationFormatter

# Initialize the tool
tool = CitationFormatter()

from scripts.citation_formatter import CitationFormatter

formatter = CitationFormatter()

# Format references for specific journal
formatted_refs = formatter.format_references(
    references=raw_references,
    target_style="Nature Medicine",
    output_format="docx"
)

# Convert between styles
converted = formatter.convert_style(
    bibliography=apa_bibliography,
    from_style="APA 7th",
    to_style="Vancouver",
    include_doi=True,
    include_pmids=True
)

# Validate reference completeness
validation = formatter.validate_references(
    references=reference_list,
    required_fields=["authors", "title", "journal", "year", "volume", "pages", "doi"]
)

print(f"Validation results:")
print(f"  Complete: {validation.complete_count}")
print(f"  Missing fields: {validation.incomplete_count}")
print(f"  Invalid DOIs: {len(validation.invalid_dois)}")

# Generate in-text citations
in_text = formatter.generate_in_text_citations(
    citations=[
        {"author": "Smith", "year": 2023, "type": "paren"},
        {"author": "Jones et al.", "year": 2022, "type": "narrative"}
    ],
    style="APA"
)

# Batch process multiple documents
batch_results = formatter.batch_format(
    files=["chapter1.docx", "chapter2.docx"],
    style="AMA",
    output_dir="formatted/"
)
```

## Core Capabilities

### 1. Format citations in 1000+ academic styles

```python
# Format functionality
result = tool.execute(data)
```

### 2. Convert seamlessly between citation formats

```python
# Convert functionality
result = tool.execute(data)
```

### 3. Validate reference completeness and accuracy

```python
# Validate functionality
result = tool.execute(data)
```

### 4. Batch process large reference collections

```python
# Batch functionality
result = tool.execute(data)
```

## Command Line Usage

```bash
python scripts/main.py --input references.bib --from-style APA --to-style Vancouver --output formatted.docx --validate
```

## Best Practices

- Always validate DOIs and URLs before submission
- Check journal-specific requirements beyond standard style
- Maintain original reference database for updates
- Review formatting of special cases (websites, preprints)

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

**Skill ID**: 625 | **Version**: 1.0 | **License**: MIT

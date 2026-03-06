---
name: key-takeaways
description: Extracts and summarizes key takeaways from documents, meeting notes, articles, and other text content. Use when the user asks for summaries, bullet points, main points, highlights, or a TL;DR of any document or body of text. Produces structured outputs such as numbered lists, executive summaries, and action items. Supports configurable output formats including JSON export for downstream use.
allowed-tools: "Read Write Bash Edit"
license: MIT
metadata:
  skill-author: AIPOCH
  version: "1.0"
---

# Key Takeaways

Extracts and presents the most important points from any body of text — meeting notes, articles, reports, or documents — as concise, structured takeaways. Supports multiple output formats and is configurable for audience or depth.

## Quick Start

```python
from scripts.main import Key_Takeaways

# Initialize
tool = Key_Takeaways()

# Extract key takeaways from a document
result = tool.process("meeting_notes.txt")

# Export as structured JSON
tool.export(result, format="json")
```

## Core Capabilities

### 1. Extract key points from text

```python
# Read source document and extract top takeaways
result = tool.process("quarterly_report.txt")
# Returns: [{"point": "Revenue grew 12% YoY", "source_line": 4}, ...]
```

### 2. Generate structured summaries

```python
# Generate a bullet-point executive summary
result = tool.process("meeting_notes.txt", style="executive")
# Returns: {"summary": "...", "action_items": [...], "decisions": [...]}
```

### 3. Configure output depth and audience

```python
# Adjust number of takeaways and target audience
result = tool.process("article.txt", max_points=5, audience="non-technical")
```

### 4. Export results

```python
# Export takeaways to JSON or plain text
tool.export(result, format="json", output_path="takeaways.json")
tool.export(result, format="txt",  output_path="takeaways.txt")
```

## CLI Usage

```bash
# Extract key takeaways from a file
python scripts/main.py --input document.txt --output takeaways.txt

# Use a config file to set depth, audience, and format
python scripts/main.py --input document.txt --config config.json --verbose

# Batch process a directory of documents
python scripts/main.py --batch input_dir/ --output output_dir/
```

**Batch processing notes:**
- Verify the output directory exists before running: `mkdir -p output_dir/`
- If processing fails on an individual file, the tool logs the error and continues with remaining files; review `output_dir/errors.log` after the run
- After batch completion, validate all JSON outputs: `for f in output_dir/*.json; do python -m json.tool "$f" > /dev/null && echo "OK: $f" || echo "FAIL: $f"; done`

## Example Input / Output

**Input** (`meeting_notes.txt`):
```
Q3 review: Sales up 15%. New product launch delayed to Q4.
Action: Alice to update roadmap by Friday. Budget approved for hiring.
```

**Output** (`takeaways.json`):
```json
{
  "key_points": [
    "Sales increased 15% in Q3",
    "Product launch rescheduled to Q4"
  ],
  "action_items": [
    "Alice to update roadmap by Friday"
  ],
  "decisions": [
    "Budget approved for hiring"
  ]
}
```

## Quality Checklist

- [ ] Source text is readable and complete before processing
- [ ] Output point count matches configured `max_points` setting
- [ ] Action items and decisions are separated from general observations
- [ ] Exported file opens and validates correctly (e.g., `python -m json.tool takeaways.json`)
  - If JSON validation fails, check source file encoding (UTF-8 expected) and re-run; inspect `--verbose` output for parsing errors
- [ ] Results reviewed against original source for accuracy

## References

- `references/guide.md` - Detailed documentation
- `references/examples/` - Sample inputs and outputs

---

**Skill ID**: 308 | **Version**: 1.0 | **License**: MIT

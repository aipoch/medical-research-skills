---
name: scientific-schematics
description: Automates publication-quality scientific diagrams (e.g., flowcharts, architectures, pathways) when you need journal/poster-ready visuals from a natural-language description.
license: MIT
author: AIPOCH
---
> **Source**: [https://github.com/aipoch/medical-research-skills](https://github.com/aipoch/medical-research-skills)

# Scientific Schematics Skill

## When to Use
- Creating **journal-ready** figures (clean typography, consistent styling, high resolution) from a short textual description.
- Producing **poster-friendly** diagrams that prioritize readability at distance (larger labels, stronger contrast).
- Drafting **neural network architecture** schematics (e.g., Transformer blocks, attention modules) for papers or slides.
- Generating **biological pathway** visuals (e.g., Krebs cycle) with iterative quality review.
- Rapidly iterating on a diagram concept when you need **AI-assisted refinement loops** instead of manual redraws.

## Key Features
- **Text-to-diagram automation**: Converts a natural-language prompt into a publication-quality schematic.
- **Iterative generate → review → refine loop**: Automatically improves the figure until a quality threshold is met.
- **Document-type aware critique**: Reviewer feedback adapts to `journal` vs `poster` requirements.
- **Model-configurable pipeline**: Choose separate LLMs for generation and vision-based review.
- **Output validation**: Performs final checks (e.g., resolution/accessibility considerations) before saving to `figures/`.
- Reference guidance:
  - Best practices: `references/best_practices.md`
  - Supported diagram categories: `references/diagram_types.md`

## Dependencies
- Python 3.10+ (recommended)
- Python packages:
  - `pillow` (PIL)
  - `matplotlib`
  - `requests`
- Environment:
  - `OPENROUTER_API_KEY` (required)

## Example Usage
### 1) Set the OpenRouter API key
**Windows (PowerShell)**
```powershell
$env:OPENROUTER_API_KEY="your_key_here"
```

**Linux/macOS**
```bash
export OPENROUTER_API_KEY="your_key_here"
```

### 2) Run the generator (journal/poster)
```bash
python scripts/generate_schematic.py "Transformer architecture with attention mechanism" --doc-type journal
```

### 3) Override the generation model
```bash
python scripts/generate_schematic.py "Krebs cycle" --doc-type journal --generator anthropic/claude-3.5-sonnet
```

### 4) (Optional) Override both generator and reviewer
```bash
python scripts/generate_schematic.py "Flowchart of a clinical trial enrollment pipeline" \
  --doc-type poster \
  --generator google/gemini-3.6-flash \
  --reviewer google/gemini-3.6-flash
```

## Implementation Details
### Pipeline Stages
1. **Generation**
   - A code-capable LLM converts the prompt into a diagram image.
   - Default generator model: `google/gemini-3.6-flash`.

2. **Review**
   - A vision-capable LLM evaluates the generated image against the target `--doc-type`.
   - Default reviewer model: `google/gemini-3.6-flash`.
   - The reviewer returns actionable critique and a numeric quality score.

3. **Refinement Loop**
   - If the score is below the acceptance threshold (e.g., **8.5/10**), the system re-enters generation using the reviewer’s feedback as constraints.
   - This repeats until the threshold is met or the run terminates by internal stopping conditions.

4. **Finalization**
   - Performs final checks such as **resolution suitability** and **accessibility-oriented considerations** (e.g., legibility).
   - Saves the final artifact to the `figures/` directory.

### Key Parameters
- `--doc-type <journal|poster>`: Controls review criteria (e.g., density/precision for journals vs readability/scale for posters).
- `--generator <model_id>`: Model used to produce the diagram.
- `--reviewer <model_id>`: Model used to critique the diagram.
- **Quality threshold**: A numeric cutoff (example: `8.5/10`) that determines whether refinement continues.
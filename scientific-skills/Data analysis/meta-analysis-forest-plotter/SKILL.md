---
name: meta-analysis-forest-plotter
description: Use when creating forest plots for meta-analyses, visualizing effect sizes across studies, or generating publication-ready meta-analysis figures. Produces high-quality forest plots with confidence intervals, heterogeneity metrics, and subgroup analyses.
allowed-tools: "Read Write Bash Edit"
license: MIT
metadata:
  skill-author: AIPOCH
  version: "1.0"
---

# Meta-Analysis Forest Plot Generator

Create publication-ready forest plots for systematic reviews and meta-analyses with customizable styling and statistical annotations.

## Quick Start

```python
from scripts.forest_plotter import ForestPlotter

plotter = ForestPlotter()

# Generate forest plot
plot = plotter.create_plot(
    studies=["Study A", "Study B", "Study C"],
    effect_sizes=[1.2, 0.8, 1.5],
    ci_lower=[0.9, 0.5, 1.1],
    ci_upper=[1.5, 1.1, 1.9],
    overall_effect=1.15
)
```

## Core Capabilities

### 1. Basic Forest Plot

```python
fig = plotter.plot(
    data=studies_df,
    effect_col="HR",
    ci_lower_col="CI_lower",
    ci_upper_col="CI_upper",
    study_col="study_name"
)
```

**Required Data Columns:**
- Study name/identifier
- Effect size (OR, HR, RR, MD, etc.)
- Confidence interval lower bound
- Confidence interval upper bound
- Weight (optional, for precision)

### 2. Statistical Annotations

```python
fig = plotter.plot_with_stats(
    data,
    heterogeneity_stats={
        "I2": 45.2,
        "p_value": 0.03,
        "Q_statistic": 18.4
    },
    overall_effect={
        "estimate": 1.15,
        "ci": [0.98, 1.35],
        "p_value": 0.08
    }
)
```

**Heterogeneity Metrics:**
| Metric | Interpretation |
|--------|---------------|
| I² < 25% | Low heterogeneity |
| I² 25-50% | Moderate heterogeneity |
| I² > 50% | High heterogeneity |
| Q p-value < 0.05 | Significant heterogeneity |

### 3. Subgroup Analysis

```python
fig = plotter.subgroup_plot(
    data,
    subgroup_col="treatment_type",
    subgroups=["Surgery", "Radiation", "Combined"]
)
```

### 4. Custom Styling

```python
fig = plotter.plot(
    data,
    style="publication",
    journal="lancet",  # or "nejm", "jama", "nature"
    color_scheme="monochrome",
    show_weights=True
)
```

## CLI Usage

```bash
# From CSV data
python scripts/forest_plotter.py \
  --input meta_analysis_data.csv \
  --effect-col OR \
  --output forest_plot.pdf

# With custom styling
python scripts/forest_plotter.py \
  --input data.csv \
  --style lancet \
  --width 8 --height 10
```

## Output Formats

- **PDF**: Publication quality, vector graphics
- **PNG**: Web/presentation, 300 DPI
- **SVG**: Editable in Illustrator/Inkscape
- **TIFF**: Journal submission format

## References

- `references/forest-plot-styles.md` - Journal-specific formatting
- `examples/sample-plots/` - Example outputs

---

**Skill ID**: 207 | **Version**: 1.0 | **License**: MIT

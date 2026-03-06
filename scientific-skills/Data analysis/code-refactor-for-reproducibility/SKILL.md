---
name: code-refactor-for-reproducibility
description: Use when refactoring research code for publication, adding documentation to existing analysis scripts, creating reproducible computational workflows, or preparing code for sharing with collaborators. Transforms research code into publication-ready, reproducible workflows. Adds documentation, implements error handling, creates environment specifications, and ensures computational reproducibility for scientific publications.
allowed-tools: "Read Write Bash Edit"
license: MIT
metadata:
  skill-author: AIPOCH
  version: "1.0"
---

# Research Code Reproducibility Refactoring Tool

## Workflow Overview

Follow this sequence when refactoring a research codebase:

1. **Analyze** — identify reproducibility issues in existing code
2. **Refactor** — apply documentation, parameterization, and error handling
3. **Specify environment** — pin dependencies and create environment files
4. **Validate** — run tests and verify behaviour is unchanged

---

## Step 1: Analyze Code for Reproducibility Issues

Read each source file and check for the following problems. Document findings before making any changes.

**Checklist:** missing docstrings · hardcoded absolute paths · missing random seeds · bare `except:` clauses · unpinned imports · unexplained magic numbers

**Example — detecting issues manually:**

```python
import ast, pathlib

def find_hardcoded_paths(source: str) -> list[str]:
    """Return string literals that look like absolute paths."""
    tree = ast.parse(source)
    return [
        node.s for node in ast.walk(tree)
        if isinstance(node, ast.Constant)
        and isinstance(node.s, str)
        and node.s.startswith("/")
    ]

source = pathlib.Path("analysis.py").read_text()
print(find_hardcoded_paths(source))
```

---

## Step 2: Refactor for Best Practices

Apply improvements in place. Always back up originals first.

### 2a. Add docstrings

```python
# Before
def load_data(path):
    import pandas as pd
    return pd.read_csv(path)

# After
def load_data(path: str) -> "pd.DataFrame":
    """Load a CSV dataset from disk.

    Parameters
    ----------
    path : str
        Path to the CSV file (relative to project root).

    Returns
    -------
    pd.DataFrame
        Raw dataset with original column names preserved.
    """
    import pandas as pd
    return pd.read_csv(path)
```

### 2b. Parameterize hardcoded values

```python
from pathlib import Path
import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", type=Path, default=Path("data/raw.csv"))
    parser.add_argument("--output", type=Path, default=Path("results/"))
    return parser.parse_args()

args = parse_args()
df = pd.read_csv(args.data)
args.output.mkdir(parents=True, exist_ok=True)
```

### 2c. Set random seeds

```python
import random
import numpy as np

SEED = 42  # document this constant at module level

random.seed(SEED)
np.random.seed(SEED)

# scikit-learn
from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier(random_state=SEED)

# PyTorch
import torch
torch.manual_seed(SEED)
torch.backends.cudnn.deterministic = True
```

### 2d. Add error handling and logging

```python
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)

def load_data(path: Path) -> "pd.DataFrame":
    """Load dataset with validation."""
    import pandas as pd
    if not path.exists():
        raise FileNotFoundError(f"Data file not found: {path}")
    logger.info("Loading data from %s", path)
    df = pd.read_csv(path)
    if df.empty:
        raise ValueError(f"Loaded dataframe is empty: {path}")
    logger.info("Loaded %d rows, %d columns", *df.shape)
    return df
```

---

## Step 3: Generate Environment Specifications

See `references/environment-setup.md` for full Dockerfile and Conda environment templates.

### requirements.txt (pip)

```bash
pip install pipreqs
pipreqs src/ --output requirements.txt --force
```

Verify resolution:
```bash
python -m venv .venv_test && source .venv_test/bin/activate
pip install -r requirements.txt
python -c "import pandas, numpy, sklearn"
deactivate && rm -rf .venv_test
```

### environment.yml (Conda)

```yaml
name: my-research-env
channels:
  - conda-forge
  - defaults
dependencies:
  - python=3.9
  - numpy=1.24.3
  - pandas=2.0.1
  - scikit-learn=1.2.2
  - matplotlib=3.7.1
  - pip:
    - some-pip-only-package==0.5.0
```

```bash
conda env create -f environment.yml
conda activate my-research-env
```

---

## Step 4: Create Documentation

### README structure

Generate a `README.md` containing at minimum:

```markdown
## Requirements
<!-- List Python version and key packages with versions -->

## Installation
```bash
conda env create -f environment.yml
conda activate my-research-env
```

## Data
<!-- Describe input data format, source, and where to place files -->

## Running the Analysis
```bash
python main.py --data data/raw.csv --output results/
```

## Expected Outputs
<!-- Describe files created and how to interpret them -->

## Reproducing Results
- Random seed: 42 (set in `config.py`)
- Hardware: results validated on CPU; GPU results may differ slightly
```

---

## Step 5: Validate Reproducibility

After all changes, verify that behaviour is unchanged:

```bash
# 1. Run the full pipeline and capture output checksums
python main.py --data data/raw.csv --output results/
md5sum results/*.csv > checksums_refactored.md5
diff checksums_original.md5 checksums_refactored.md5

# 2. Run unit tests
pytest tests/ -v --tb=short

# 3. Confirm determinism across two clean runs
python main.py --output results_run1/
python main.py --output results_run2/
diff -r results_run1/ results_run2/
```

**Reproducibility verification checklist:**
- [ ] Output checksums match pre-refactor baseline
- [ ] All tests pass
- [ ] Pipeline runs twice and produces identical outputs
- [ ] `requirements.txt` / `environment.yml` installs cleanly in a fresh environment
- [ ] No absolute paths remain in source files
- [ ] Random seeds are set and documented
- [ ] All public functions have docstrings
- [ ] README contains complete reproduction instructions

---

## Best Practices Summary

| Practice |
|---|
| Relative paths only |
| Pin dependency versions |
| Set random seeds |
| Docstrings on all public functions |
| Validate outputs against a baseline |
| Automate environment setup |

## References

- `references/guide.md` — Comprehensive user guide
- `references/environment-setup.md` — Dockerfile and full environment templates
- `references/examples/` — Working code examples
- `references/api-docs/` — Complete API documentation

---

**Skill ID**: 455 | **Version**: 1.0 | **License**: MIT

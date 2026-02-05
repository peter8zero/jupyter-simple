# UK Defined Benefit Pension Specification Templates

Simple Jupyter notebook templates for documenting pension calculation specifications.

## What's Included

| File | Purpose |
|------|---------|
| `active_to_retirement_spec.ipynb` | Active member retiring directly from service |
| `active_to_deferred_spec.ipynb` | Active member leaving with a deferred pension |
| `deferred_retirement_spec.ipynb` | Deferred member taking pension at retirement |
| `QUICK_START.md` | How to use the templates (includes cheat sheets) |
| `_quarto.yml` | Quarto config for rendering to HTML/PDF/Word |

## Requirements

- Python 3.8+
- VS Code with Jupyter extension
- Quarto (for rendering to PDF/HTML/Word)

```bash
pip install jupyter
```

Install Quarto from: https://quarto.org/docs/get-started/

For version control (optional):
```bash
pip install jupytext
```

## Quick Start

1. Open `deferred_retirement_spec.ipynb` in VS Code
2. Edit the input values in the first code cell
3. Click **Run All** to see calculation results
4. Render with Quarto when ready to share (see below)

## How It Works

Each notebook combines:
- **Markdown cells** — Documentation and explanations
- **Code cells** — Simple formulas that execute

The code is just basic arithmetic:
```python
excess = pension - gmp
revalued = excess * (1 + rate) ** years
```

## Rendering with Quarto

Render individual notebooks:
```bash
quarto render active_to_retirement_spec.ipynb          # HTML (default)
quarto render active_to_retirement_spec.ipynb --to pdf
quarto render active_to_retirement_spec.ipynb --to docx
```

Render all notebooks in the project:
```bash
quarto render
```

Output files go to the `_output/` folder. The `_quarto.yml` file configures:
- Table of contents
- Section numbering
- Consistent styling across all specs
- Code execution on render

## Version Control with Jupytext

To get clean Git diffs, pair notebooks with Python files:

```bash
jupytext --set-formats ipynb,py:percent deferred_retirement_spec.ipynb
```

Then commit only the `.py` files. See `QUICK_START.md` for details.

## Templates

- [x] Active to retirement
- [x] Active to deferred
- [x] Deferred to retirement
- [ ] Transfer values *(coming soon)*
- [ ] Death benefits *(coming soon)*

## Template Workflow

```
Active Member
    │
    ├──► Retires directly ──► active_to_retirement_spec.ipynb
    │
    └──► Leaves early ──► active_to_deferred_spec.ipynb
                                    │
                                    ▼
                          Deferred Member
                                    │
                                    └──► Retires ──► deferred_retirement_spec.ipynb
```

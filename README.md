# UK Defined Benefit Pension Specification Templates

Simple Jupyter notebook templates for documenting pension calculation specifications.

## What's Included

| File | Purpose |
|------|---------|
| `active_to_retirement_spec.ipynb` | Active member retiring directly from service |
| `active_to_deferred_spec.ipynb` | Active member leaving with a deferred pension |
| `deferred_retirement_spec.ipynb` | Deferred member taking pension at retirement |
| `QUICK_START.md` | How to use the templates (includes cheat sheets) |

## Requirements

- Python 3.8+
- VS Code with Jupyter extension

```bash
pip install jupyter
```

For version control (optional):
```bash
pip install jupytext
```

## Quick Start

1. Open `deferred_retirement_spec.ipynb` in VS Code
2. Edit the input values in the first code cell
3. Click **Run All** to see calculation results
4. Export to PDF/HTML when ready to share

## How It Works

Each notebook combines:
- **Markdown cells** — Documentation and explanations
- **Code cells** — Simple formulas that execute

The code is just basic arithmetic:
```python
excess = pension - gmp
revalued = excess * (1 + rate) ** years
```

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

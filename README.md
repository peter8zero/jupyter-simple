# Executable Calculation Specifications

Write calculation specs that actually run. Test your logic before handoff. No more ambiguous Word documents.

## What Is This?

Jupyter notebook templates for documenting calculations as **executable specifications**. Instead of writing formulas in Word that nobody can test, you write specs that run with real data and prove they work.

Perfect for:
- Pension benefit calculations
- Financial calculations
- Any business logic that needs clear documentation

## Getting Started

| Step | What to do |
|------|------------|
| 1 | Read **[QUICK_START.md](QUICK_START.md)** — install and run in 5 minutes |
| 2 | Open **TEMPLATE_starter_spec.ipynb** — practice with the generic template |
| 3 | Read **GUIDE_building_calc_specs.ipynb** — learn to build your own specs |

## What's Included

### Documentation

| File | Purpose |
|------|---------|
| [QUICK_START.md](QUICK_START.md) | Install and run your first spec in 5 minutes |
| GUIDE_building_calc_specs.ipynb | Complete tutorial + FAQ + cheat sheets |

### Templates

| Template | Use for |
|----------|---------|
| **TEMPLATE_starter_spec.ipynb** | Any calculation (start here for practice) |
| active_to_retirement_spec.ipynb | Pension: active member retiring |
| active_to_deferred_spec.ipynb | Pension: active member leaving early |
| deferred_retirement_spec.ipynb | Pension: deferred member retiring |

### Configuration

| File | Purpose |
|------|---------|
| _quarto.yml | Rendering settings for PDF/HTML/Word output |

## Requirements

- Python 3.8+
- VS Code with Jupyter extension
- Quarto (for PDF/HTML/Word export)

## 30-Second Install

1. Install [VS Code](https://code.visualstudio.com/), [Python](https://www.python.org/downloads/), and [Quarto](https://quarto.org/docs/get-started/)
2. In VS Code, install the **Jupyter** and **Quarto** extensions
3. Open any `.ipynb` file and click **Run All**

See [QUICK_START.md](QUICK_START.md) for detailed setup.

## How It Works

```
┌─────────────────────────────────────────────────────────┐
│  Markdown Cell                                          │
│  "Step 1: Calculate the revalued pension"               │
│  Formula: revalued = original × (1 + rate)^years        │
└─────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────┐
│  Code Cell                                              │
│  revalued = original * (1 + rate) ** years              │
│  print(f"Revalued pension: £{revalued:,.2f}")          │
└─────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────┐
│  Output                                                 │
│  Revalued pension: £17,958.56                          │
└─────────────────────────────────────────────────────────┘
```

Documentation and calculation in one place. Change inputs, re-run, see results instantly.

## Pension Template Workflow

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

## Rendering Output

Convert notebooks to shareable documents:

```bash
quarto render TEMPLATE_starter_spec.ipynb --to pdf    # PDF
quarto render TEMPLATE_starter_spec.ipynb --to html   # HTML
quarto render TEMPLATE_starter_spec.ipynb --to docx   # Word
quarto render                                          # All notebooks
```

Or press `Ctrl+Shift+K` in VS Code.

## Why This Approach?

| Traditional Spec | Executable Spec |
|------------------|-----------------|
| Formulas are static text | Formulas actually run |
| Test manually (or not at all) | Click Run All to test |
| Bugs found in development | Bugs found while writing |
| Ambiguous prose | Precise code |
| Developer has questions | Logic is proven |

See the FAQ section in the GUIDE for detailed answers to common concerns.

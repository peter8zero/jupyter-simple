# Simple Jupyter Notebooks for Pension Specs

## Why This Works

- **Markdown cells** = Documentation (like Word)
- **Code cells** = Calculator (like Excel formulas)
- **Run cells** = See results instantly

## Setup (one time)

1. Install VS Code: https://code.visualstudio.com/
2. Install Python: https://www.python.org/downloads/
3. In VS Code, install the "Jupyter" extension (click Extensions icon, search "Jupyter")

## Using the Template

### Opening
- Open VS Code
- File → Open → select the `.ipynb` file

### The Two Types of Cells

**Markdown cells** (documentation):
- Double-click to edit
- Press `Shift+Enter` to save and move on

**Code cells** (calculations):
- Click to select
- Edit the numbers
- Press `Shift+Enter` to run and see results

### Running the Calculation

1. Edit the member data in the first code cell:
   ```python
   pension_at_leaving = 15000.00   # Change this
   gmp_at_leaving = 3500.00        # Change this
   years_of_revaluation = 7        # Change this
   years_early = 3                 # Change this
   gender = "M"                    # M or F
   ```

2. Click "Run All" at the top (or press `Shift+Enter` on each cell)

3. See results at the bottom

### The Code is Just Arithmetic

This:
```python
excess_at_leaving = pension_at_leaving - gmp_at_leaving
```

Is the same as this Excel formula:
```
=B2-B3
```

Just with names instead of cell references.

## Key Shortcuts

| Action | Shortcut |
|--------|----------|
| Run cell and move to next | `Shift+Enter` |
| Run cell and stay | `Ctrl+Enter` |
| Run all cells | Click "Run All" button |
| Add cell below | `B` (when cell selected) |
| Delete cell | `DD` (press D twice) |
| Change to Markdown | `M` |
| Change to Code | `Y` |

## Exporting

- **To PDF**: File → Export → PDF
- **To HTML**: File → Export → HTML

## Tips

1. **Test different scenarios** by changing the input values and re-running
2. **Add notes** by inserting new Markdown cells
3. **The code builds on itself** - run cells in order from top to bottom

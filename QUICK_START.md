# Quick Start

Get up and running in 5 minutes.

---

## 1. Install (one time)

- [ ] **VS Code**: https://code.visualstudio.com/
- [ ] **Python 3.8+**: https://www.python.org/downloads/
- [ ] **Quarto**: https://quarto.org/docs/get-started/

Then in VS Code, install these extensions (click the Extensions icon in the sidebar):
- [ ] **Jupyter**
- [ ] **Quarto**

**For PDF export**, run this once in your terminal:
```bash
quarto install tinytex
```

---

## 2. Open a Template

1. Open VS Code
2. **File → Open Folder** → select the `jupyter-simple` folder
3. Open `TEMPLATE_starter_spec.ipynb` (or any `.ipynb` file)

You should see a mix of formatted text (Markdown cells) and code cells.

---

## 3. Run the Calculation

Click **Run All** at the top of the notebook (or in the `...` menu).

All code cells will execute and show their output. The calculation runs top-to-bottom.

---

## 4. Edit and Re-run

1. Find the **Inputs** code cell (usually near the top)
2. Change some values:
   ```python
   principal = 25000.00    # Change this number
   rate = 0.03             # Change this number
   years = 10              # Change this number
   ```
3. Click **Run All** again
4. See the updated results

That's it. You're using executable specifications.

---

## 5. Render to PDF/Word/HTML

When you're ready to share, render the notebook to a polished document.

**From VS Code:**
- Press `Ctrl+Shift+K` (or `Cmd+Shift+K` on Mac)
- Select format (HTML, PDF, or Word)

**From command line:**
```bash
quarto render TEMPLATE_starter_spec.ipynb --to pdf
```

Output goes to the `_output/` folder.

---

## Key Shortcuts

| Action | Shortcut |
|--------|----------|
| Run cell and move to next | `Shift+Enter` |
| Run cell and stay | `Ctrl+Enter` |
| Run all cells | Click **Run All** |
| Render document | `Ctrl+Shift+K` |

**When a cell is selected (blue border):**

| Action | Key |
|--------|-----|
| Add cell below | `B` |
| Add cell above | `A` |
| Delete cell | `D D` (press D twice) |
| Change to Markdown | `M` |
| Change to Code | `Y` |
| Edit cell | `Enter` |
| Stop editing | `Escape` |

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Cell shows `[*]` and hangs | Kernel is busy. Click the Stop button or restart kernel (circular arrow icon) |
| `NameError: name 'x' is not defined` | Cells must run in order. Click **Run All** to run from the top |
| Numbers look wrong | Check your input values |
| Can't edit a cell | Click inside the cell, or press `Enter` when selected |
| Results don't update | Re-run the cell after changes (`Shift+Enter`) |
| PDF won't render | Run `quarto install tinytex` in terminal |

---

## Next Steps

| Goal | Read |
|------|------|
| Learn Python basics for specs | Open `GUIDE_building_calc_specs.ipynb` |
| See pension-specific templates | Open any `*_spec.ipynb` file |
| Understand the cheat sheets | See the Appendix in the GUIDE |

---

## Quick Reference

**Editing values:**
```python
value = 15000.00      # Number
rate = 0.05           # 5% as decimal
name = "Smith"        # Text in quotes
is_married = True     # True or False
```

**Basic arithmetic:**
```python
total = a + b         # Add
diff = a - b          # Subtract
product = a * b       # Multiply
quotient = a / b      # Divide
power = a ** b        # a to the power of b
```

**Common pension formula:**
```python
revalued = original * (1 + rate) ** years
```

For more, see the GUIDE.

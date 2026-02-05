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

---

## Markdown Cheat Sheet

Use these in Markdown cells to format your documentation.

### Headings

```markdown
# Heading 1 (largest)
## Heading 2
### Heading 3
#### Heading 4
```

### Text Formatting

```markdown
**bold text**
*italic text*
***bold and italic***
~~strikethrough~~
`inline code`
```

### Lists

**Bullet list:**
```markdown
- Item one
- Item two
  - Nested item
  - Another nested
- Item three
```

**Numbered list:**
```markdown
1. First step
2. Second step
3. Third step
```

### Tables

```markdown
| Column 1 | Column 2 | Column 3 |
|----------|----------|----------|
| Data     | Data     | Data     |
| More     | More     | More     |
```

**Alignment:**
```markdown
| Left     | Center   | Right    |
|:---------|:--------:|---------:|
| text     | text     | text     |
```

### Links and Images

```markdown
[Link text](https://example.com)
![Image alt text](path/to/image.png)
```

### Code Blocks

For formulas or code snippets:

````markdown
```python
result = value * factor
```
````

Or inline: `` `variable_name` ``

### Blockquotes

```markdown
> This is a quote or important note.
> It can span multiple lines.
```

### Horizontal Rule

```markdown
---
```

### Checkboxes (task lists)

```markdown
- [x] Completed task
- [ ] Incomplete task
```

---

## Python Cheat Sheet

Common patterns used in these templates.

### Variables

```python
# Simple assignment
pension = 15000.00
years = 10
gender = "M"
```

### Arithmetic

```python
# Basic math
total = value1 + value2
difference = value1 - value2
product = value1 * value2
quotient = value1 / value2

# Compound interest / revaluation
factor = (1 + rate) ** years
revalued = original * factor
```

### Print Statements

```python
# Basic print
print("Hello")

# F-strings (formatted)
print(f"Pension: {pension}")
print(f"Pension: {pension:,.2f}")      # With commas and 2 decimals
print(f"Pension: £{pension:>12,.2f}")  # Right-aligned, 12 chars wide
```

### Conditionals

```python
if gender == "M":
    factor = male_factor
else:
    factor = female_factor
```

### Dictionaries (lookup tables)

```python
# Define
factors = {0: 1.000, 1: 0.940, 2: 0.882}

# Look up
result = factors[years_early]
result = factors.get(years_early, 0.720)  # With default
```

---

## Formatting Numbers

| Format | Example | Result |
|--------|---------|--------|
| `{x}` | `f"{15000}"` | 15000 |
| `{x:,}` | `f"{15000:,}"` | 15,000 |
| `{x:.2f}` | `f"{15000:.2f}"` | 15000.00 |
| `{x:,.2f}` | `f"{15000:,.2f}"` | 15,000.00 |
| `{x:>10}` | `f"{15000:>10}"` | `    15000` (right-aligned) |
| `{x:<10}` | `f"{15000:<10}"` | `15000    ` (left-aligned) |
| `{x:.4f}` | `f"{0.826:.4f}"` | 0.8260 |
| `{x:.2%}` | `f"{0.035:.2%}"` | 3.50% |

---

## Useful Symbols

Copy-paste these into your Markdown cells:

| Symbol | Usage |
|--------|-------|
| £ | Currency |
| × | Multiplication |
| ÷ | Division |
| ≤ ≥ | Less/greater than or equal |
| ≠ | Not equal |
| → | Arrow (workflow) |
| ✓ ✗ | Check/cross marks |
| • | Bullet point |
| — | Em dash |

---

## Template Structure

All pension spec templates follow this pattern:

1. **Header** — Scheme name, version, author, date
2. **Purpose** — What this spec calculates
3. **Member Data** — Editable input values
4. **Scheme Parameters** — Rules (usually don't change)
5. **Calculation** — Step-by-step with explanations
6. **Summary** — All inputs and outputs in one place
7. **Reference Tables** — Factor tables, etc.
8. **Edge Cases** — How to handle special situations
9. **Sign-Off** — Author, reviewer, approver

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Cell shows `[*]` and hangs | Kernel is busy. Click ◼ Stop button or restart kernel |
| `NameError: name 'x' is not defined` | Run cells in order from top. A cell is using a variable defined earlier |
| Numbers look wrong | Check input values in Member Data section |
| Can't edit a cell | Make sure you're clicking inside the cell, not just selecting it |
| Results don't update | Re-run the cell after making changes (`Shift+Enter`) |

---

## Version Control with Jupytext

For team collaboration, pair notebooks with Python files:

```bash
# One-time setup for a notebook
jupytext --set-formats ipynb,py:percent active_to_retirement_spec.ipynb
```

This creates `active_to_retirement_spec.py` that stays in sync. Commit the `.py` file to Git for clean diffs.

**Sync after editing:**
```bash
jupytext --sync active_to_retirement_spec.ipynb
```

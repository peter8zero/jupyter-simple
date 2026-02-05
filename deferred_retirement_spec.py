# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.1
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Deferred to Retirement Calculation
#
# | Field | Value |
# |-------|-------|
# | Scheme | [Scheme Name] |
# | Version | 1.0 |
# | Author | [Your Name] |
# | Date | [Date] |

# %% [markdown]
# ## 1. Purpose of this spec is to 
#
# This document specifies how to calculate a deferred member's pension at retirement.

# %% [markdown]
# ## 2. Member Data
#
# Enter the member's details below. **Change these values** to test different scenarios.

# %%
# Member details - EDIT THESE VALUES
pension_at_leaving = 15000.00
gmp_at_leaving = 3500.00
years_of_revaluation = 7
years_early = 3
gender = "M"  # M or F

# %% [markdown]
# ## 3. Scheme Parameters
#
# These are the scheme rules. Only change if the scheme rules are different.

# %%
# Scheme parameters - usually don't change these
gmp_reval_rate = 0.035      # 3.5% fixed rate
excess_reval_rate = 0.025   # 2.5% (example average CPI)

# Early retirement factors
erf_male =   {0: 1.000, 1: 0.940, 2: 0.882, 3: 0.826, 4: 0.772, 5: 0.720}
erf_female = {0: 1.000, 1: 0.945, 2: 0.891, 3: 0.839, 4: 0.789, 5: 0.741}

# %% [markdown]
# ## 4. Calculation
#
# ### Step 1: Split into GMP and Excess

# %%
excess_at_leaving = pension_at_leaving - gmp_at_leaving

print(f"Pension at leaving:  £{pension_at_leaving:,.2f}")
print(f"GMP at leaving:      £{gmp_at_leaving:,.2f}")
print(f"Excess at leaving:   £{excess_at_leaving:,.2f}")

# %% [markdown]
# ### Step 2: Revalue GMP
#
# Formula: `GMP at retirement = GMP at leaving × (1 + rate)^years`

# %%
gmp_reval_factor = (1 + gmp_reval_rate) ** years_of_revaluation
gmp_revalued = gmp_at_leaving * gmp_reval_factor

print(f"GMP revaluation factor: {gmp_reval_factor:.4f}")
print(f"GMP revalued:           £{gmp_revalued:,.2f}")

# %% [markdown]
# ### Step 3: Revalue Excess
#
# Formula: `Excess at retirement = Excess at leaving × (1 + rate)^years`

# %%
excess_reval_factor = (1 + excess_reval_rate) ** years_of_revaluation
excess_revalued = excess_at_leaving * excess_reval_factor

print(f"Excess revaluation factor: {excess_reval_factor:.4f}")
print(f"Excess revalued:           £{excess_revalued:,.2f}")

# %% [markdown]
# ### Step 4: Apply Early Retirement Factor
#
# Look up factor based on years early and gender.

# %%
# Look up the early retirement factor
if gender == "M":
    erf = erf_male[years_early]
else:
    erf = erf_female[years_early]

gmp_at_retirement = gmp_revalued * erf
excess_at_retirement = excess_revalued * erf

print(f"Years early:             {years_early}")
print(f"Early retirement factor: {erf}")
print(f"")
print(f"GMP at retirement:       £{gmp_at_retirement:,.2f}")
print(f"Excess at retirement:    £{excess_at_retirement:,.2f}")

# %% [markdown]
# ### Step 5: Total Pension

# %%
total_pension = gmp_at_retirement + excess_at_retirement

print("="*40)
print(f"TOTAL PENSION: £{total_pension:,.2f} per year")
print("="*40)

# %% [markdown]
# ## 5. Summary
#
# Run this cell to see the full calculation summary.

# %%
print("CALCULATION SUMMARY")
print("="*50)
print(f"")
print(f"INPUTS:")
print(f"  Pension at leaving:      £{pension_at_leaving:>12,.2f}")
print(f"  GMP at leaving:          £{gmp_at_leaving:>12,.2f}")
print(f"  Years of revaluation:     {years_of_revaluation:>12}")
print(f"  Years early:              {years_early:>12}")
print(f"  Gender:                   {gender:>12}")
print(f"")
print(f"CALCULATION:")
print(f"  Excess at leaving:       £{excess_at_leaving:>12,.2f}")
print(f"  GMP reval factor:         {gmp_reval_factor:>12.4f}")
print(f"  Excess reval factor:      {excess_reval_factor:>12.4f}")
print(f"  Early retirement factor:  {erf:>12.4f}")
print(f"")
print(f"RESULT:")
print(f"  GMP at retirement:       £{gmp_at_retirement:>12,.2f}")
print(f"  Excess at retirement:    £{excess_at_retirement:>12,.2f}")
print(f"  " + "-"*36)
print(f"  TOTAL PENSION:           £{total_pension:>12,.2f} p.a.")
print(f"")
print("="*50)

# %% [markdown]
# ## 6. Early Retirement Factor Table
#
# | Years Early | Male | Female |
# |-------------|------|--------|
# | 0 | 1.000 | 1.000 |
# | 1 | 0.940 | 0.945 |
# | 2 | 0.882 | 0.891 |
# | 3 | 0.826 | 0.839 |
# | 4 | 0.772 | 0.789 |
# | 5 | 0.720 | 0.741 |

# %% [markdown]
# ## 7. Edge Cases
#
# | Scenario | How to Handle |
# |----------|---------------|
# | No GMP | Set `gmp_at_leaving = 0` |
# | Normal retirement | Set `years_early = 0` |
# | Late retirement | Need late retirement factors (not in this spec) |

# %% [markdown]
# ## 8. Sign-Off
#
# | Role | Name | Date |
# |------|------|------|
# | Author | | |
# | Reviewer | | |
# | Approver | | |

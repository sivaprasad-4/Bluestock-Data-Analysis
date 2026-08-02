# Mutual Fund Data Dictionary

This document describes the datasets used in the Bluestock Data Analysis project.

---

# 1. dim_fund

**Source:** `01_fund_master.csv`

| Column | Data Type | Description |
|---------|-----------|-------------|
| amfi_code | INTEGER | Unique AMFI scheme code |
| fund_house | TEXT | Mutual fund company |
| scheme_name | TEXT | Name of the mutual fund scheme |
| category | TEXT | Fund category (Equity/Debt) |
| sub_category | TEXT | Fund sub-category |
| plan | TEXT | Regular or Direct plan |
| launch_date | DATE | Scheme launch date |
| benchmark | TEXT | Benchmark index |
| expense_ratio_pct | REAL | Expense ratio (%) |
| exit_load_pct | REAL | Exit load (%) |
| min_sip_amount | INTEGER | Minimum SIP amount |
| min_lumpsum_amount | INTEGER | Minimum lump sum investment |
| fund_manager | TEXT | Fund manager name |
| risk_category | TEXT | Risk level |
| sebi_category_code | TEXT | SEBI category code |

---

# 2. fact_nav

**Source:** `03_nav_history.csv`

| Column | Data Type | Description |
|---------|-----------|-------------|
| amfi_code | INTEGER | Scheme AMFI code |
| nav_date | DATE | NAV date |
| nav | REAL | Net Asset Value |
| daily_return | REAL | Daily percentage return |

---

# 3. fact_transactions

**Source:** `08_investor_transactions.csv`

| Column | Data Type | Description |
|---------|-----------|-------------|
| investor_id | TEXT | Investor ID |
| transaction_date | DATE | Transaction date |
| amfi_code | INTEGER | Scheme AMFI code |
| transaction_type | TEXT | SIP, Lumpsum or Redemption |
| amount_inr | INTEGER | Transaction amount (INR) |
| state | TEXT | Investor state |
| city | TEXT | Investor city |
| city_tier | TEXT | T30/B30 classification |
| age_group | TEXT | Investor age group |
| gender | TEXT | Investor gender |
| annual_income_lakh | REAL | Annual income (Lakhs) |
| payment_mode | TEXT | Payment method |
| kyc_status | TEXT | KYC verification status |

---

# 4. fact_performance

**Source:** `07_scheme_performance.csv`

| Column | Data Type | Description |
|---------|-----------|-------------|
| amfi_code | INTEGER | Scheme AMFI code |
| scheme_name | TEXT | Scheme name |
| fund_house | TEXT | Fund house |
| category | TEXT | Fund category |
| plan | TEXT | Direct/Regular |
| return_1yr_pct | REAL | 1-Year return (%) |
| return_3yr_pct | REAL | 3-Year return (%) |
| return_5yr_pct | REAL | 5-Year return (%) |
| benchmark_3yr_pct | REAL | Benchmark return (%) |
| alpha | REAL | Alpha |
| beta | REAL | Beta |
| sharpe_ratio | REAL | Sharpe Ratio |
| sortino_ratio | REAL | Sortino Ratio |
| std_dev_ann_pct | REAL | Annualized standard deviation |
| max_drawdown_pct | REAL | Maximum drawdown (%) |
| aum_crore | REAL | Assets Under Management (Crores) |
| expense_ratio_pct | REAL | Expense ratio (%) |
| morningstar_rating | INTEGER | Morningstar rating |
| risk_grade | TEXT | Risk grade |
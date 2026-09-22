# 🏦 Enterprise Retail Banking ELT Engine & Governance Verifier

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=flat-square&logo=python&logoColor=white)
![DuckDB](https://img.shields.io/badge/Engine-DuckDB-yellow?style=flat-square&logo=duckdb&logoColor=black)
![Pytest](https://img.shields.io/badge/Testing-Pytest-green?style=flat-square&logo=pytest&logoColor=white)
![Governance](https://img.shields.io/badge/Data-Governance-brightgreen?style=flat-square)
![Architecture](https://img.shields.io/badge/Layout-src--layout-orange?style=flat-square)

A high-performance, modular Python framework built to simulate, execute, and automatically evaluate ELT (Extract, Load, Transform) data pipelines in an isolated, in-memory **OLAP environment**.

Designed using enterprise software engineering standards, this framework models retail banking transformations — aggregating transaction logs into daily customer summaries — and enforces runtime **Data Quality Verification** and **Data Governance** assertions.

---

## 🎨 Architecture & Pipeline Flow

The engine uses a Gym-style environment loop (`reset()`, `step()`, `submit()`) powered by **DuckDB** for zero-dependency, sub-second query evaluation.

```text
  📥 Raw Staging Data          ⚡ In-Memory Engine         🛡️ Governance Engine          📊 Metric Evaluation
  ┌──────────────────┐         ┌──────────────────┐        ┌────────────────────┐        ┌──────────────────┐
  │ raw_transactions │  ──►    │  DuckDB Execution │  ──►   │ • Non-Null Check   │  ──►   │  Reward Score    │
  │ (account, date)  │         │  (Aggregations)   │        │ • Primary Key PK   │        │  (1.0 = Success) │
  └──────────────────┘         └──────────────────┘         │ • Status Filter    │        └──────────────────┘
                                                              └────────────────────┘
```

---

## ✨ Engineering Highlights

- ⚡ **Sub-Second OLAP Execution** — Leverages DuckDB for vectorized, zero-overhead SQL execution directly in memory.
- 🛡️ **Automated Governance Guardrails** — Intercepts transformed datasets prior to final target reconciliation to enforce primary key uniqueness and non-null constraints.
- 🏦 **Financial Domain Abstraction** — Models real-world retail banking workflows, calculating daily customer spending metrics while pruning failed or cancelled transactions.
- 📦 **Enterprise Package Architecture** — Built with a clean `src/` layout and `pyproject.toml` configuration, supporting local editable installation (`pip install -e .`).
- 🧪 **Comprehensive Pytest Suite** — Automated unit testing covering valid pipeline runs, business rule logic filtering, and edge-case governance failures.

---

## 🛠️ Data Governance & Quality Engine

The verification harness (`verifier.py`) subjects candidate target tables to strict enterprise governance rules:

| Governance Check | Description | Targeted Columns | Compliance Status |
|---|---|---|---|
| **Non-Null Constraint** | Guarantees primary key identity columns contain zero NULL values. | `account_id`, `txn_date` | 🟢 Enforced |
| **Composite Uniqueness** | Verifies primary/composite key candidates contain no duplicate entries. | `(account_id, txn_date)` | 🟢 Enforced |
| **Business Status Filter** | Ensures failed or non-completed transactions are excluded from aggregates. | `status = 'COMPLETED'` | 🟢 Enforced |

---

## 💡 Benchmark SQL Transformation

The framework tests candidate SQL queries against staging tables to build target analytical models:

```sql
-- Target: daily_customer_summary
CREATE TABLE daily_customer_summary AS 
SELECT 
    account_id, 
    txn_date, 
    SUM(amount) AS total_spend, 
    COUNT(*) AS txn_count
FROM raw_transactions
WHERE status = 'COMPLETED'
GROUP BY account_id, txn_date
ORDER BY account_id, txn_date;
```

---

## 📂 Project Layout

```text
banking-elt-governance/
├── 📁 src/
│   └── 📁 elt_bench/
│       ├── 📄 __init__.py
│       ├── 📄 env.py              # Gym-style environment managing DuckDB sessions
│       ├── 📄 verifier.py         # Data quality assertions & target matching engine
│       └── 📁 tasks/
│           ├── 📄 __init__.py
│           └── 📄 banking_elt.py  # Retail banking data schemas & expected targets
├── 📁 tests/
│   └── 📄 test_verifier.py        # Automated Pytest suite (success, filter, & DQ tests)
├── 📄 test_local.py               # Local integration driver script
├── 📄 pyproject.toml              # Package metadata & Pytest configuration
├── 📄 .gitignore
└── 📄 README.md
```

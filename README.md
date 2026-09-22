# 🏦 Enterprise Retail Banking ELT Engine & Governance Verifier

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=flat-square&logo=python&logoColor=white)
![DuckDB](https://img.shields.io/badge/Engine-DuckDB-yellow?style=flat-square&logo=duckdb&logoColor=black)
![Pytest](https://img.shields.io/badge/Testing-Pytest-green?style=flat-square&logo=pytest&logoColor=white)
![Governance](https://img.shields.io/badge/Data-Governance-brightgreen?style=flat-square)
![Architecture](https://img.shields.io/badge/Layout-src--layout-orange?style=flat-square)

A high-performance, modular Python framework built to simulate, execute, and automatically evaluate ELT (Extract, Load, Transform) data pipelines in an isolated, in-memory **OLAP environment**.

Designed using enterprise software engineering standards, this framework models retail banking transformations—aggregating transaction logs into daily customer summaries—and enforces runtime **Data Quality Verification** and **Data Governance** assertions.

---

## 🎨 Architecture & Pipeline Flow

The engine uses a Gym-style environment loop (`reset()`, `step()`, `submit()`) powered by **DuckDB** for zero-dependency, sub-second query evaluation.

```text
  📥 Raw Staging Data       ⚡ In-Memory Engine         🛡️ Governance Engine        📊 Metric Evaluation
  ┌──────────────────┐      ┌──────────────────┐      ┌────────────────────┐      ┌──────────────────┐
  │ raw_transactions │ ──►  │ DuckDB Execution │ ──►  │ • Non-Null Check   │ ──►  │ Reward Score     │
  │ (account, date)  │      │ (Aggregations)   │      │ • Primary Key PK   │      │ (1.0 = Success)  │
  └──────────────────┘      └──────────────────┘      │ • Status Filter    │      └──────────────────┘
                                                      └────────────────────┘

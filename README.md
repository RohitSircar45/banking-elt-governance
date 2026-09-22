# 🏦 Enterprise Retail Banking ELT Engine

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=flat-square&logo=python&logoColor=white)
![DuckDB](https://img.shields.io/badge/Engine-DuckDB-yellow?style=flat-square&logo=duckdb&logoColor=black)
![Pytest](https://img.shields.io/badge/Testing-Pytest-green?style=flat-square&logo=pytest&logoColor=white)
![Governance](https://img.shields.io/badge/Data-Governance-brightgreen?style=flat-square)
![Architecture](https://img.shields.io/badge/Layout-src--layout-orange?style=flat-square)

A high-performance Python framework built to simulate, execute, and automatically evaluate ELT (Extract, Load, Transform) pipelines using **DuckDB**, **Pandas**, and **Pytest**.

This project models enterprise retail banking transformations and enforces automated **Data Governance** and **Quality Verification** rules in real time.

---

## 🎨 System Architecture

```text
  📥 Raw Transactions ──► ⚡ DuckDB Engine ──► 🛡️ Governance Check ──► 📊 Final Metric
   (Staging Tables)        (In-Memory OLAP)     (Nulls / Duplicates)     (Reward Score)

# ELT-Bench RL Environment

A fast, lightweight Python environment built for testing LLMs on ELT (Extract, Load, Transform) data engineering tasks. It uses DuckDB under the hood so everything runs locally in-memory with zero external dependencies or API keys required.

## How It Works

1. **Reset:** The environment spins up an in-memory DuckDB instance and loads raw source data as staging tables.
2. **Step:** The agent runs standard SQL queries (`CREATE TABLE`, `INSERT`, etc.) to transform data into target analytical schemas.
3. **Submit:** An automated verifier checks the final database state against ground-truth tables and returns a score from `0.0` to `1.0`.

## Repository Layout

* `env.py` — The main environment loop (`reset`, `step`, `submit`).
* `verifier.py` — Grading logic that compares output tables against expected DataFrames (handles out-of-order rows and flexible data types).
* `test_local.py` — A simple script to test the full pipeline on your machine.

## Getting Started

### 1. Install dependencies
```bash
pip install duckdb pandas
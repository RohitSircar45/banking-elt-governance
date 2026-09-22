import pytest
from elt_bench.env import ELTBenchEnv
from elt_bench.tasks.banking_elt import get_banking_task_data

def test_banking_task_success():
    sources, targets = get_banking_task_data()
    env = ELTBenchEnv(sources, targets)
    env.reset()

    correct_query = """
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
    """
    env.step(correct_query)
    reward = env.submit()
    assert reward == 1.0


def test_banking_task_failure_on_missing_filter():
    sources, targets = get_banking_task_data()
    env = ELTBenchEnv(sources, targets)
    env.reset()

    incorrect_query = """
    CREATE TABLE daily_customer_summary AS 
    SELECT 
        account_id, 
        txn_date, 
        SUM(amount) AS total_spend, 
        COUNT(*) AS txn_count
    FROM raw_transactions
    GROUP BY account_id, txn_date;
    """
    env.step(incorrect_query)
    reward = env.submit()
    assert reward < 1.0


def test_data_quality_governance_failure():
    """
    Tests that queries generating NULL values in required key columns 
    are flagged as Data Quality failures (reward < 1.0).
    """
    sources, targets = get_banking_task_data()
    env = ELTBenchEnv(sources, targets)
    env.reset()

    # Query that produces NULL account_ids
    bad_quality_query = """
    CREATE TABLE daily_customer_summary AS 
    SELECT 
        CAST(NULL AS VARCHAR) AS account_id, 
        txn_date, 
        SUM(amount) AS total_spend, 
        COUNT(*) AS txn_count
    FROM raw_transactions
    WHERE status = 'COMPLETED'
    GROUP BY txn_date;
    """
    env.step(bad_quality_query)
    reward = env.submit()
    assert reward < 1.0
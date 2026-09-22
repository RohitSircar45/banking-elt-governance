import pandas as pd

def get_banking_task_data():
    """
    Simulates raw retail banking transaction logs (staging layer) 
    and target analytical aggregate data for the ELT benchmark environment.
    """
    # Raw source table: raw_transactions
    raw_transactions = pd.DataFrame({
        "transaction_id": [101, 102, 103, 104, 105],
        "account_id": ["ACC_1", "ACC_1", "ACC_2", "ACC_1", "ACC_2"],
        "txn_date": ["2026-03-01", "2026-03-01", "2026-03-01", "2026-03-02", "2026-03-02"],
        "amount": [150.00, 45.50, 200.00, 12.00, 500.00],
        "status": ["COMPLETED", "COMPLETED", "FAILED", "COMPLETED", "COMPLETED"]
    })

    # Expected target table: daily_customer_summary
    # Filters out FAILED transactions and aggregates total spend per account per day
    expected_summary = pd.DataFrame({
        "account_id": ["ACC_1", "ACC_1", "ACC_2"],
        "txn_date": ["2026-03-01", "2026-03-02", "2026-03-02"],
        "total_spend": [195.50, 12.00, 500.00],
        "txn_count": [2, 1, 1]
    })

    sources = {"transactions": raw_transactions}
    targets = {"daily_customer_summary": expected_summary}

    return sources, targets
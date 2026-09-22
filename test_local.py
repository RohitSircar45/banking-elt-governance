from elt_bench.env import ELTBenchEnv
from elt_bench.tasks.banking_elt import get_banking_task_data

# 1. Load Banking Financial Data Task
sources, targets = get_banking_task_data()

# 2. Start the environment
env = ELTBenchEnv(sources, targets)
env.reset()

# 3. Simulate SQL written by an AI model to build daily_customer_summary
query = """
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

env.step(query)

# 4. Grade the submission
reward = env.submit()
print(f"Banking Transformation Task Reward: {reward}")
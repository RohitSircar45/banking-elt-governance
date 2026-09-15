import pandas as pd
from env import ELTBenchEnv

# 1. Define dummy input source data (Orders)
sources = {"orders": pd.DataFrame({"user_id": [1, 2, 1], "amount": [50.0, 250.0, 50.0]})}

# 2. Define expected output target data (User Summaries)
targets = {"user_summary": pd.DataFrame({"user_id": [1, 2], "total_spent": [100.0, 250.0]})}

# 3. Start the environment
env = ELTBenchEnv(sources, targets)
env.reset()

# 4. Simulate a correct SQL command written by the AI model
env.step("CREATE TABLE user_summary AS SELECT user_id, SUM(amount) AS total_spent FROM raw_orders GROUP BY user_id")

# 5. Grade the submission
reward = env.submit()
print(f"Integration Test Reward: {reward}")
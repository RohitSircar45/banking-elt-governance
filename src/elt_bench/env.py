import duckdb
from .verifier import verify_elt_pipeline

class ELTBenchEnv:
    def __init__(self, source_data: dict, target_data: dict):
        self.source_data = source_data
        self.target_data = target_data
        self.conn = None

    def reset(self):
        """Prepares a fresh database and loads raw starting data."""
        self.conn = duckdb.connect(":memory:")
        for name, df in self.source_data.items():
            self.conn.register(f"raw_{name}", df)
            self.conn.execute(f"CREATE TABLE raw_{name} AS SELECT * FROM raw_{name}")
        return f"Loaded tables: {list(self.source_data.keys())}"

    def step(self, sql_query: str):
        """Executes a SQL command sent by the model."""
        try:
            res = self.conn.execute(sql_query).df()
            return f"SUCCESS:\n{res.head()}"
        except Exception as e:
            return f"ERROR: {str(e)}"

    def submit(self) -> float:
        """Triggers grading when the model finishes its task."""
        return verify_elt_pipeline(self.conn, self.target_data)
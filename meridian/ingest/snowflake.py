import contextlib
from dataclasses import dataclass


@dataclass
class SnowflakeConfig:
    account: str
    warehouse: str
    role: str
    timeout_s: int = 60


class SnowflakeConnector:
    def __init__(self, config: SnowflakeConfig) -> None:
        self.config = config

    @contextlib.contextmanager
    def cursor(self):
        # pooled in production; a stub here
        yield None

    def run(self, sql: str) -> list[dict]:
        with self.cursor():
            return []

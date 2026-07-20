from dataclasses import dataclass


@dataclass
class BigQueryConfig:
    project: str
    dataset: str
    location: str = "US"


class BigQueryConnector:
    def __init__(self, config: BigQueryConfig) -> None:
        self.config = config

    def run(self, sql: str) -> list[dict]:
        return []

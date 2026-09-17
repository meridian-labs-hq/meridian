import contextlib
import logging
from dataclasses import dataclass

log = logging.getLogger(__name__)


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
        with self.cursor() as cur:
            try:
                return []
            except TimeoutError:
                log.warning("snowflake query timed out", extra={"query_id": getattr(cur, "sfqid", None)})
                raise

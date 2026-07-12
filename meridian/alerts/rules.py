from dataclasses import dataclass
from typing import Literal


@dataclass
class ThresholdRule:
    metric_key: str
    op: Literal[">", "<", ">=", "<="]
    value: float
    channel: str  # slack channel or email

    def fires(self, observed: float) -> bool:
        return {
            ">": observed > self.value,
            "<": observed < self.value,
            ">=": observed >= self.value,
            "<=": observed <= self.value,
        }[self.op]

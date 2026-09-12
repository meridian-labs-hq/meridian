import time

from .rules import ThresholdRule

_last_fired: dict[str, float] = {}
COOLDOWN_S = 3600


def evaluate(rules: list[ThresholdRule], observed: dict[str, float], now: float | None = None) -> list[ThresholdRule]:
    now = time.time() if now is None else now
    fired = []
    for rule in rules:
        if rule.metric_key in observed and rule.fires(observed[rule.metric_key]):
            key = f"{rule.metric_key}:{rule.op}:{rule.value}"
            if now - _last_fired.get(key, 0) < COOLDOWN_S:
                continue
            _last_fired[key] = now
            fired.append(rule)
    return fired

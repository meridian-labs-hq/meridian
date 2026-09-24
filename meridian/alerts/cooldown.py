COOLDOWN_S = 3600


def key(metric_key: str, kind: str) -> str:
    return f"{metric_key}:{kind}"

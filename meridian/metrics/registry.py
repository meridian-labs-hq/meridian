from .models import Metric

_REGISTRY: dict[str, Metric] = {}


def register(metric: Metric) -> None:
    if metric.key in _REGISTRY:
        raise ValueError(f"duplicate metric {metric.key}")
    _REGISTRY[metric.key] = metric


def get(key: str) -> Metric:
    return _REGISTRY[key]


def all_metrics() -> list[Metric]:
    return sorted(_REGISTRY.values(), key=lambda m: m.key)

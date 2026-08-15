from statistics import mean, pstdev


def zscore(series: list[float], latest: float) -> float:
    if len(series) < 2:
        return 0.0
    sd = pstdev(series) or 1.0
    return (latest - mean(series)) / sd


def is_anomaly(series: list[float], latest: float, threshold: float = 3.0) -> bool:
    return abs(zscore(series, latest)) >= threshold

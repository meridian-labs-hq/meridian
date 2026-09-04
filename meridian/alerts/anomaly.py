from statistics import mean, pstdev

WINDOW = 28


def zscore(series: list[float], latest: float) -> float:
    window = series[-WINDOW:]
    if len(window) < 2:
        return 0.0
    sd = pstdev(window) or 1.0
    return (latest - mean(window)) / sd


def is_anomaly(series: list[float], latest: float, threshold: float = 3.0) -> bool:
    # weekly seasonality: compare against the same weekday when we have 4+ weeks
    if len(series) >= 28:
        same_day = series[-7::-7][:4]
        if same_day and abs(latest - mean(same_day)) < (pstdev(same_day) or 1.0):
            return False
    return abs(zscore(series, latest)) >= threshold

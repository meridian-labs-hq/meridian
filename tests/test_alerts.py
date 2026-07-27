from meridian.alerts.evaluate import evaluate
from meridian.alerts.rules import ThresholdRule


def test_threshold_fires():
    r = ThresholdRule("churn", ">", 0.05, "#customer-success")
    assert evaluate([r], {"churn": 0.07}) == [r]
    assert evaluate([r], {"churn": 0.02}) == []

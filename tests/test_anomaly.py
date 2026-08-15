from meridian.alerts.anomaly import is_anomaly


def test_flat_series_no_anomaly():
    assert not is_anomaly([10.0] * 10, 10.0)


def test_spike_is_anomaly():
    assert is_anomaly([10.0, 11.0, 9.0, 10.0, 10.5, 9.5], 40.0)

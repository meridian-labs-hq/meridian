import pytest

from meridian.metrics import registry
from meridian.metrics.models import Metric


def test_register_and_get():
    m = Metric(key="arr", name="ARR", sql="select sum(mrr)*12 from subs", owner="finance")
    registry.register(m)
    assert registry.get("arr").name == "ARR"


def test_duplicate_refused():
    m = Metric(key="dup", name="Dup", sql="select 1", owner="x")
    registry.register(m)
    with pytest.raises(ValueError):
        registry.register(m)

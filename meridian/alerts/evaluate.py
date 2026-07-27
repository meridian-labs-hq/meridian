from .rules import ThresholdRule


def evaluate(rules: list[ThresholdRule], observed: dict[str, float]) -> list[ThresholdRule]:
    fired = []
    for rule in rules:
        if rule.metric_key in observed and rule.fires(observed[rule.metric_key]):
            fired.append(rule)
    return fired

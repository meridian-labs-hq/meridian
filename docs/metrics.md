# Defining a metric

A metric is a name, an owner and a SQL expression. Define it once in `metrics/definitions/` and every dashboard and alert reads the same definition.

```yaml
key: arr
name: ARR
owner: finance
sql: select sum(mrr) * 12 from subscriptions where status = 'active'
```

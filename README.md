# Meridian

Meridian is a B2B analytics platform: connect a warehouse, define metrics once, and ship dashboards and alerts to every team.

## Layout

- `meridian/api` — FastAPI service
- `meridian/metrics` — metric definitions and the semantic layer
- `meridian/ingest` — warehouse connectors
- `meridian/alerts` — threshold and anomaly alerts
- `web/` — dashboard front end

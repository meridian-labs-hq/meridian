from fastapi import APIRouter, HTTPException

from meridian.metrics import registry

router = APIRouter(prefix="/metrics")


@router.get("")
def list_metrics():
    return [m.model_dump() for m in registry.all_metrics()]


@router.get("/{key}")
def get_metric(key: str):
    try:
        return registry.get(key).model_dump()
    except KeyError:
        raise HTTPException(404, f"no metric {key}")

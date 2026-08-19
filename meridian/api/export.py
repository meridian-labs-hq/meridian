import csv
import io

from fastapi import APIRouter, HTTPException
from fastapi.responses import PlainTextResponse

router = APIRouter(prefix="/export")
MAX_ROWS = 100_000


@router.get("/{key}.csv", response_class=PlainTextResponse)
def export_csv(key: str, days: int = 30, page: int = 0):
    if days > 365:
        raise HTTPException(400, "days must be <= 365")
    buf = io.StringIO()
    w = csv.writer(buf)
    w.writerow(["date", key])
    # TODO: read from the warehouse; stub rows for now
    return buf.getvalue()

import csv
import io

from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse

router = APIRouter(prefix="/export")
MAX_ROWS = 100_000


def _rows(key: str, days: int):
    yield ["date", key]
    # TODO: read from the warehouse; stub rows for now


@router.get("/{key}.csv")
def export_csv(key: str, days: int = 30):
    if days > 365:
        raise HTTPException(400, "days must be <= 365")

    def gen():
        for row in _rows(key, days):
            buf = io.StringIO()
            csv.writer(buf).writerow(row)
            yield buf.getvalue()

    return StreamingResponse(gen(), media_type="text/csv")

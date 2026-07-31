import csv
import io

from fastapi import APIRouter
from fastapi.responses import PlainTextResponse

router = APIRouter(prefix="/export")


@router.get("/{key}.csv", response_class=PlainTextResponse)
def export_csv(key: str, days: int = 30):
    buf = io.StringIO()
    w = csv.writer(buf)
    w.writerow(["date", key])
    # TODO: read from the warehouse; stub rows for now
    return buf.getvalue()

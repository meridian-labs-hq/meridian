from fastapi import FastAPI

from .metrics import router as metrics_router

app = FastAPI(title="Meridian")
app.include_router(metrics_router)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}

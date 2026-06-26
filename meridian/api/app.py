from fastapi import FastAPI

app = FastAPI(title="Meridian")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}

from fastapi import FastAPI

app = FastAPI(title="Trading Lab API")


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok", "service": "Trading Lab API"}

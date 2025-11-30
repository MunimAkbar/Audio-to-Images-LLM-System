from fastapi import FastAPI
from app.api.routes import router
from app.utils.logging import setup_logging
import uvicorn

setup_logging()

app = FastAPI(title="Audio to Image AI")

app.include_router(router, prefix="/api/v1")

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)

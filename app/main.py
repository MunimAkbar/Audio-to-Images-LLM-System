from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.api.routes import router
from app.utils.logging import setup_logging
from app.config import config
import uvicorn

setup_logging()

app = FastAPI(title="Audio to Image AI")

# 1. Mount the Images (so we can see generated art)
app.mount("/images", StaticFiles(directory=config.OUTPUT_DIR), name="images")

# 2. Mount the Static Assets (CSS, JS) <--- ADD THIS LINE
app.mount("/static", StaticFiles(directory=config.STATIC_DIR), name="static")

# Include Routes
app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
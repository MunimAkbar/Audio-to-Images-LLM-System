from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.api.routes import router
from app.utils.logging import setup_logging
from app.config import config
import uvicorn

setup_logging()

app = FastAPI(title="Audio to Image AI")

# Mount the directory where images are saved so they are accessible via URL
# e.g., http://localhost:8000/images/filename.png
app.mount("/images", StaticFiles(directory=config.OUTPUT_DIR), name="images")

# Include Routes
app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
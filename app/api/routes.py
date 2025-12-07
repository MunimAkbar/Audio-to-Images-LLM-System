from fastapi import APIRouter, UploadFile, File, HTTPException, Body
from fastapi.responses import HTMLResponse
from app.services.orchestrator import Orchestrator
from app.config import config
from pydantic import BaseModel
import shutil
import os
import uuid

router = APIRouter()
orchestrator = Orchestrator()

# Request model for Step 2
class GenerateRequest(BaseModel):
    prompt: str

@router.get("/", response_class=HTMLResponse)
async def get_ui():
    with open(os.path.join(config.STATIC_DIR, "index.html"), "r", encoding="utf-8") as f:
        return f.read()

# STEP 1: Process Audio
@router.post("/process-audio")
async def process_audio_endpoint(file: UploadFile = File(...)):
    try:
        file_extension = os.path.splitext(file.filename)[1]
        temp_filename = f"{uuid.uuid4()}{file_extension}"
        file_path = os.path.join(config.AUDIO_UPLOAD_DIR, temp_filename)
        
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
            
        result = orchestrator.audio_to_prompt(file_path)
        
        # Cleanup audio
        os.remove(file_path)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# STEP 2: Generate Image
@router.post("/generate-image")
async def generate_image_endpoint(request: GenerateRequest):
    try:
        result = orchestrator.prompt_to_image(request.prompt)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
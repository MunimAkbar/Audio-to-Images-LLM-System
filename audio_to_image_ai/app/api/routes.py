from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.orchestrator import Orchestrator
from app.config import config
import shutil
import os
import uuid

router = APIRouter()
orchestrator = Orchestrator()

@router.post("/generate")
async def generate_image_from_audio(file: UploadFile = File(...)):
    """
    Uploads an audio file and generates an image from it.
    """
    try:
        # Save uploaded file
        file_extension = os.path.splitext(file.filename)[1]
        temp_filename = f"{uuid.uuid4()}{file_extension}"
        file_path = os.path.join(config.AUDIO_UPLOAD_DIR, temp_filename)
        
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
            
        # Process
        result = orchestrator.process_audio(file_path)
        
        return result
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

import os
from pathlib import Path
import torch

class Config:
    # Base Paths
    BASE_DIR = Path(__file__).resolve().parent.parent
    AUDIO_UPLOAD_DIR = BASE_DIR / "app" / "audio" / "uploads"
    OUTPUT_DIR = BASE_DIR / "data" / "processed"

    # Create directories if they don't exist
    AUDIO_UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Model Settings
    DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
    
    # STT Settings
    WHISPER_MODEL_SIZE = "base"  # Options: tiny, base, small, medium, large

    # LLM Settings
    OLLAMA_MODEL = "llama3:8b"
    OLLAMA_BASE_URL = "http://localhost:11434"

    # Image Gen Settings
    SD_MODEL_ID = "runwayml/stable-diffusion-v1-5" # Or any other local/huggingface model
    # For better performance on 8GB VRAM, we might want to use fp16
    USE_FP16 = True

config = Config()

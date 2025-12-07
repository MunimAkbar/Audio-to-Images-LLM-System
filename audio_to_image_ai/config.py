import os
from pathlib import Path
import torch

class Config:
    # Base Paths
    BASE_DIR = Path(__file__).resolve().parent.parent
    AUDIO_UPLOAD_DIR = BASE_DIR / "app" / "audio" / "uploads"
    OUTPUT_DIR = BASE_DIR / "data" / "processed"
    STATIC_DIR = BASE_DIR / "app" / "static"

    # Create directories
    AUDIO_UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Hardware
    DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
    
    # STT Settings (Whisper)
    WHISPER_MODEL_SIZE = "base"

    # LLM Settings (Ollama)
    OLLAMA_MODEL = "llama3:8b" # Make sure this matches your 'ollama list'
    OLLAMA_BASE_URL = "http://localhost:11434"

    # Image Gen Settings (Updated for SD 2.1)
    SD_MODEL_ID = "stabilityai/stable-diffusion-2-1"
    
    # Use bfloat16 if supported (Ampere GPUs+), otherwise float16
    TORCH_DTYPE = torch.bfloat16 if torch.cuda.is_bf16_supported() else torch.float16

config = Config()
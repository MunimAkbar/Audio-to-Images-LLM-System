import os
import torch

class Config:
    # Base Paths
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DATA_DIR = os.path.join(BASE_DIR, "data")
    OUTPUT_DIR = os.path.join(DATA_DIR, "images")
    AUDIO_UPLOAD_DIR = os.path.join(DATA_DIR, "uploads")
    STATIC_DIR = os.path.join(BASE_DIR, "app", "static")
    
    # Create directories if they don't exist
    os.makedirs(DATA_DIR, exist_ok=True)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    os.makedirs(AUDIO_UPLOAD_DIR, exist_ok=True)
    
    # Device
    DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

    # Model Settings
    WHISPER_MODEL_SIZE = "base"
    OLLAMA_MODEL = "llama3.2"
    OLLAMA_BASE_URL = "http://localhost:11434"
    SD_MODEL_ID = "runwayml/stable-diffusion-v1-5"
    TORCH_DTYPE = torch.float16 if DEVICE == "cuda" else torch.float32

config = Config()

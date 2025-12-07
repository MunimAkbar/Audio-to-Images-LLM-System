import uuid
import logging
import os
import torch
from app.config import config

# USE THESE RELATIVE IMPORTS
from .stt import SpeechToText
from .prompt_builder import PromptBuilder
from .image_gen import ImageGenerator

logger = logging.getLogger(__name__)

class Orchestrator:
    def __init__(self):
        # Initialize models once when server starts
        self.stt = SpeechToText()
        self.prompt_builder = PromptBuilder()
        self.image_gen = ImageGenerator()

    def process_audio(self, audio_file_path: str) -> dict:
        try:
            # 1. Transcribe
            transcribed_text = self.stt.transcribe(audio_file_path)
            
            # 2. Generate Prompt
            sd_prompt = self.prompt_builder.generate_prompt(transcribed_text)
            
            # Clear VRAM slightly before image gen if possible
            if config.DEVICE == "cuda":
                torch.cuda.empty_cache()

            # 3. Generate Image
            image_filename = f"{uuid.uuid4()}.png"
            output_path = os.path.join(config.OUTPUT_DIR, image_filename)
            
            self.image_gen.generate_image(sd_prompt, output_path)
            
            # Return relative path for the frontend to access
            relative_image_path = f"/images/{image_filename}"
            
            return {
                "transcribed_text": transcribed_text,
                "generated_prompt": sd_prompt,
                "image_url": relative_image_path
            }
        except Exception as e:
            logger.error(f"Pipeline failed: {str(e)}")
            raise e
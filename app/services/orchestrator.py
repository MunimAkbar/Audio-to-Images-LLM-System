import uuid
import os
import torch
from app.services.stt import SpeechToText
from app.services.prompt_builder import PromptBuilder
from app.services.image_gen import ImageGenerator
from app.config import config
import logging

logger = logging.getLogger(__name__)

class Orchestrator:
    def __init__(self):
        self.stt = SpeechToText()
        self.prompt_builder = PromptBuilder()
        # We initialize ImageGen later or keep it loaded depending on VRAM
        self.image_gen = ImageGenerator()

    def audio_to_prompt(self, audio_file_path: str) -> dict:
        """
        Step 1: Audio -> Text -> Prompt
        """
        try:
            # 1. Transcribe
            transcribed_text = self.stt.transcribe(audio_file_path)
            
            # 2. Generate Prompt
            sd_prompt = self.prompt_builder.generate_prompt(transcribed_text)
            
            return {
                "transcribed_text": transcribed_text,
                "generated_prompt": sd_prompt
            }
        except Exception as e:
            logger.error(f"Step 1 failed: {str(e)}")
            raise e

    def prompt_to_image(self, prompt: str) -> dict:
        """
        Step 2: Prompt -> Image
        """
        try:
            # Clear cache to help 4GB VRAM
            if config.DEVICE == "cuda":
                torch.cuda.empty_cache()

            image_filename = f"{uuid.uuid4()}.png"
            output_path = os.path.join(config.OUTPUT_DIR, image_filename)
            
            self.image_gen.generate_image(prompt, output_path)
            
            return {
                "image_url": f"/images/{image_filename}"
            }
        except Exception as e:
            logger.error(f"Step 2 failed: {str(e)}")
            raise e
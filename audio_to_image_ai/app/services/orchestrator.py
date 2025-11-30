import uuid
from app.core.stt import SpeechToText
from app.core.prompt_builder import PromptBuilder
from app.core.image_gen import ImageGenerator
from app.config import config
import logging
import os

logger = logging.getLogger(__name__)

class Orchestrator:
    def __init__(self):
        self.stt = SpeechToText()
        self.prompt_builder = PromptBuilder()
        self.image_gen = ImageGenerator()

    def process_audio(self, audio_file_path: str) -> dict:
        """
        Runs the full pipeline: Audio -> Text -> Prompt -> Image
        """
        try:
            # 1. Transcribe Audio
            transcribed_text = self.stt.transcribe(audio_file_path)
            
            # 2. Generate Prompt
            sd_prompt = self.prompt_builder.generate_prompt(transcribed_text)
            
            # 3. Generate Image
            image_filename = f"{uuid.uuid4()}.png"
            output_path = os.path.join(config.OUTPUT_DIR, image_filename)
            self.image_gen.generate_image(sd_prompt, output_path)
            
            return {
                "transcribed_text": transcribed_text,
                "generated_prompt": sd_prompt,
                "image_path": str(output_path)
            }
        except Exception as e:
            logger.error(f"Pipeline failed: {str(e)}")
            raise e

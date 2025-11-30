import whisper
from app.config import config
import logging

logger = logging.getLogger(__name__)

class SpeechToText:
    def __init__(self):
        logger.info(f"Loading Whisper model: {config.WHISPER_MODEL_SIZE} on {config.DEVICE}")
        self.model = whisper.load_model(config.WHISPER_MODEL_SIZE, device=config.DEVICE)

    def transcribe(self, audio_path: str) -> str:
        """
        Transcribes audio file to text.
        """
        try:
            logger.info(f"Transcribing audio: {audio_path}")
            result = self.model.transcribe(audio_path)
            text = result["text"].strip()
            logger.info(f"Transcription successful: {text[:50]}...")
            return text
        except Exception as e:
            logger.error(f"Error during transcription: {str(e)}")
            raise e

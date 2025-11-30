from diffusers import StableDiffusionPipeline
import torch
from app.config import config
import logging
from PIL import Image

logger = logging.getLogger(__name__)

class ImageGenerator:
    def __init__(self):
        logger.info(f"Loading Stable Diffusion model: {config.SD_MODEL_ID} on {config.DEVICE}")
        
        dtype = torch.float16 if config.USE_FP16 and config.DEVICE == "cuda" else torch.float32
        
        try:
            self.pipe = StableDiffusionPipeline.from_pretrained(
                config.SD_MODEL_ID, 
                torch_dtype=dtype
            )
            self.pipe.to(config.DEVICE)
            # Enable memory optimizations if using CUDA
            if config.DEVICE == "cuda":
                self.pipe.enable_attention_slicing()
        except Exception as e:
            logger.error(f"Failed to load Stable Diffusion model: {e}")
            raise e

    def generate_image(self, prompt: str, output_path: str) -> str:
        """
        Generates an image from a prompt and saves it.
        """
        try:
            logger.info(f"Generating image for prompt: {prompt}")
            image = self.pipe(prompt).images[0]
            
            image.save(output_path)
            logger.info(f"Image saved to: {output_path}")
            return output_path
        except Exception as e:
            logger.error(f"Error during image generation: {str(e)}")
            raise e

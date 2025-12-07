import torch
from diffusers import StableDiffusionPipeline, DPMSolverMultistepScheduler
from app.config import config
import logging

logger = logging.getLogger(__name__)

class ImageGenerator:
    def __init__(self):
        logger.info(f"Loading SD Model: {config.SD_MODEL_ID} on {config.DEVICE}")
        
        try:
            # 1. Load Pipeline
            self.pipe = StableDiffusionPipeline.from_pretrained(
                config.SD_MODEL_ID, 
                torch_dtype=config.TORCH_DTYPE
            )
            
            # 2. Configure Scheduler (as requested)
            self.pipe.scheduler = DPMSolverMultistepScheduler.from_config(
                self.pipe.scheduler.config
            )
            
            # 3. Move to GPU
            self.pipe = self.pipe.to(config.DEVICE)
            
            # 4. Optimization
            self.pipe.enable_attention_slicing()
            
        except Exception as e:
            logger.error(f"Failed to load Stable Diffusion model: {e}")
            raise e

    def generate_image(self, prompt: str, output_path: str):
        """
        Generates an image using the configured pipeline options.
        """
        try:
            logger.info(f"Generating image for prompt: {prompt}")
            
            # Run inference with specific parameters
            results = self.pipe(
                prompt,
                num_inference_steps=50,
                guidance_scale=7.5, # 3.5 is usually too low for SD 2.1, bumped to 7.5
                height=768, # SD 2.1 defaults to 768x768 usually, but 512 works too
                width=768
            )
            
            image = results.images[0]
            image.save(output_path)
            logger.info(f"Image saved to: {output_path}")
            
            return output_path
            
        except Exception as e:
            logger.error(f"Error during image generation: {str(e)}")
            raise e
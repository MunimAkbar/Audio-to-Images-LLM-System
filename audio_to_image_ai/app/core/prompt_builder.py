from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate
from app.config import config
import logging

logger = logging.getLogger(__name__)

class PromptBuilder:
    def __init__(self):
        logger.info(f"Initializing Ollama with model: {config.OLLAMA_MODEL}")
        self.llm = OllamaLLM(
            model=config.OLLAMA_MODEL,
            base_url=config.OLLAMA_BASE_URL
        )
        
        self.prompt_template = PromptTemplate(
            input_variables=["text"],
            template="""
            You are an expert AI art prompt generator. Your task is to take the following transcribed text and convert it into a highly detailed, creative, and effective prompt for Stable Diffusion.
            
            Transcribed Text: "{text}"
            
            Instructions:
            1. Extract the main subject and action.
            2. Add artistic style details (e.g., "cinematic lighting", "hyperrealistic", "oil painting", "cyberpunk", "studio ghibli style").
            3. Add quality boosters (e.g., "4k", "8k", "high resolution", "detailed texture").
            4. Keep the output as a single comma-separated string of keywords and phrases.
            5. Do NOT include any conversational text, just the prompt.
            
            Stable Diffusion Prompt:
            """
        )
        self.chain = self.prompt_template | self.llm

    def generate_prompt(self, text: str) -> str:
        """
        Generates a Stable Diffusion prompt from input text.
        """
        try:
            logger.info(f"Generating prompt for text: {text[:50]}...")
            response = self.chain.invoke({"text": text})
            cleaned_prompt = response.strip()
            logger.info(f"Generated prompt: {cleaned_prompt}")
            return cleaned_prompt
        except Exception as e:
            logger.error(f"Error during prompt generation: {str(e)}")
            raise e

import sys
import os

# Add the project root to the python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.services.orchestrator import Orchestrator
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)

def test_pipeline():
    print("Initializing Orchestrator...")
    try:
        orchestrator = Orchestrator()
    except Exception as e:
        print(f"Failed to initialize Orchestrator: {e}")
        return

    # Create a dummy audio file for testing if one doesn't exist
    # For a real test, we'd need a real audio file. 
    # Here we will just check if components loaded correctly.
    print("Orchestrator initialized successfully.")
    print("Components loaded:")
    print(f"- STT Model: {orchestrator.stt.model}")
    print(f"- LLM Chain: {orchestrator.prompt_builder.chain}")
    print(f"- Image Gen Pipe: {orchestrator.image_gen.pipe}")
    
    print("\nTo test with a real file, place an audio file in 'data/raw' and run:")
    print("orchestrator.process_audio('path/to/audio.wav')")

if __name__ == "__main__":
    test_pipeline()

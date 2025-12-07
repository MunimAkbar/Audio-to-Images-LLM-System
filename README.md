# Audio to Image AI

This project is an AI-powered application that converts audio input into generated images. It leverages a pipeline of state-of-the-art models:
1.  **Speech-to-Text (STT):** Uses OpenAI's **Whisper** to transcribe audio to text.
2.  **Prompt Generation:** Uses **Llama 3** (via Ollama) to refine the transcribed text into a descriptive image generation prompt.
3.  **Image Generation:** Uses **Stable Diffusion** to generate an image based on the refined prompt.

## Features

-   **Audio Transcription:** Accurate speech-to-text using Whisper.
-   **Intelligent Prompting:** Enhances simple audio descriptions into detailed artistic prompts using Llama 3.
-   **Image Synthesis:** High-quality image generation with Stable Diffusion.
-   **REST API:** FastAPI-based backend for easy integration.

## Prerequisites

Before running the project, ensure you have the following installed:

-   **Python 3.8+**
-   **Ollama:** Required for running the Llama 3 model locally.
    -   Install Ollama from [ollama.com](https://ollama.com/).
    -   Pull the Llama 3 model: `ollama pull llama3:8b`
-   **FFmpeg:** Required by Whisper for audio processing.
    -   **Windows:** `winget install ffmpeg` or download from [ffmpeg.org](https://ffmpeg.org/).
    -   **Linux:** `sudo apt install ffmpeg`
    -   **macOS:** `brew install ffmpeg`
-   **CUDA (Optional but Recommended):** For GPU acceleration with PyTorch.

## Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd audio_to_image_ai
    ```

2.  **Create a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Configuration

Configuration settings can be modified in `app/config.py`. Key settings include:

-   `WHISPER_MODEL_SIZE`: Model size for Whisper (default: `base`).
-   `OLLAMA_MODEL`: LLM model to use (default: `llama3:8b`).
-   `SD_MODEL_ID`: Stable Diffusion model ID (default: `runwayml/stable-diffusion-v1-5`).
-   `DEVICE`: Automatically detects `cuda` or `cpu`.

## Usage

### Running the API Server

Start the FastAPI server:

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`.
Access the interactive API documentation at `http://localhost:8000/docs`.

### Testing the Pipeline

You can verify the pipeline components using the provided test script:

```bash
python test_pipeline.py
```

This script initializes the orchestrator and checks if all models (Whisper, Ollama, Stable Diffusion) load correctly.

## Project Structure

```
audio_to_image_ai/
├── app/
│   ├── api/            # API routes and endpoints
│   ├── services/       # Core logic (Orchestrator, STT, LLM, ImageGen)
│   ├── utils/          # Utility functions
│   ├── config.py       # Configuration settings
│   └── main.py         # Application entry point
├── data/               # Data storage (uploads, processed images)
├── docker/             # Docker configuration
├── requirements.txt    # Python dependencies
└── test_pipeline.py    # Pipeline verification script
```

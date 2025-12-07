# Audio to Image AI

This project is an AI-powered application that converts audio input into generated images. It orchestrates a pipeline of state-of-the-art models to transcribe speech, refine prompts, and generate artistic visuals.

## Features

-   **Audio Transcription:** Accurate speech-to-text using **OpenAI Whisper** (Default: `base` model).
-   **Intelligent Prompting:** Enhances simple audio descriptions into detailed artistic prompts using **Llama 3.2** (via Ollama).
-   **Image Synthesis:** High-quality image generation with **Stable Diffusion v1.5**.
-   **REST API:** FastAPI-based backend with an integrated web interface.

## Project Structure

```
audio_to_image_ai/
├── app/
│   ├── api/            # API routes and endpoints
│   ├── audio/          # Storage for uploaded audio
│   ├── services/       # Core logic (Orchestrator, STT, LLM, ImageGen)
│   ├── static/         # Frontend access (HTML/JS/CSS)
│   ├── utils/          # Utility functions
│   ├── config.py       # Configuration settings
│   └── main.py         # Application entry point
├── data/               # Data storage (processed images)
├── docker/             # Docker configuration
├── requirements.txt    # Python dependencies
└── test_pipeline.py    # Pipeline verification script
```

## Prerequisites

Before running the project, ensure you have the following installed:

-   **Python 3.8+**
-   **Ollama:** Required for running the Llama 3.2 model locally.
    -   Install Ollama from [ollama.com](https://ollama.com/).
    -   Pull the model: `ollama pull llama3.2`
-   **FFmpeg:** Required by Whisper for audio processing.
    -   **Windows:** `winget install ffmpeg` or download from [ffmpeg.org](https://ffmpeg.org/).
    -   **Linux:** `sudo apt install ffmpeg`
    -   **macOS:** `brew install ffmpeg`
-   **CUDA (Optional but Recommended):** For GPU acceleration with PyTorch.

## Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd audio_to_image_LLMsystem
    ```

2.  **Create a virtual environment:**
    ```bash
    python -m venv venv
    # Windows:
    venv\Scripts\activate
    # Linux/macOS:
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Configuration

Configuration settings can be modified in `app/config.py`. Key settings include:

-   `WHISPER_MODEL_SIZE`: Model size for Whisper (default: `base`).
-   `OLLAMA_MODEL`: LLM model to use (default: `llama3.2`).
-   `SD_MODEL_ID`: Stable Diffusion model ID (default: `runwayml/stable-diffusion-v1-5`).
-   `DEVICE`: Automatically detects `cuda` or `cpu`.

## Usage

### Running the Application

Start the FastAPI server:

```bash
uvicorn app.main:app --reload
```

-   **Web Interface:** Open `http://localhost:8000` in your browser to use the application.
-   **API Documentation:** Access the interactive API docs at `http://localhost:8000/docs`.

### Testing the Pipeline

You can verify that all components (Whisper, Ollama, Stable Diffusion) are correctly configured and loaded using the test script:

```bash
python test_pipeline.py
```

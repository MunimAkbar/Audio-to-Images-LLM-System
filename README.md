# 🎧🎨 Audio-to-Image AI  
Convert audio → text → artistic prompt → image automatically.

This project implements a full pipeline that converts user audio into text, generates an artistic prompt, and produces an image using state-of-the-art AI models.

---

## 📁 Project Structure

audio_to_image_ai/
├── app/
│ ├── api/ # FastAPI routes
│ ├── core/ # Core logic (STT, Prompt Builder, Image Gen)
│ ├── services/ # Pipeline Orchestrator
│ ├── utils/ # Utility functions
│ └── audio/uploads/ # Uploaded audio files
├── data/
└── ...


---

## ⚙️ Core Components

### **Speech-to-Text (stt.py)**
- Uses **OpenAI Whisper** to convert audio into text.

### **Prompt Builder (prompt_builder.py)**
- Uses **LangChain + Ollama (llama3:8b)** to generate creative prompts from transcribed text.

### **Image Generator (image_gen.py)**
- Uses **Diffusers (Stable Diffusion)** to create images from prompts.

### **Pipeline Orchestrator (orchestrator.py)**
- Connects all components:  
  **Audio → STT → Prompt → Image**

---

## 🚀 API

### **POST /generate**
- Accepts audio file  
- Returns generated image + prompt

### **Entry Point**

python -m app.main

---

## 🧪 Testing the Pipeline

python test_pipeline.py


---

## ▶️ How to Run Locally

### **1. Create and Activate Virtual Environment**

python -m venv venv

**Windows**

.\venv\Scripts\activate

**Linux/Mac**

source venv/bin/activate

### **2. Install Dependencies**

pip install -r requirements.txt

### **3. Start FastAPI Server**

python -m app.main


---

## 🐳 Docker Usage

### **Build Image**

docker build -f docker/Dockerfile -t audio-to-image .

### **Run Container**

docker run -p 8000:8000 audio-to-image


> **Note:**  
> To access a local Ollama instance from Docker, you may need:
> - `--network host` (Linux)  
> - or set  
>   `OLLAMA_BASE_URL=http://host.docker.internal:11434` (Windows/Mac)

---

## ⚠️ Requirements

- **Ollama** installed locally with:

ollama pull llama3:8b

- **GPU recommended** for optimal performance  
(Whisper STT, Llama prompt generation, Stable Diffusion image generation).

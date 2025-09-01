# 🎙️ AI Voice Agent

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green.svg)](https://fastapi.tiangolo.com/)
[![AssemblyAI](https://img.shields.io/badge/AssemblyAI-STT-orange.svg)](https://www.assemblyai.com/)
[![Google Gemini](https://img.shields.io/badge/Google-Gemini%202.5%20Flash-red.svg)](https://ai.google.dev/)
[![Murf TTS](https://img.shields.io/badge/Murf-TTS-purple.svg)](https://murf.ai/)

## Table of Contents
- [Project Overview](#project-overview)
- [Technologies Used](#technologies-used)
- [Architecture](#architecture)
- [Key Features](#key-features)
- [Project Structure](#project-structure)
- [Running the AI Voice Agent](#running-the-ai-voice-agent--api-server)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

## Project Overview
The AI Voice Agent is a web-based conversational assistant that lets you speak naturally, processes your voice in real time, and replies with synthesized speech—all in a single-page, responsive interface. Built as part of the **#30DaysOfAIVoiceAgents** challenge, the project demonstrates seamless integration of speech-to-text, large-language modeling, and text-to-speech services to create an end-to-end voice experience.

Every interaction feels fluid: you press a single button to record, the backend pipelines your audio through transcription and LLM services, and you immediately hear a spoken reply without needing to refresh or navigate away.

[🚀 Live Demo](https://your-github-repo-link) | [📖 Documentation](https://github.com/your-username/Ai_Voice_Agent/wiki)

---
## Technologies Used

| Layer       | Technology                   | Purpose                                     |
|-------------|------------------------------|---------------------------------------------|
| Frontend    | HTML · CSS · JavaScript      | Audio capture, UI rendering, and interactivity |
| Backend     | FastAPI · Python · httpx     | REST endpoints, async HTTP requests         |
| STT         | AssemblyAI                   | Speech-to-text transcription                |
| LLM         | Google Gemini 2.5 Flash      | Multi-turn conversational intelligence      |
| TTS         | Murf TTS                     | High-quality text-to-speech synthesis       |
| Dev Tools   | Uvicorn · python-dotenv      | Local server hosting and environment management |

---
## Architecture
```
Browser UI
  └─ Record button captures WebM audio stream
      ↓
FastAPI Server
  ├─ Uploads audio to AssemblyAI (polling for transcript)
  ├─ Sends transcript + chat history to Gemini LLM
  └─ Forwards Gemini’s text reply to Murf TTS
      ↓
Murf TTS returns MP3 audio
  └─ Browser auto-plays response and updates chat history
```
- Audio files are temporarily stored under `uploads/` for asynchronous processing.
- All network calls are non-blocking, leveraging `async`/`await` to keep the UI snappy.
- Chat state (user prompts + AI replies) is stored in memory per session for multi-turn context.
---
## How It Works
1. **User Interaction**: Click the record button to start capturing audio from the microphone.
2. **Audio Processing**: The audio is sent to AssemblyAI for transcription, which returns text in real-time.
3. **AI Response Generation**: The transcribed text, along with chat history, is sent to Google Gemini 2.5 Flash for generating a contextual response.
4. **Speech Synthesis**: The AI's text response is converted to audio using Murf TTS.
5. **Playback and Display**: The audio plays automatically, and the conversation is appended to the chat history on the page.
6. **Error Handling**: If any service fails, a fallback audio is played, and an error message is shown.

This seamless pipeline ensures a natural voice interaction without page reloads.
---
## Key Features
- **Single-Button Recording**  
  A unified “Start / Stop / Processing” control with animated feedback and status indicators.
- **Real-Time Transcription**  
  High-accuracy speech-to-text powered by AssemblyAI, streamed back to the UI as soon as it’s ready.
- **Multi-Turn Conversation**  
  Maintains context across exchanges with Google’s Gemini 2.5 Flash model to deliver coherent, follow-up responses.
- **Text-to-Speech Playback**  
  Converts AI replies into natural-sounding audio via Murf TTS and auto-plays them in the browser.
- **Weather Detection and Integration**  
  Advanced weather query detection and real-time weather data fetching for location-based responses.
- **Persona Support**  
  Customizable AI personas for different interaction styles and personalities.
- **Graceful Fallbacks**  
  Detects API failures or missing keys, displays informative messages, and plays a built-in fallback audio clip.
- **Persistent Chat History**  
  Dynamically appends each question and reply to the page, allowing you to review the conversation until page refresh.
- **Animated, Gradient UI**  
  Clean, minimal layout with subtle animations, gradient backgrounds, and responsive design for all devices.
- **Extensive Testing Suite**  
  Comprehensive test files for API keys, weather detection, personas, and overall functionality.
---
## Project Structure
```
Ai_Voice_Agent-main/
├── .gitignore
├── llm.py
├── main.py
├── personas.py
├── README.md
├── render.yaml
├── requirements.txt
├── schemas.py
├── stt.py
├── test_api_key.py
├── test_enhanced_weather_detection.py
├── test_persona.py
├── test_weather_detection.py
├── test_weather_real.py
├── test_weather.py
├── TESTING_QUESTIONS.md
├── TODO_API_KEYS.md
├── TODO.md
├── tts.py
├── vercel.json
├── weather.py
├── services/
├── static/
│   ├── fallback.mp3
│   ├── index.html
│   ├── recorder.js
│   └── style.css
└── uploads/
```
- **services/**: Contains modules for STT, LLM, and TTS services.
- **static/**: Frontend files including HTML, CSS, JS, and fallback audio.
- **uploads/**: Directory for temporary audio file storage (auto-created).
- **Test files**: Various test scripts for API keys, weather detection, personas, etc.
- **Configuration files**: .env, requirements.txt, vercel.json for deployment.
---
## API Endpoints
- `GET /`: Serves the main HTML page.
- `POST /transcribe`: Uploads audio and returns transcription.
- `POST /chat`: Processes chat with LLM and returns response.
- `POST /tts`: Converts text to speech and returns audio URL.

For detailed API docs, see [API Documentation](https://github.com/your-username/Ai_Voice_Agent/wiki/API).

---
# ⚙️ Running the AI Voice Agent & API Server
Follow these steps to set up, configure, and run the complete voice-agent stack on your local machine.
---
## 1. Clone or Prepare Project Files
1. Place all project files in a single folder on your machine.
2. Verify the structure matches the [Project Structure](#project-structure) above.
---
## 2. Create & Activate a Python Virtual Environment
```bash
# macOS / Linux
python3 -m venv venv
source venv/bin/activate
# Windows (PowerShell)
python -m venv venv
.\venv\Scripts\Activate.ps1
```
---
## 3. Install Dependencies
```bash
pip install -r requirements.txt
```
This will install:
- fastapi  
- uvicorn  
- httpx  
- python-dotenv  
- any other listed packages
---
## 4. Set Environment Variables
Create a file named `.env` in your project’s root directory with **all** the following keys:
```
ASSEMBLY_API_KEY=your_assemblyai_key
GEMINI_API_KEY=your_gemini_key
MURF_API_KEY=your_murf_key
```
• ASSEMBLY_API_KEY: AssemblyAI transcription API key  
• GEMINI_API_KEY: Google Gemini LLM API key  
• MURF_API_KEY: Murf TTS API key  
---
## 5. Verify Fallback Audio
Ensure the fallback file lives at `static/fallback.mp3`. This clip plays automatically if any external service fails.
---
## 6. Launch the Server
```bash
uvicorn main:app --reload
```
- The `--reload` flag watches for code changes and restarts automatically.  
- By default, the API will be available at `http://localhost:8000`.
---
## 7. Use the App
1. Open your browser to `http://localhost:8000`.  
2. Click the central record button to Start → Stop → Processing.  
3. Watch your speech transcribe, then hear the AI reply instantly.  
4. Scroll through the persistent chat history on the same page.  
---
# ▶️ Next Steps & Tips
- To test error handling, temporarily remove or invalidate one of the keys in `.env`.  
- For production, consider:
  - Adding HTTPS (e.g., via Traefik or NGINX)  
  - Deploying on a cloud VM or container platform  
  - Persisting chat history in a lightweight database (SQLite, Redis)  
  - Customizing UI themes or swapping in alternative voices  
Feel free to iterate, share your tweaks on LinkedIn, and keep building on this modular foundation!

## Contributing
We welcome contributions! Please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and test thoroughly.
4. Submit a pull request with a clear description of your changes.

For major changes, please open an issue first to discuss what you would like to change.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


# main.py
import os
import logging
from pathlib import Path

from dotenv import load_dotenv
from fastapi import FastAPI, UploadFile, File, HTTPException, Request
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from schemas import AudioResponse, PersonaResponse, SetPersonaRequest
from personas import PERSONAS
from stt import transcribe_audio
from llm import generate_llm_response
from tts import synthesize_speech

# ---------- Setup ----------
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
load_dotenv()

app = FastAPI()

# API keys
ASSEMBLY_API_KEY = os.getenv("ASSEMBLY_API_KEY")
MURF_API_KEY     = os.getenv("MURF_API_KEY")
GEMINI_API_KEY   = os.getenv("GEMINI_API_KEY")
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY", "your_openweather_key")

if not ASSEMBLY_API_KEY or not MURF_API_KEY or not GEMINI_API_KEY:
    raise RuntimeError("Missing API keys in .env")

# Static files & uploads folder
UPLOADS_DIR = Path("uploads")
UPLOADS_DIR.mkdir(exist_ok=True)
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def serve_frontend():
    return FileResponse("static/index.html")

# ---------- Multi-Turn Memory ----------
conversation_history = {}
persona_selections = {}  # Store persona selection per session

@app.get("/personas", response_model=PersonaResponse)
async def get_personas():
    """Get list of available personas"""
    personas_list = [{"name": key, **value} for key, value in PERSONAS.items()]
    return PersonaResponse(personas=personas_list)

@app.post("/persona")
async def set_persona(request: Request, persona_request: SetPersonaRequest):
    """Set persona for current session"""
    session_id = request.client.host
    persona_name = persona_request.persona_name
    
    if persona_name not in PERSONAS:
        raise HTTPException(status_code=400, detail="Persona not found")
    
    persona_selections[session_id] = persona_name
    return {"message": f"Persona set to {persona_name}", "persona": PERSONAS[persona_name]}

@app.post("/llm/query", response_model=AudioResponse)
async def llm_query(request: Request, audio: UploadFile = File(...)):
    session_id = request.client.host
    audio_path = UPLOADS_DIR / "input.wav"

    with open(audio_path, "wb") as f:
        f.write(await audio.read())

    try:
        transcript = await transcribe_audio(audio_path, ASSEMBLY_API_KEY)
        
        # Get persona for this session (default to "default" if not set)
        persona_name = persona_selections.get(session_id, "default")
        
        llm_text = await generate_llm_response(
            transcript, 
            session_id, 
            GEMINI_API_KEY, 
            conversation_history,
            persona_name,
            OPENWEATHER_API_KEY
        )
        audio_url = await synthesize_speech(llm_text, MURF_API_KEY)
    except Exception as e:
        logger.exception("Processing failed")
        raise HTTPException(status_code=500, detail=str(e))

    return AudioResponse(
        transcript=transcript,
        llm_text=llm_text,
        audio_url=audio_url
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

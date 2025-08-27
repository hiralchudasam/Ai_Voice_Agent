import httpx
import logging
import re
from personas import PERSONAS
from weather import get_weather

logger = logging.getLogger(__name__)

def is_weather_query(text: str) -> bool:
    """Check if the user is asking about weather"""
    weather_patterns = [
        r"weather.*in.*",
        r"temperature.*in.*",
        r"how.*weather.*",
        r"what.*weather.*",
        r"forecast.*",
        r"climate.*in.*",
        r"humidity.*in.*",
        r"is it.*outside",
        r"how hot.*",
        r"how cold.*",
        r"what.*temperature.*",
        r"tell me.*weather.*",
        r"give me.*forecast.*",
        r"how.*humid.*",
        r"current weather.*",
        r"current temperature.*"
    ]
    
    text_lower = text.lower()
    for pattern in weather_patterns:
        if re.search(pattern, text_lower):
            return True
    return False

def extract_location(text: str) -> str:
    """Extract location from weather query"""
    patterns = [
        r"weather in ([\w\s,]+)",
        r"temperature in ([\w\s,]+)",
        r"forecast for ([\w\s,]+)",
        r"forecast in ([\w\s,]+)",
        r"how.*weather in ([\w\s,]+)",
        r"what.*weather in ([\w\s,]+)",
        r"climate in ([\w\s,]+)",
        r"humidity in ([\w\s,]+)",
        r"temperature for ([\w\s,]+)"
    ]
    
    text_lower = text.lower()
    for pattern in patterns:
        match = re.search(pattern, text_lower)
        if match:
            location = match.group(1).strip()
            # Capitalize the first letter of each word for better presentation
            return " ".join(word.capitalize() for word in location.split())
    
    # If no specific pattern matches, try to extract any location-like words
    words = text.split()
    location_keywords = ["in", "at", "for", "of"]
    for i, word in enumerate(words):
        if word.lower() in location_keywords and i + 1 < len(words):
            location = " ".join(words[i+1:]).replace("?", "").strip()
            return " ".join(word.capitalize() for word in location.split())
    
    return ""

async def generate_llm_response(transcript: str, session_id: str, api_key: str, history: dict, persona_name: str = "default", openweather_api_key: str = "") -> str:
    if session_id not in history:
        history[session_id] = []
        
    # Get persona system prompt
    persona = PERSONAS.get(persona_name, PERSONAS["default"])
    
    # Check if this is the first message in conversation, add system prompt
    if len(history[session_id]) == 0:
        history[session_id].append({
            "role": "user", 
            "parts": [{"text": f"System: {persona['system_prompt']}"}]
        })

    # Check if this is a weather query
    if is_weather_query(transcript):
        location = extract_location(transcript)
        if location:
            weather_info = await get_weather(location, openweather_api_key)
            if weather_info:
                # Add weather response to history
                history[session_id].append({"role": "user", "parts": [{"text": transcript}]})
                history[session_id].append({"role": "model", "parts": [{"text": weather_info}]})
                return weather_info
            else:
                # Weather API failed, let Gemini handle it normally
                pass

    history[session_id].append({"role": "user", "parts": [{"text": transcript}]})

    gemini_url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent"
    async with httpx.AsyncClient(timeout=20) as client:
        llm_resp = await client.post(
            gemini_url,
            json={"contents": history[session_id]},
            headers={"Content-Type": "application/json"},
            params={"key": api_key}
        )
    llm_resp.raise_for_status()
    candidate = llm_resp.json()["candidates"][0]
    llm_text = candidate["content"]["parts"][0]["text"]

    history[session_id].append({"role": "model", "parts": [{"text": llm_text}]})
    return llm_text

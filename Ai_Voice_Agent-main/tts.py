import httpx
import logging

logger = logging.getLogger(__name__)

async def synthesize_speech(text: str, api_key: str) -> str:
    """
    Synthesize speech using Murf TTS API with fallback to local audio file
    """
    # Fallback audio URL for when TTS service fails
    FALLBACK_AUDIO_URL = "/static/fallback.mp3"
    
    # If no API key is provided, use fallback immediately
    if not api_key or api_key == "your_murf_key":
        logger.warning("No valid Murf API key provided, using fallback audio")
        return FALLBACK_AUDIO_URL
    
    payload = {
        "text": text,
        "voice_id": "en-IN-alia",
        "audio_format": "mp3"
    }
    
    try:
        async with httpx.AsyncClient(timeout=30) as client:
            resp = await client.post(
                "https://api.murf.ai/v1/speech/generate",
                json=payload,
                headers={"api-key": api_key, "Content-Type": "application/json"}
            )
        resp.raise_for_status()
        data = resp.json()
        
        # Return the audio URL from the response
        audio_url = data.get("audioFile") or data.get("audio_url")
        if audio_url:
            return audio_url
        else:
            logger.warning("No audio URL in Murf API response, using fallback")
            return FALLBACK_AUDIO_URL
            
    except httpx.HTTPStatusError as e:
        logger.error(f"Murf API HTTP error: {e.response.status_code} - {e.response.text}")
        return FALLBACK_AUDIO_URL
    except httpx.RequestError as e:
        logger.error(f"Murf API request error: {str(e)}")
        return FALLBACK_AUDIO_URL
    except Exception as e:
        logger.error(f"Unexpected error in TTS synthesis: {str(e)}")
        return FALLBACK_AUDIO_URL

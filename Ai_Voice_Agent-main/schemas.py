from pydantic import BaseModel, Field
from typing import List


class AudioResponse(BaseModel):
    transcript: str
    llm_text: str
    audio_url: str

class Persona(BaseModel):
    name: str
    description: str
    system_prompt: str

class PersonaResponse(BaseModel):
    personas: List[Persona] = Field(..., description="List of available personas")
    
class SetPersonaRequest(BaseModel):
    persona_name: str = Field(..., description="Name of the persona to set for the session")

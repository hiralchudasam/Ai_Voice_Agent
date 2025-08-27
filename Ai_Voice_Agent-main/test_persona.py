#!/usr/bin/env python3
"""
Test script to verify persona functionality
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from personas import PERSONAS
from schemas import Persona, PersonaResponse, SetPersonaRequest

def test_personas():
    """Test that personas are properly configured"""
    print("Testing persona configuration...")
    
    # Test that all personas have required fields
    for persona_name, persona_data in PERSONAS.items():
        assert 'name' in persona_data, f"Persona {persona_name} missing name"
        assert 'description' in persona_data, f"Persona {persona_name} missing description"
        assert 'system_prompt' in persona_data, f"Persona {persona_name} missing system_prompt"
        print(f"✓ {persona_name}: {persona_data['name']}")
    
    print("All personas configured correctly!")

def test_schemas():
    """Test that schemas work correctly"""
    print("\nTesting schemas...")
    
    # Test Persona schema
    persona = Persona(name="Test", description="Test persona", system_prompt="Test prompt")
    assert persona.name == "Test"
    
    # Test PersonaResponse schema
    personas_list = [Persona(name="Test", description="Test", system_prompt="Test")]
    response = PersonaResponse(personas=personas_list)
    assert len(response.personas) == 1
    
    # Test SetPersonaRequest schema
    request = SetPersonaRequest(persona_name="default")
    assert request.persona_name == "default"
    
    print("All schemas working correctly!")

if __name__ == "__main__":
    test_personas()
    test_schemas()
    print("\n✅ All persona tests passed!")

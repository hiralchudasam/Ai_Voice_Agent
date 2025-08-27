#!/usr/bin/env python3
"""
Test script to verify OpenWeatherMap API key is loaded correctly
"""
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get the API key
api_key = os.getenv("OPENWEATHER_API_KEY")

print(f"OPENWEATHER_API_KEY: {api_key}")
print(f"Key length: {len(api_key) if api_key else 0} characters")
print(f"Is key placeholder: {api_key == 'your_openweather_key' if api_key else 'No key'}")

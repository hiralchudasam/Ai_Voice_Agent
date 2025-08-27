#!/usr/bin/env python3
"""
Test script to verify weather functionality with real API key
"""
import os
import asyncio
from dotenv import load_dotenv
from weather import get_weather

# Load environment variables
load_dotenv()

# Get the API key
api_key = os.getenv("OPENWEATHER_API_KEY")

async def test_weather_with_real_key():
    print(f"Testing weather with API key: {api_key[:10]}... (truncated)")
    
    # Test with a simple location
    result = await get_weather("New York", api_key)
    print(f"Weather result: {result}")
    
    # Test with another location
    result2 = await get_weather("London", api_key)
    print(f"Weather result 2: {result2}")

if __name__ == "__main__":
    asyncio.run(test_weather_with_real_key())

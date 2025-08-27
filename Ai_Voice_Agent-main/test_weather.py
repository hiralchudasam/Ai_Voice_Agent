#!/usr/bin/env python3
"""
Test script for the weather functionality
"""
import asyncio
import sys
import os

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from weather import get_weather

async def test_weather():
    """Test the weather functionality"""
    # Test with a placeholder API key (will use fallback to Gemini)
    test_api_key = "your_openweather_key"
    
    # Test locations
    test_locations = [
        "New York",
        "London",
        "Tokyo",
        "Paris"
    ]
    
    print("Testing weather functionality...")
    print("=" * 50)
    
    for location in test_locations:
        print(f"\nTesting weather for: {location}")
        result = await get_weather(location, test_api_key)
        
        if result is None:
            print(f"✓ Weather service returned None (expected with placeholder API key)")
            print(f"  This means the query will be handled by Gemini instead")
        else:
            print(f"✓ Weather data received:")
            print(f"  {result}")
    
    print("\n" + "=" * 50)
    print("Weather functionality test completed!")

if __name__ == "__main__":
    asyncio.run(test_weather())

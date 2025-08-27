#!/usr/bin/env python3
"""
Test script for weather query detection
"""
import sys
import os

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from llm import is_weather_query, extract_location

def test_weather_detection():
    """Test weather query detection"""
    test_queries = [
        ("What's the weather like in New York?", True, "New York"),
        ("How's the temperature in London?", True, "London"),
        ("Tell me the forecast for Tokyo", True, "Tokyo"),
        ("What is the climate in Paris?", True, "Paris"),
        ("How humid is it in Miami?", True, "Miami"),
        ("Is it hot outside?", True, ""),
        ("How cold is it today?", True, ""),
        ("What's the weather like?", True, ""),
        ("Tell me a joke", False, ""),
        ("What time is it?", False, ""),
        ("How are you doing?", False, ""),
        ("What's the capital of France?", False, ""),
    ]
    
    print("Testing weather query detection...")
    print("=" * 60)
    
    for query, expected_detection, expected_location in test_queries:
        is_weather = is_weather_query(query)
        location = extract_location(query) if is_weather else ""
        
        status = "✓" if is_weather == expected_detection else "✗"
        location_status = "✓" if location == expected_location else f"✗ (got: '{location}')"
        
        print(f"{status} Query: '{query}'")
        print(f"   Detection: {is_weather} (expected: {expected_detection})")
        if is_weather:
            print(f"   Location: {location_status} '{location}' (expected: '{expected_location}')")
        print()
    
    print("=" * 60)
    print("Weather detection test completed!")

if __name__ == "__main__":
    test_weather_detection()

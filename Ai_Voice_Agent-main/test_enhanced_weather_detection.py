#!/usr/bin/env python3
"""
Enhanced test script for weather query detection with new patterns
"""
import sys
import os
import unittest  # Import unittest

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from llm import is_weather_query, extract_location

class TestEnhancedWeatherDetection(unittest.TestCase):  # Create a test case class
    def test_enhanced_weather_detection(self):
        """Test enhanced weather query detection with new patterns"""
        test_queries = [
            # New patterns to test
            ("What's the wind speed in Chicago?", True, "Chicago"),
            ("How windy is it in Boston?", True, "Boston"),
            ("What's the visibility in Seattle?", True, "Seattle"),
            ("Is it raining in Miami?", True, "Miami"),
            ("Is it snowing in Denver?", True, "Denver"),
            ("Rain in Los Angeles?", True, "Los Angeles"),
            ("Snow in Minneapolis?", True, "Minneapolis"),
            ("Weather today in San Francisco?", True, "San Francisco"),
            ("Weather tomorrow in Austin?", True, "Austin"),
            ("Weather this week in Dallas?", True, "Dallas"),
            ("Weather report for Phoenix?", True, "Phoenix"),
            ("Temperature today in Houston?", True, "Houston"),
            ("Temperature tomorrow in Atlanta?", True, "Atlanta"),
            ("Wind in Portland?", True, "Portland"),
            ("Visibility in Detroit?", True, "Detroit"),
            
            # Non-weather queries
            ("Tell me about the stock market", False, ""),
            ("What's your favorite color?", False, ""),
            ("How to cook pasta?", False, ""),
            ("What is artificial intelligence?", False, ""),
        ]
        
        print("Testing enhanced weather query detection...")
        print("=" * 70)
        
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
        
        print("=" * 70)
        print("Enhanced weather detection test completed!")

if __name__ == "__main__":
    unittest.main()  # Run the tests

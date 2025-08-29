# Weather Skill Testing Questions

## Basic Weather Queries
1. "What's the weather like in New York?"
2. "How's the temperature in London?"
3. "Tell me the forecast for Tokyo"
4. "What is the climate in Paris?"
5. "How humid is it in Miami?"

## New Enhanced Weather Patterns
6. "What's the wind speed in Chicago?"
7. "How windy is it in Boston?"
8. "What's the visibility in Seattle?"
9. "Is it raining in Miami?"
10. "Is it snowing in Denver?"
11. "Rain in Los Angeles?"
12. "Snow in Minneapolis?"
13. "Weather today in San Francisco?"
14. "Weather tomorrow in Austin?"
15. "Weather this week in Dallas?"
16. "Weather report for Phoenix?"
17. "Temperature today in Houston?"
18. "Temperature tomorrow in Atlanta?"
19. "Wind in Portland?"
20. "Visibility in Detroit?"

## Location-Specific Variations
21. "What's the weather like?" (should detect weather but no location)
22. "How cold is it today?" (should detect weather but no location)
23. "Is it hot outside?" (should detect weather but no location)

## Edge Cases
24. "Weather in New York City, USA" (multi-word location)
25. "Temperature in London, UK" (country specification)
26. "Forecast for Tokyo, Japan" (country specification)
27. "What's the weather like in a place that doesn't exist?" (error handling)
28. "Weather in 12345" (invalid location)

## Non-Weather Queries (Should NOT trigger weather detection)
29. "Tell me a joke"
30. "What time is it?"
31. "How are you doing?"
32. "What's the capital of France?"
33. "Tell me about the stock market"
34. "What's your favorite color?"
35. "How to cook pasta?"
36. "What is artificial intelligence?"

## Testing Focus Areas:
- Verify weather detection works for all new patterns
- Check location extraction accuracy
- Test error handling for invalid locations
- Confirm temperature conversion displays both Celsius and Fahrenheit
- Ensure non-weather queries don't trigger weather functionality
- Test response format includes wind speed and visibility data

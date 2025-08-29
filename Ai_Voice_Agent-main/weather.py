import httpx
import logging
from typing import Optional

logger = logging.getLogger(__name__)

async def get_weather(location: str, api_key: str) -> Optional[str]:
    """
    Get weather information for a location using WeatherAPI
    """
    if not api_key or api_key == "your_openweather_key":
        return "Weather service is not configured. Please set up WeatherAPI key to get real weather data."
    
    try:
        url = "http://api.weatherapi.com/v1/current.json"
        async with httpx.AsyncClient(timeout=10) as client:
            response = await client.get(
                url,
                params={
                    "key": api_key,
                    "q": location
                }
            )
            response.raise_for_status()
            weather_data = response.json()
            
            if "error" in weather_data:
                return f"Error fetching weather data: {weather_data['error']['message']}"
            
            # Format the weather information
            temp = weather_data["current"]["temp_c"]
            description = weather_data["current"]["condition"]["text"]
            city = weather_data["location"]["name"]
            country = weather_data["location"]["country"]
            
            # Return only the requested information based on the query
            return (
                f"Current weather in {city}, {country}:\n"
                f"Temperature: {temp}°C\n"
                f"Conditions: {description.capitalize()}"
            )
            
    except httpx.HTTPStatusError as e:
        error_msg = f"Error fetching weather data: HTTP {e.response.status_code}"
        logger.error(error_msg)
        return error_msg
    except httpx.RequestError as e:
        error_msg = f"Network error connecting to weather service: {str(e)}"
        logger.error(error_msg)
        return error_msg
    except Exception as e:
        error_msg = f"Unexpected error getting weather: {str(e)}"
        logger.error(error_msg)
        return error_msg

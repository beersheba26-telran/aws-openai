tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get weather for a city",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {
                        "type": "string",
                        "description": "City name"
                    }
                },
                "required": ["city"]
            }
        }
    }
]
TOOL_FUNCTIONS={
    "get_weather":lambda city: get_weather(city)
}
def get_weather(city):
    # Mock implementation for testing
    weather_data = {
        "Rehovot": "Sunny, 25°C",
        "Tel Aviv": "Cloudy, 22°C",
        "Jerusalem": "Rainy, 18°C"
    }
    return weather_data.get(city, f"Weather data not available for {city}")


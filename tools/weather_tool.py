import requests
from strands import tool


def get_weather(city: str) -> dict:
    """
    Get current weather and a two-day forecast for an Indian city.

    Args:
        city: Name of the city in India.
    """

    try:
        # Step 1: Convert city name into coordinates
        geo_url = "https://geocoding-api.open-meteo.com/v1/search"

        geo_response = requests.get(
            geo_url,
            params={
                "name": city,
                "count": 10,
                "countryCode": "IN",
            },
            timeout=15,
        )
        geo_response.raise_for_status()

        locations = geo_response.json().get("results", [])

        if not locations:
            return {"error": f"City '{city}' not found in India."}

        location = locations[0]

        latitude = location["latitude"]
        longitude = location["longitude"]

        # Step 2: Fetch weather forecast
        weather_url = "https://api.open-meteo.com/v1/forecast"

        weather_response = requests.get(
            weather_url,
            params={
                "latitude": latitude,
                "longitude": longitude,
                "current": "temperature_2m,precipitation,wind_speed_10m",
                "daily": (
                    "temperature_2m_max,"
                    "temperature_2m_min,"
                    "precipitation_sum,"
                    "precipitation_probability_max"
                ),
                "forecast_days": 2,
                "timezone": "Asia/Kolkata",
            },
            timeout=15,
        )
        weather_response.raise_for_status()

        data = weather_response.json()

        return {
            "city": location["name"],
            "state": location.get("admin1", ""),
            "current": data.get("current", {}),
            "daily_forecast": data.get("daily", {}),
        }

    except requests.RequestException as error:
        return {"error": f"Weather API request failed: {error}"}
    except (KeyError, ValueError, TypeError) as error:
        return {"error": f"Invalid weather data: {error}"}
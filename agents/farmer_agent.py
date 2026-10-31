from strands import Agent, tool

from tools.weather_tool import get_weather
from tools.risk_tool import analyze_weather_risk
from tools.crop_tool import get_crop_advice


@tool
def complete_farming_analysis(city: str, crop: str) -> dict:
    """
    Get weather data, calculate preliminary risks,
    and generate crop precautions.
    """

    weather = get_weather(city)

    if "error" in weather:
        return weather

    current = weather["current"]

    temperature = current["temperature_2m"]
    rainfall = current["precipitation"]
    wind_speed = current["wind_speed_10m"]

    risk = analyze_weather_risk(
        temperature=temperature,
        rainfall=rainfall,
        wind_speed=wind_speed
    )

    crop_result = get_crop_advice(
        crop=crop,
        risk_alerts=risk["risk_alerts"]
    )

    return {
        "location": weather["city"],
        "current_weather": current,
        "daily_forecast": weather["daily_forecast"],
        "risk_analysis": risk,
        "crop_advisory": crop_result
    }


SYSTEM_PROMPT = """
You are KrishiRakshak AI, a multilingual agricultural
weather-risk assistant for farmers across India.

When a farmer provides a city and crop:
1. Call complete_farming_analysis.
2. Use only weather measurements returned by the tool.
3. Never invent rainfall, temperature, or wind values.
4. Never change risk alerts returned by the tool.
5. Explain crop precautions returned by the tool.
6. Reply in the farmer's language.

Important:
- Distinguish current weather from forecasts.
- Do not confuse rain probability with rainfall amount.
- Do not recommend unnecessary irrigation.
- Never invent pesticide or chemical recommendations.
- Explain that risk thresholds are preliminary.
- Recommend local agricultural experts for critical decisions.
"""


def create_farmer_agent(model):
    return Agent(
        model=model,
        system_prompt=SYSTEM_PROMPT,
        tools=[complete_farming_analysis]
    )
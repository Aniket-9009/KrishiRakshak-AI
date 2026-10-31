from tools.risk_tool import analyze_weather_risk

result = analyze_weather_risk(
    temperature=42,
    rainfall=60,
    wind_speed=55
)

print(result)
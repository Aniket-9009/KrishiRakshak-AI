from tools.weather_tool import get_weather
import json

weather = get_weather("Pune")

print("\n===== ORIGINAL WEATHER API DATA =====")

print(json.dumps(weather, indent=4, ensure_ascii=False))
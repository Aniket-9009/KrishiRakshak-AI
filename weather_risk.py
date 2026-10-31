from tools.weather_tool import get_weather
from tools.risk_tool import analyze_weather_risk


print("================================")
print("     KrishiRakshak AI 🌾")
print("================================")

city = input("Enter Indian City: ").strip()

if not city:
    print("Please enter a city name.")
    raise SystemExit(1)

# Step 1: Get Weather Data
weather = get_weather(city)

if "error" in weather:
    print("Error:", weather["error"])
    raise SystemExit(1)

# Step 2: Extract Current Weather
current = weather["current"]

temperature = current["temperature_2m"]
rainfall = current["precipitation"]
wind_speed = current["wind_speed_10m"]

print("\n📍 Location:", weather["city"])
print("🌡️ Temperature:", temperature, "°C")
print("🌧️ Current Precipitation:", rainfall, "mm")
print("💨 Wind Speed:", wind_speed, "km/h")

# Step 3: Analyze Weather Risk
risk = analyze_weather_risk(
    temperature=temperature,
    rainfall=rainfall,
    wind_speed=wind_speed
)

# Step 4: Display Risk Alerts
print("\n⚠️ Weather Risk Analysis:")

for alert in risk["risk_alerts"]:
    print("-", alert)

print("\n🌾 Analysis Completed!")
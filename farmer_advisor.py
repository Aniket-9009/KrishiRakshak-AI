from tools.weather_tool import get_weather
from tools.risk_tool import analyze_weather_risk
from tools.crop_tool import get_crop_advice

print("\n🌾 Welcome to KrishiRakshak AI 🌾")

city = input("Enter your City: ").strip()
crop = input("Enter your Crop (tomato/onion/wheat/rice/cotton): ").strip()

if not city or not crop:
    print("Please enter both city and crop.")
    raise SystemExit(1)

# STEP 1: Get Live Weather
print("\n🌦️ Fetching Live Weather...")

weather = get_weather(city)

if "error" in weather:
    print("Error:", weather["error"])
    raise SystemExit(1)

current = weather["current"]

temperature = current["temperature_2m"]
rainfall = current["precipitation"]
wind_speed = current["wind_speed_10m"]

# STEP 2: Analyze Weather Risk
risk = analyze_weather_risk(
    temperature=temperature,
    rainfall=rainfall,
    wind_speed=wind_speed
)

# STEP 3: Generate Crop Advisory
advisory = get_crop_advice(
    crop=crop,
    risk_alerts=risk["risk_alerts"]
)

# STEP 4: Display Results
print("\n========== KRISHIRAKSHAK AI ==========")

print("\n📍 City:", weather["city"])
print("🌱 Crop:", advisory["crop"])

print("\n🌦️ Current Weather:")
print("🌡️ Temperature:", temperature, "°C")
print("🌧️ Rainfall:", rainfall, "mm")
print("💨 Wind Speed:", wind_speed, "km/h")

print("\n⚠️ Weather Risks:")
for alert in risk["risk_alerts"]:
    print("-", alert)

print("\n🌱 Crop Protection Advice:")
for advice in advisory["advice"]:
    print("-", advice)

print("\n======================================")
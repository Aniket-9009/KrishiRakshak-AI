import requests

url = "https://api.open-meteo.com/v1/forecast"

params = {
    "latitude": 18.52,
    "longitude": 73.85,
    "current": "temperature_2m,precipitation",
    "timezone": "Asia/Kolkata",
}

response = requests.get(url, params=params, timeout=15)
response.raise_for_status()

data = response.json()

print("🌾 KrishiRakshak AI")
print("------------------------")
print("City: Pune")
print("Temperature:", data["current"]["temperature_2m"], "°C")
print("Rainfall:", data["current"]["precipitation"], "mm")
from agents.farmer_agent import (
    weather_checker,
    risk_checker,
    crop_advisor
)

print("🌾 KrishiRakshak AI — Strands Tools")

for tool in [
    weather_checker,
    risk_checker,
    crop_advisor
]:
    print("Registered:", tool.tool_name)

print("All three Strands tools loaded successfully!")
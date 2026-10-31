from tools.crop_tool import get_crop_advice

result = get_crop_advice(
    crop="tomato",
    risk_alerts=[
        "HEAVY RAIN RISK",
        "STRONG WIND RISK"
    ]
)

print("\n🌾 KrishiRakshak AI")
print("Crop:", result["crop"])

print("\n🌱 Crop Advisory:")

for advice in result["advice"]:
    print("-", advice)
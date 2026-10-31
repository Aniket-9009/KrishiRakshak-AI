CROP_ADVICE = {
    "Marathi": {
        "heavy_rain": {
            "tomato": "🍅 टोमॅटो पिकामध्ये पाणी साचू देऊ नका.",
            "onion": "🧅 कांदा पिकाच्या शेतातील पाण्याचा निचरा तपासा.",
            "wheat": "🌾 गहू पिकाच्या शेतात पाणी साचणार नाही याची काळजी घ्या.",
            "rice": "🌾 भातशेतीतील पाण्याची पातळी आणि निचरा तपासा.",
            "cotton": "🌿 कापूस पिकामध्ये पाणी साचू देऊ नका.",
        },
        "heat": "🌡️ उष्णतेमुळे पिकांची स्थिती आणि जमिनीतील ओलावा तपासा.",
        "wind": "💨 जोरदार वाऱ्यामुळे पिकांचे नुकसान झाले आहे का ते तपासा.",
        "moderate_rain": "🌧️ पावसाचा अंदाज लक्षात घेऊन सिंचनापूर्वी जमिनीतील ओलावा तपासा.",
        "low": "✅ तपासलेल्या हवामान निकषांनुसार विशेष धोका आढळलेला नाही.",
        "disclaimer": "⚠️ महत्त्वाच्या शेतीविषयक निर्णयांसाठी स्थानिक कृषी तज्ज्ञांचा सल्ला घ्या.",
    },

    "Hindi": {
        "heavy_rain": {
            "tomato": "🍅 टमाटर की फसल में पानी जमा न होने दें।",
            "onion": "🧅 प्याज के खेत में जल निकासी जांचें।",
            "wheat": "🌾 गेहूं के खेत में जलभराव रोकें।",
            "rice": "🌾 धान के खेत में पानी का स्तर और निकासी जांचें।",
            "cotton": "🌿 कपास के खेत में जलभराव रोकें।",
        },
        "heat": "🌡️ गर्मी के कारण फसल की स्थिति और मिट्टी की नमी जांचें।",
        "wind": "💨 तेज हवा से फसल को नुकसान हुआ है या नहीं, जांचें।",
        "moderate_rain": "🌧️ बारिश के अनुमान को देखते हुए सिंचाई से पहले मिट्टी की नमी जांचें।",
        "low": "✅ जांचे गए मौसम मानदंडों के अनुसार कोई विशेष जोखिम नहीं मिला।",
        "disclaimer": "⚠️ महत्वपूर्ण खेती संबंधी निर्णयों के लिए स्थानीय कृषि विशेषज्ञ से सलाह लें।",
    },

    "English": {
        "heavy_rain": {
            "tomato": "🍅 Prevent waterlogging around tomato plants.",
            "onion": "🧅 Check drainage in onion fields.",
            "wheat": "🌾 Prevent waterlogging in wheat fields.",
            "rice": "🌾 Monitor water levels and drainage in rice fields.",
            "cotton": "🌿 Prevent waterlogging in cotton fields.",
        },
        "heat": "🌡️ Monitor crop condition and soil moisture during high temperatures.",
        "wind": "💨 Inspect crops for possible wind damage.",
        "moderate_rain": "🌧️ Check soil moisture before irrigation when rain is forecast.",
        "low": "✅ No elevated risk detected under the checked weather thresholds.",
        "disclaimer": "⚠️ Consult local agricultural experts before important farming decisions.",
    },
}


def get_multilingual_crop_advice(crop, risk_alerts, language):
    texts = CROP_ADVICE.get(language, CROP_ADVICE["English"])
    crop = crop.lower()

    advice = []

    if "HEAVY RAIN RISK" in risk_alerts:
        advice.append(
            texts["heavy_rain"].get(
                crop,
                texts["moderate_rain"]
            )
        )

    if "MODERATE RAIN RISK" in risk_alerts:
        advice.append(texts["moderate_rain"])

    if any("HEAT RISK" in alert for alert in risk_alerts):
        advice.append(texts["heat"])

    if any("WIND RISK" in alert for alert in risk_alerts):
        advice.append(texts["wind"])

    if not advice:
        advice.append(texts["low"])

    advice.append(texts["disclaimer"])

    return advice
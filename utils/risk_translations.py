RISK_TRANSLATIONS = {
    "Marathi": {
        "HIGH HEAT RISK": "🔴 तीव्र उष्णतेचा धोका",
        "MODERATE HEAT RISK": "🟡 मध्यम उष्णतेचा धोका",
        "HEAVY RAIN RISK": "🔴 अतिवृष्टीचा संभाव्य धोका",
        "MODERATE RAIN RISK": "🟡 मध्यम पावसाचा धोका",
        "STRONG WIND RISK": "🔴 जोरदार वाऱ्याचा धोका",
        "MODERATE WIND RISK": "🟡 मध्यम वाऱ्याचा धोका",
        "LOW WEATHER RISK": "🟢 तपासलेल्या निकषांनुसार कमी धोका",
        "NO ELEVATED RISK UNDER CHECKED THRESHOLDS":
            "🟢 तपासलेल्या निकषांनुसार विशेष धोका नाही",
    },
    "Hindi": {
        "HIGH HEAT RISK": "🔴 अत्यधिक गर्मी का जोखिम",
        "MODERATE HEAT RISK": "🟡 मध्यम गर्मी का जोखिम",
        "HEAVY RAIN RISK": "🔴 भारी बारिश का संभावित जोखिम",
        "MODERATE RAIN RISK": "🟡 मध्यम बारिश का जोखिम",
        "STRONG WIND RISK": "🔴 तेज हवा का जोखिम",
        "MODERATE WIND RISK": "🟡 मध्यम हवा का जोखिम",
        "LOW WEATHER RISK": "🟢 जांचे गए मानदंडों के अनुसार कम जोखिम",
        "NO ELEVATED RISK UNDER CHECKED THRESHOLDS":
            "🟢 जांचे गए मानदंडों के अनुसार विशेष जोखिम नहीं",
    },
    "English": {
        "HIGH HEAT RISK": "🔴 High Heat Risk",
        "MODERATE HEAT RISK": "🟡 Moderate Heat Risk",
        "HEAVY RAIN RISK": "🔴 Heavy Rain Risk",
        "MODERATE RAIN RISK": "🟡 Moderate Rain Risk",
        "STRONG WIND RISK": "🔴 Strong Wind Risk",
        "MODERATE WIND RISK": "🟡 Moderate Wind Risk",
        "LOW WEATHER RISK": "🟢 Low Risk Under Checked Thresholds",
        "NO ELEVATED RISK UNDER CHECKED THRESHOLDS":
            "🟢 No Elevated Risk Under Checked Thresholds",
    },
}


def translate_risk(alert, language):
    return RISK_TRANSLATIONS.get(
        language, RISK_TRANSLATIONS["English"]
    ).get(alert, alert)
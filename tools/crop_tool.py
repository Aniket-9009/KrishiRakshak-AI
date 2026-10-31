def get_crop_advice(crop: str, risk_alerts: list) -> dict:
    """
    Generate basic crop-specific weather precautions.
    """

    crop = crop.strip().lower()

    crop_names = {
        "tomato": "टोमॅटो",
        "onion": "कांदा",
        "wheat": "गहू",
        "rice": "भात",
        "cotton": "कापूस",
    }

    crop_name = crop_names.get(crop, crop)

    advice = []

    for risk in risk_alerts:

        if "RAIN" in risk:
            advice.append(
                "शेतात पाणी साचणार नाही याची काळजी घ्या."
            )

            if crop == "tomato":
                advice.append(
                    "टोमॅटोच्या शेतात पाण्याचा योग्य निचरा ठेवा."
                )

            elif crop == "onion":
                advice.append(
                    "कांद्याच्या शेतात जास्त ओलावा साचू देऊ नका."
                )

        elif "HEAT" in risk:
            advice.append(
                "जमिनीतील ओलावा तपासा आणि गरजेनुसार सिंचन करा."
            )

        elif "WIND" in risk:
            advice.append(
                "कमकुवत झाडांना आवश्यक आधार द्या."
            )

    if not advice:
        advice.append(
            "सध्या तपासलेल्या हवामान निकषांनुसार विशेष धोका आढळलेला नाही."
        )

    advice.append(
        "ही प्राथमिक माहिती आहे. महत्त्वाच्या शेतीविषयक निर्णयांसाठी स्थानिक कृषी तज्ज्ञांचा सल्ला घ्या."
    )

    return {
        "crop": crop_name,
        "risk_alerts": risk_alerts,
        "advice": advice
    }
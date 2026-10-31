def analyze_forecast_risk(forecast):
    """
    Analyze daily forecast for preliminary
    heat and rainfall risks.
    """

    alerts = []

    dates = forecast.get("time", [])
    max_temps = forecast.get("temperature_2m_max", [])
    rainfalls = forecast.get("precipitation_sum", [])

    for date, temperature, rainfall in zip(
        dates, max_temps, rainfalls
    ):
        daily_alerts = []

        if temperature >= 40:
            daily_alerts.append("HIGH HEAT RISK")
        elif temperature >= 35:
            daily_alerts.append("MODERATE HEAT RISK")

        if rainfall >= 50:
            daily_alerts.append("HEAVY RAIN RISK")
        elif rainfall >= 20:
            daily_alerts.append("MODERATE RAIN RISK")

        if not daily_alerts:
            daily_alerts.append(
                "NO ELEVATED RISK UNDER CHECKED THRESHOLDS"
            )

        alerts.append({
            "date": date,
            "temperature_max": temperature,
            "expected_rainfall": rainfall,
            "risk_alerts": daily_alerts
        })

    return alerts
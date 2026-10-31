from strands import tool


@tool
def analyze_weather_risk(
    temperature: float,
    rainfall: float,
    wind_speed: float
) -> dict:
    """
    Analyze basic weather risks for farmers.

    Args:
        temperature: Temperature in Celsius.
        rainfall: Rainfall in millimeters.
        wind_speed: Wind speed in km/h.
    """

    alerts = []

    # Temperature Risk
    if temperature >= 40:
        alerts.append("HIGH HEAT RISK")
    elif temperature >= 35:
        alerts.append("MODERATE HEAT RISK")

    # Rainfall Risk
    if rainfall >= 50:
        alerts.append("HEAVY RAIN RISK")
    elif rainfall >= 20:
        alerts.append("MODERATE RAIN RISK")

    # Wind Risk
    if wind_speed >= 50:
        alerts.append("STRONG WIND RISK")
    elif wind_speed >= 30:
        alerts.append("MODERATE WIND RISK")

    if not alerts:
        alerts.append("LOW WEATHER RISK")

    return {
        "temperature": temperature,
        "rainfall": rainfall,
        "wind_speed": wind_speed,
        "risk_alerts": alerts
    }
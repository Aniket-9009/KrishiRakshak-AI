"""KrishiRakshak AI — multilingual farmer weather dashboard.

Requires the existing tools/, utils/ and agents/ modules in the project.
"""
import html
from datetime import datetime

import streamlit as st

from agents.farmer_agent import create_farmer_agent
from strands.models.ollama import OllamaModel
from tools.weather_tool import get_weather
from tools.risk_tool import analyze_weather_risk
from tools.forecast_risk_tool import analyze_forecast_risk
from utils.translations import get_text
from utils.risk_translations import translate_risk
from utils.crop_translations import get_multilingual_crop_advice

st.set_page_config(page_title="KrishiRakshak AI | Farmer Dashboard", page_icon="🌾", layout="wide", initial_sidebar_state="expanded")

st.markdown("""
<style>
:root {color-scheme: light;}
.stApp {background: linear-gradient(155deg,#f1f8f1 0%,#fbfdf9 55%,#f0f6fc 100%);}
.block-container {max-width: 1230px; padding-top: 1.5rem; padding-bottom: 2.8rem;}
h1,h2,h3 {color:#173e30; letter-spacing:-.025em;}
.hero {background:linear-gradient(110deg,#145b43,#237956 65%,#32916b);color:white;
 padding:30px 34px;border-radius:22px;margin-bottom:24px;box-shadow:0 10px 30px #174e3824;}
.hero h1 {color:white;font-size:clamp(1.7rem,4vw,2.7rem);margin:0 0 9px;}
.hero p {color:#e4f5e9;margin:5px 0;font-size:1.04rem;}
.hero .badge {display:inline-block;background:#ffffff25;border:1px solid #ffffff55;border-radius:20px;
 padding:5px 12px;margin-bottom:12px;font-size:.83rem;letter-spacing:.04em;}
.section-label {font-size:1.22rem;font-weight:750;color:#194e3c;margin:26px 0 14px;}
.section-note {color:#577269;font-size:.91rem;margin-top:-8px;margin-bottom:12px;}
[data-testid="stMetric"] {background:#fff;border:1px solid #e2ece5;border-radius:16px;
 padding:16px 17px;box-shadow:0 4px 18px #1a51360c;}
[data-testid="stMetricLabel"] {color:#4c6a5e;}
[data-testid="stMetricValue"] {color:#174e3b;}
[data-testid="stVerticalBlockBorderWrapper"] {border-radius:17px;}
div.stButton>button[kind="primary"] {background:#18764f;border:0;border-radius:11px;font-weight:700;
 padding:.65rem 1.5rem;min-height:46px;}
div.stButton>button[kind="primary"]:hover {background:#0c5c3b;}
[data-testid="stSidebar"] {background:#eaf4eb;}
.small-note {color:#5d7468;font-size:.86rem;}
.footer {text-align:center;color:#597269;font-size:.85rem;padding:16px 0;}
@media(max-width:640px){.hero{padding:22px 18px;border-radius:16px}.block-container{padding:1rem .75rem 2rem}}
</style>
""", unsafe_allow_html=True)

# Visual refresh: accessible contrast, modern cards and responsive sidebar.
st.markdown("""
<style>
/* App foundation */
.stApp {background:linear-gradient(135deg,#f4faf5 0%,#f8fafc 55%,#edf7f1 100%);color:#19392d;}
.block-container {max-width:1300px;padding:2.2rem 2.5rem 3rem;}
[data-testid="stHeader"] {background:transparent;}
/* The previous theme made sidebar labels white on a pale background. */
section[data-testid="stSidebar"] {background:linear-gradient(180deg,#103d30 0%,#16543d 55%,#0d392c 100%) !important;border-right:1px solid #285c47;}
section[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p,
section[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] h3,
section[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] h4,
section[data-testid="stSidebar"] label,
section[data-testid="stSidebar"] [data-testid="stWidgetLabel"] p,
section[data-testid="stSidebar"] [data-testid="stCaptionContainer"] p {color:#f1fbf5 !important;opacity:1 !important;}
section[data-testid="stSidebar"] [data-testid="stCaptionContainer"] p {color:#b7d6c6 !important;line-height:1.6;}
section[data-testid="stSidebar"] [data-baseweb="input"] input,
section[data-testid="stSidebar"] [data-baseweb="select"] > div {background:#f7fcf9 !important;color:#173d2f !important;border-radius:12px !important;border:1px solid #d2e5d9 !important;}
section[data-testid="stSidebar"] [data-baseweb="select"] * {color:#173d2f;}
section[data-testid="stSidebar"] .stButton button {background:#f6c65d !important;color:#1b3b2e !important;border:0 !important;border-radius:12px !important;font-weight:800 !important;min-height:52px;box-shadow:0 7px 18px #051d142b;}
section[data-testid="stSidebar"] .stButton button:hover {background:#ffda86 !important;transform:translateY(-1px);}
section[data-testid="stSidebar"] hr {border-color:#ffffff35;}
/* Hero */
.hero {position:relative;overflow:hidden;background:linear-gradient(120deg,#0c4935 0%,#146c4b 54%,#24956b 100%);border-radius:26px;padding:45px 46px 42px;margin-bottom:28px;box-shadow:0 18px 40px #125a3c29;}
.hero:after {content:'✺';position:absolute;right:45px;top:-45px;font-size:270px;line-height:1;color:#ffffff12;pointer-events:none;}
.hero h1 {font-size:clamp(2.1rem,4vw,3.5rem);font-weight:850;letter-spacing:-.04em;line-height:1.2;position:relative;z-index:1;}
.hero p {font-size:1.07rem;line-height:1.65;max-width:760px;position:relative;z-index:1;}
.hero .badge {font-weight:750;font-size:.76rem;letter-spacing:.11em;padding:8px 15px;background:#ffffff1e;border:1px solid #ffffff50;}
.hero .hero-divider {height:1px;background:#ffffff35;margin:21px 0 16px;max-width:650px;}
.hero .hero-foot {display:flex;gap:12px;flex-wrap:wrap;font-size:.82rem;color:#dcf9e8;font-weight:600;}
.hero .hero-foot span {background:#ffffff19;padding:7px 12px;border-radius:20px;}
/* Sections and cards */
.section-label {font-size:1.42rem;color:#154b37;font-weight:850;letter-spacing:-.02em;margin:34px 0 13px;}
.section-note {color:#637c70;}
[data-testid="stMetric"] {background:#fff;border:1px solid #e0ebe4;border-radius:18px;padding:22px 20px;box-shadow:0 9px 25px #164e3010;min-height:123px;}
[data-testid="stMetricLabel"] p {font-weight:650;color:#5a7365 !important;}
[data-testid="stMetricValue"] {font-weight:850;color:#154f39 !important;}
[data-testid="stVerticalBlockBorderWrapper"] {border-radius:20px !important;background:#ffffffb8;border-color:#e0ebe4 !important;box-shadow:0 5px 18px #164e3009;}
[data-testid="stAlert"] {border-radius:14px !important;}
[data-testid="stAlert"] p {line-height:1.6;}
[data-testid="stExpander"] {border-radius:14px;}
.footer {border-top:1px solid #d9e9dd;margin-top:25px;padding-top:22px;line-height:1.7;}
.welcome {background:#fff;border:1px solid #dbeadf;border-left:5px solid #1c9365;border-radius:16px;padding:24px 28px;box-shadow:0 7px 22px #164e300c;margin:14px 0 20px;}
.welcome h3 {color:#145039;margin:0 0 8px;font-size:1.2rem;}
.welcome p {color:#587568;margin:0;line-height:1.65;}
@media(max-width:900px){.block-container{padding:1.4rem 1rem 2rem}.hero{padding:30px 25px;border-radius:19px}.hero:after{font-size:150px;right:5px;top:5px}}
@media(max-width:640px){.hero{padding:25px 20px}.hero h1{font-size:2rem}.section-label{font-size:1.2rem}[data-testid="stMetric"]{padding:13px;min-height:95px}.hero .hero-foot{gap:6px}}
</style>
""", unsafe_allow_html=True)

EXTRA = {
    "Marathi": {
        "sidebar": "शेतकरी नियंत्रण पॅनेल", "location": "ठिकाण", "crop_name": "पीक", "today": "सध्याचे निरीक्षण",
        "expected_rain": "🌧️ अपेक्षित पाऊस", "forecast_note": "दैनिक अंदाज; प्रत्यक्ष पाऊस वेगळा असू शकतो.",
        "risk_note": "हे अधिकृत हवामान इशारे नाहीत; साध्या नियमांवर आधारित अंदाज आहे.",
        "enter_city": "कृपया शहराचे नाव लिहा.", "fetch": "हवामानाची माहिती मिळवत आहे...",
        "received": "हवामान माहिती मिळाली", "unknown_error": "हवामान सेवा सध्या उपलब्ध नाही.",
        "upcoming": "पुढील दिवसांसाठी खबरदारी", "no_forecast": "पुढील दिवसांचा अंदाज उपलब्ध नाही.",
        "assistant_note": "मराठीमध्ये खालील माहिती नियमांवर आधारित आहे; AI ने तयार केलेली नाही.",
        "assistant_intro": "हवामान आणि पिकाच्या सूचनांचा आढावा घ्या. हवामान बदलल्यास पुन्हा तपासा.",
        "ai_loading": "AI सहाय्यक उत्तर तयार करत आहे...", "ai_error": "AI सहाय्यक उपलब्ध नाही",
        "disclaimer": "ही प्राथमिक माहिती आहे. महत्त्वाच्या शेतीविषयक निर्णयांसाठी स्थानिक कृषी तज्ज्ञांचा सल्ला घ्या.",
        "threshold": "तपासलेल्या निकषांनुसार विशेष धोका नाही.", "forecast_for": "दिवसाचा अंदाज",
        "run_english": "AI सहाय्यक फक्त English पर्यायात चालतो.",
    },
    "Hindi": {
        "sidebar": "किसान नियंत्रण पैनल", "location": "स्थान", "crop_name": "फसल", "today": "वर्तमान अवलोकन",
        "expected_rain": "🌧️ अनुमानित वर्षा", "forecast_note": "दैनिक पूर्वानुमान; वास्तविक बारिश अलग हो सकती है।",
        "risk_note": "ये आधिकारिक मौसम चेतावनियां नहीं हैं; सरल नियमों पर आधारित हैं।",
        "enter_city": "कृपया शहर का नाम दर्ज करें।", "fetch": "मौसम की जानकारी प्राप्त की जा रही है...",
        "received": "मौसम की जानकारी मिली", "unknown_error": "मौसम सेवा अभी उपलब्ध नहीं है।",
        "upcoming": "आने वाले दिनों की सावधानियां", "no_forecast": "आने वाले दिनों का पूर्वानुमान उपलब्ध नहीं है।",
        "assistant_note": "हिंदी में नीचे दी गई जानकारी नियमों पर आधारित है; AI द्वारा तैयार नहीं की गई है।",
        "assistant_intro": "मौसम और फसल सलाह देखें। मौसम बदलने पर दोबारा जांच करें।",
        "ai_loading": "AI सहायक उत्तर तैयार कर रहा है...", "ai_error": "AI सहायक उपलब्ध नहीं है",
        "disclaimer": "यह प्रारंभिक जानकारी है। महत्वपूर्ण खेती के निर्णयों के लिए स्थानीय कृषि विशेषज्ञ से सलाह लें।",
        "threshold": "जांचे गए मानदंडों के अनुसार कोई विशेष जोखिम नहीं।", "forecast_for": "दिन का पूर्वानुमान",
        "run_english": "AI सहायक केवल English विकल्प में चलता है।",
    },
    "English": {
        "sidebar": "Farmer controls", "location": "Location", "crop_name": "Crop", "today": "Current observation",
        "expected_rain": "🌧️ Expected Rainfall", "forecast_note": "Daily forecast; actual rainfall may differ.",
        "risk_note": "These are simple rule-based indicators, not official weather warnings.",
        "enter_city": "Please enter a city name.", "fetch": "Fetching weather information...",
        "received": "Weather information retrieved for", "unknown_error": "Weather service is temporarily unavailable.",
        "upcoming": "Precautions for upcoming days", "no_forecast": "Forecast is unavailable.",
        "assistant_note": "AI output may be inaccurate. Use the verified weather and rule-based alerts above.",
        "assistant_intro": "Review the weather and crop precautions. Check again when conditions change.",
        "ai_loading": "AI assistant is preparing a response...", "ai_error": "AI assistant unavailable",
        "disclaimer": "Preliminary information only. Consult local agricultural experts for important decisions.",
        "threshold": "No elevated risk under checked thresholds.", "forecast_for": "Forecast for",
        "run_english": "AI assistant runs in English mode only.",
    },
}


def tr(key):
    return get_text(language, key)


def extra(key):
    return EXTRA[language][key]


def heading(text, note=None):
    st.markdown(f'<div class="section-label">{html.escape(str(text))}</div>', unsafe_allow_html=True)
    if note:
        st.caption(note)


def show_alert(alert, *, forecast=False):
    message = translate_risk(alert, language)
    if any(token in alert for token in ("HIGH", "HEAVY", "STRONG")):
        st.error(message)
    elif "MODERATE" in alert:
        st.warning(message)
    elif forecast:
        st.success(message)
    else:
        st.info(message)


@st.cache_resource
def load_agent():
    model = OllamaModel(host="http://localhost:11434", model_id="qwen2.5:1.5b")
    return create_farmer_agent(model)


with st.sidebar:
    st.markdown("### 🌾 KrishiRakshak AI")
    language = st.selectbox("🌐 Language / भाषा", ["Marathi", "Hindi", "English"], index=0)
    st.markdown(f"#### {extra('sidebar')}")
    city = st.text_input(tr("city"), value="Pune", placeholder="Pune")
    crop = st.selectbox(tr("crop"), ["Tomato", "Onion", "Wheat", "Rice", "Cotton"])
    analyze = st.button(tr("analyze"), type="primary", use_container_width=True)
    st.divider()
    st.caption(extra("risk_note"))

st.markdown(
    f'<div class="hero"><div class="badge">🌿 SMART FARMING • WEATHER INTELLIGENCE</div>'
    f'<h1>{html.escape(tr("title"))}</h1>'
    f'<p><strong>{html.escape(tr("subtitle"))}</strong></p>'
    f'<p>{html.escape(tr("description"))}</p>'
    f'<div class="hero-divider"></div>'
    f'<div class="hero-foot"><span>☀️ Live Weather</span><span>🌱 Crop Intelligence</span>'
    f'<span>🛡️ Risk Awareness</span></div></div>',
    unsafe_allow_html=True,
)

if analyze:
    if not city.strip():
        st.warning(extra("enter_city"))
    else:
        try:
            with st.spinner(extra("fetch")):
                result = get_weather(city.strip())
            if not isinstance(result, dict):
                raise ValueError("Invalid weather response")
            if result.get("error"):
                st.error(str(result["error"]))
                st.session_state.pop("weather_result", None)
            else:
                st.session_state["weather_result"] = result
                st.session_state["selected_city"] = city.strip()
        except Exception as exc:
            st.session_state.pop("weather_result", None)
            st.error(f"{extra('unknown_error')} ({exc})")

weather = st.session_state.get("weather_result")
if weather:
    try:
        current = weather["current"]
        forecast = weather.get("daily_forecast", {})
        risk = analyze_weather_risk(
            temperature=current["temperature_2m"],
            rainfall=current["precipitation"],
            wind_speed=current["wind_speed_10m"],
        )
        forecast_alerts = analyze_forecast_risk(forecast) if forecast.get("time") else []
        st.success(f"📍 {extra('received')}: {weather.get('city', city)}")

        heading(tr("current_weather"), extra("today"))
        a, b, c = st.columns(3)
        a.metric(tr("temperature"), f"{current['temperature_2m']} °C")
        b.metric(tr("rainfall"), f"{current['precipitation']} mm")
        c.metric(tr("wind"), f"{current['wind_speed_10m']} km/h")

        heading(tr("current_risk"), extra("risk_note"))
        for alert in risk.get("risk_alerts", []):
            show_alert(alert)

        heading(tr("forecast"), extra("forecast_note"))
        dates = forecast.get("time", [])
        if not dates:
            st.info(extra("no_forecast"))
        for i, date in enumerate(dates[:2]):
            with st.container(border=True):
                st.markdown(f"**📅 {date}**")
                x, y, z, w = st.columns(4)
                x.metric(tr("max_temp"), f"{forecast['temperature_2m_max'][i]} °C")
                y.metric(tr("min_temp"), f"{forecast['temperature_2m_min'][i]} °C")
                z.metric(extra("expected_rain"), f"{forecast['precipitation_sum'][i]} mm")
                w.metric(tr("rain_probability"), f"{forecast['precipitation_probability_max'][i]}%")

        heading(tr("forecast_risk"), extra("risk_note"))
        if not forecast_alerts:
            st.info(extra("no_forecast"))
        for day in forecast_alerts[:2]:
            st.markdown(f"**📅 {day['date']}**")
            for alert in day.get("risk_alerts", []):
                show_alert(alert, forecast=True)

        heading(tr("crop_advice"))
        current_advice = get_multilingual_crop_advice(crop, risk.get("risk_alerts", []), language)
        with st.container(border=True):
            for item in current_advice:
                st.write(item)

        heading(tr("upcoming_advice"))
        if not forecast_alerts:
            st.info(extra("no_forecast"))
        for day in forecast_alerts[:2]:
            st.markdown(f"**📅 {day['date']}**")
            day_risks = [a for a in day.get("risk_alerts", []) if a != "NO ELEVATED RISK UNDER CHECKED THRESHOLDS"]
            if day_risks:
                # Each risk is evaluated; combined heat + rainfall alerts are both shown.
                day_advice = get_multilingual_crop_advice(crop, day_risks, language)
                with st.container(border=True):
                    for item in day_advice:
                        st.write(item)
            else:
                st.success(extra("threshold"))

        heading(tr("assistant"))
        if language == "English":
            st.caption(extra("assistant_note"))
            if st.button("🤖 Generate AI explanation", key="run_agent", type="secondary"):
                try:
                    with st.spinner(extra("ai_loading")):
                        agent = load_agent()
                        response = agent(
                            f"I grow {crop} in {weather.get('city', city)}. "
                            "Use your weather analysis tool. Explain weather risks and safe crop precautions "
                            "briefly in English. Never invent measurements."
                        )
                    st.write(str(response))
                except Exception as exc:
                    st.error(f"{extra('ai_error')}: {exc}")
        else:
            st.info(extra("assistant_intro"))
            st.caption(extra("assistant_note"))
            st.caption(extra("run_english"))
    except (KeyError, IndexError, TypeError, ValueError) as exc:
        st.error(f"{extra('unknown_error')} ({exc})")
else:
    welcome = {
        "Marathi": ("🌿 तुमच्या शेतासाठी हवामान माहिती", "डावीकडे शहर, पीक आणि भाषा निवडा. ‘हवामान आणि पीक धोका तपासा’ बटणावर क्लिक केल्यावर हवामान, संभाव्य धोके आणि पीक संरक्षण सूचना दिसतील."),
        "Hindi": ("🌿 आपके खेत के लिए मौसम की जानकारी", "बाईं ओर शहर, फसल और भाषा चुनें। विश्लेषण बटन दबाकर मौसम, संभावित जोखिम और फसल सुरक्षा सुझाव देखें।"),
        "English": ("🌿 Weather insights for your farm", "Select your city, crop and language in the sidebar. Click Analyze to see live weather, potential risks and practical crop precautions."),
    }[language]
    st.markdown(f'<div class="welcome"><h3>{html.escape(welcome[0])}</h3><p>{html.escape(welcome[1])}</p></div>', unsafe_allow_html=True)

st.divider()
st.markdown(f'<div class="footer">🌾 KrishiRakshak AI &nbsp;•&nbsp; {html.escape(extra("disclaimer"))}</div>', unsafe_allow_html=True)

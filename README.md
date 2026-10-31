# 🌾 KrishiRakshak AI

### AI-Powered Weather Risk & Crop Advisory for Indian Farmers

KrishiRakshak AI is a multilingual farming assistance application
that helps farmers understand weather conditions, identify potential
weather risks, and receive basic crop precautions.

## Features

- Live weather information using Open-Meteo API
- Two-day weather forecast
- Rule-based weather risk analysis
- Crop-specific precautions
- Marathi, Hindi, and English interface
- AI agent integration using Strands Agents SDK
- Local Ollama model for English AI responses
- Interactive Streamlit dashboard

## Technology Stack

- Python
- Streamlit
- Strands Agents SDK
- Ollama (Qwen 2.5 1.5B)
- Open-Meteo API

## Supported Crops

Tomato, Onion, Wheat, Rice, Cotton

## Project Structure

- app.py — Streamlit dashboard
- agents/ — Strands AI agent
- tools/ — Weather, risk, and crop analysis tools
- utils/ — Multilingual translations
- requirements.txt — Python dependencies

## Run Locally

1. Clone the repository.
2. Create a Python virtual environment.
3. Install dependencies using `pip install -r requirements.txt`.
4. Start Ollama and ensure `qwen2.5:1.5b` is available.
5. Run `streamlit run app.py`.

## Limitations

- Weather risk alerts are based on prototype thresholds.
- This application does not issue official weather warnings.
- Marathi and Hindi responses are currently rule-based.
- The Strands AI agent is available in English mode.
- Agricultural advice is preliminary and should be verified
  with local agricultural experts.

## Deployment

AWS deployment is planned.

## Disclaimer

KrishiRakshak AI is an educational prototype.
It should not be used as the sole basis for agricultural decisions.
from strands.models.ollama import OllamaModel
from agents.farmer_agent import create_farmer_agent

# Connect to local Ollama model
model = OllamaModel(
    host="http://localhost:11434",
    model_id="qwen2.5:1.5b"
)

# Create Strands AI Agent with our 3 tools
agent = create_farmer_agent(model)

print("\n🌾 Welcome to KrishiRakshak AI 🌾")
print("Ask your farming question!")
print("Type 'exit' to quit.\n")

while True:
    question = input("\nFarmer: ").strip()

    if question.lower() == "exit":
        print("Thank you for using KrishiRakshak AI!")
        break

    if not question:
        continue

    try:
       agent(question)

    except Exception as e:
        print("\nError:", e)
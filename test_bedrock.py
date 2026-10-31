import boto3
from strands import Agent
from strands.models import BedrockModel

session = boto3.Session(
    profile_name="cloudrescue",
    region_name="ap-south-1"
)

model = BedrockModel(
    model_id="apac.amazon.nova-micro-v1:0",
    boto_session=session,
    temperature=0.3
)

agent = Agent(
    model=model,
    system_prompt="You are KrishiRakshak AI. Reply in Marathi."
)

response = agent("नमस्कार! तू शेतकऱ्यांना कशी मदत करशील?")

print("\n🌾 KrishiRakshak AI Response:")
print(response)
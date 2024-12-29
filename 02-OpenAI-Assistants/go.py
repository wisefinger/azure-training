import os
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from openai import AzureOpenAI
from dotenv import load_dotenv

print("Loading environment variables...")
# Load the environment variables from .env
load_dotenv()

# Fetch environment variables
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
API_KEY = os.getenv("API_KEY")
DEPLOYMENT_NAME = os.getenv("DEPLOYMENT_NAME")  # Ensure this is correct

if not AZURE_OPENAI_ENDPOINT:
    raise ValueError("AZURE_OPENAI_ENDPOINT environment variable is not set.")
if not API_KEY:
    raise ValueError("API_KEY environment variable is not set.")

# Initialize the token provider
try:
    token_provider = get_bearer_token_provider(
        DefaultAzureCredential(),
        "https://cognitiveservices.azure.com/.default"
    )
except Exception as e:
    raise RuntimeError(f"Failed to initialize token provider: {e}")

# Initialize AzureOpenAI client
try:
    client = AzureOpenAI(
        azure_ad_token_provider=token_provider,
        azure_endpoint=AZURE_OPENAI_ENDPOINT,
        api_version="2024-10-21",  # Ensure this matches your API version
    )
except Exception as e:
    raise RuntimeError(f"Failed to initialize AzureOpenAI client: {e}")

# List models to verify setup
try:
  available_models = client.models.list()
  #loop through the models and print the name and id
  for model in available_models:
    print(f"Model Name:  {model.id}")

except Exception as e:
    raise RuntimeError(f"Error fetching models: {e}")

# Create an assistant
try:
    assistant = client.beta.assistants.create(
        name="Math Assist",
        instructions="You are an AI assistant that can write code to help answer math questions.",
        tools=[{"type": "code_interpreter"}],
        model=DEPLOYMENT_NAME  # Ensure this matches your deployed model
    )
    print("Assistant created successfully.")
except Exception as e:
    raise RuntimeError(f"Failed to create assistant: {e}")
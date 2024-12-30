
from openai import AzureOpenAI
import os
from dotenv import load_dotenv

deployment_name="gpt-4o-mini"


# Load the environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY environment variable is not set or is empty")


# Initialize the AzureOpenAI client
client = AzureOpenAI(
    api_key=OPENAI_API_KEY,  
    api_version="2024-07-01-preview",
    azure_endpoint="https://kris-try-one.openai.azure.com/"
)


# Create a chat completion
chat_completion = client.chat.completions.create(
    model=deployment_name, # model = "deployment_name".
    messages= [
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "Write a haiku about programming."
        }
      ]
    }
  ]
)
# Print the completion
print(chat_completion.choices[0].message.content) 

print("starting.......................")




print("completed.......................")
import os  
import base64
from openai import AzureOpenAI
from dotenv import load_dotenv
import json

# 1. Load the environment variables from .env
load_dotenv()

# 2. Access the variables
end_point = os.getenv("end_point")
api_key = os.getenv("api_key")

deployment = os.getenv("DEPLOYMENT_NAME", "gpt-4o-mini")  


# Initialize Azure OpenAI client with key-based authentication    
client = AzureOpenAI(  
    azure_endpoint=end_point,  
    api_key=api_key,  
    api_version="2024-05-01-preview",  
)
    
# IMAGE_PATH = "YOUR_IMAGE_PATH"
# encoded_image = base64.b64encode(open(IMAGE_PATH, 'rb').read()).decode('ascii')

#Prepare the chat prompt 
chat_prompt = [
    {
        "role": "system",
        "content": [
            {
                "type": "text",
                "text": "You are an AI assistant that helps people find information."
            }
        ]
    },
    {
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": "what is the capital of France?"
            }
        ]
    },
   
   
     
] 
    
# Include speech result if speech is enabled  
messages = chat_prompt  
    
# Generate the completion  
completion = client.chat.completions.create(  
    model=deployment,  
    messages=messages,  
    max_tokens=800,  
    temperature=0.7,  
    top_p=0.95,  
    frequency_penalty=0,  
    presence_penalty=0,  
    stop=None,  
    stream=False
)






# Parse the JSON string
data = json.loads(completion.to_json())

# Extract the "content" field
content = data["choices"][0]["message"]["content"]
print(content)


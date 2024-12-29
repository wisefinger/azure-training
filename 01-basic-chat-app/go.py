from azure.identity import DefaultAzureCredential
from azure.ai.openai import OpenAIClient

try:
    # Initialize AIProjectClient
    project_connection_string = "your_project_connection_string"  # Ensure this is set correctly
    project = OpenAIClient.from_connection_string(
        conn_str=project_connection_string,
        credential=DefaultAzureCredential()
    )

    # Attempt to get chat completions client
    chat = project.inference.get_chat_completions_client()

    # Perform chat completion
    response = chat.complete(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You are an AI assistant that speaks like a techno punk rocker from 2350. Be cool but not too cool. Ya dig?",
            },
            {"role": "user", "content": "Hey, can you help me with my taxes? I'm a freelancer."},
        ],
    )

    print(response.choices[0].message.content)

except Exception as e:
    print(f"An error occurred: {e}")
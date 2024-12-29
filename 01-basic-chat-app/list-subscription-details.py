from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from azure.mgmt.resource.subscriptions import SubscriptionClient

from dotenv import load_dotenv
import os

print("starting script ----------------------------------------------------------------------------")
# 1. Load the environment variables from .env
load_dotenv()

# Initialize DefaultAzureCredential
credential = DefaultAzureCredential()

# Create a SubscriptionClient instance
subscription_client = SubscriptionClient(credential)

# Fetch and display details of all subscriptions
print("Your Azure Subscriptions:")
for subscription in subscription_client.subscriptions.list():
    print(f"Subscription ID: {subscription.subscription_id}")
    print(f"Subscription Name: {subscription.display_name}")
    print(f"State: {subscription.state}")
    print("-" * 40)




print("completing script --------------------------------------------------------------------------")
""" # create the project client
project = AIProjectClient.from_connection_string(
    conn_str=project_connection_string, credential=DefaultAzureCredential()
)

chat = project.inference.get_chat_completions_client()
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

print(response.choices[0].message.content) """
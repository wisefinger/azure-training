from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient
from dotenv import load_dotenv
import os

# Define the project connection string
project_connection_string = "eastus2.api.azureml.ms;10eccf89-3ce4-4c6d-b72c-3a559a4cc8b0;rg-kriscardoen-4514_ai;00-basic-chat-app"

print("Starting script ----------------------------------------------------------------------------")

# 1. Load the environment variables from .env
load_dotenv()

# Initialize DefaultAzureCredential
credential = DefaultAzureCredential()

# Replace this with your Azure subscription ID
AZURE_SUBSCRIPTION_ID = os.getenv("AZURE_SUBSCRIPTION_ID")  # Ensure you set this in your .env file

# Create a ResourceManagementClient instance
resource_client = ResourceManagementClient(credential, AZURE_SUBSCRIPTION_ID)

# Specify the resource group name
resource_group_name = "rg-kriscardoen-4514_ai"  # Replace with your resource group name

# Fetch and display all resources in the specified resource group
print(f"Resources in Resource Group '{resource_group_name}':")
for resource in resource_client.resources.list_by_resource_group(resource_group_name):
    print(f"Resource Name: {resource.name}")
    print(f"Resource Type: {resource.type}")
    print(f"Location: {resource.location}")
    print(f"ID: {resource.id}")
    print("-" * 40)



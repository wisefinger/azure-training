from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient
from dotenv import load_dotenv
import os


print("Starting script ----------------------------------------------------------------------------")


# Load the environment variables from .env
load_dotenv()

# Initialize DefaultAzureCredential
credential = DefaultAzureCredential()

# Replace this with your Azure subscription ID
AZURE_SUBSCRIPTION_ID = os.getenv("AZURE_SUBSCRIPTION_ID") 

# Obtain the management object for resources.
resource_client = ResourceManagementClient(credential, AZURE_SUBSCRIPTION_ID)

# Retrieve the list of resource groups
group_list = resource_client.resource_groups.list()

# Show the groups in formatted output
column_width = 40

print("Resource Group".ljust(column_width) + "Location")
print("-" * (column_width * 2))

for group in list(group_list):
    print(f"{group.name:<{column_width}}{group.location}")



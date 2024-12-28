




print("starting script.....................................")
from dotenv import load_dotenv
import os
from azure.storage.blob import BlobServiceClient

# 1. Load the environment variables from .env
load_dotenv()

# 2. Access the variables
azure_conn = os.getenv("azure_conn")
azure_key = os.getenv("azure_key")

blob_service_client = BlobServiceClient.from_connection_string(azure_conn)

# 3. create a new container
# container_name = "mycontainer"
# container_client = blob_service_client.create_container(container_name)

# upload a file
container_name = "mycontainer"
# upload the "image.png" file 
blob_client = blob_service_client.get_blob_client(container=container_name, blob="image.png")



















print("script completed....................................")
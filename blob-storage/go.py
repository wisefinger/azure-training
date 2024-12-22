




print("starting script.....................................")
from dotenv import load_dotenv
import os

# 1. Load the environment variables from .env
load_dotenv()

# 2. Access the variables
azure_conn = os.getenv("azure_conn")
azure_key = os.getenv("azure_key")






















print("script completed....................................")
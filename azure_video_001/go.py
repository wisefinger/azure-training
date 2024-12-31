import os
from dotenv import load_dotenv
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes

print("Starting...")

# Load environment variables
load_dotenv()
AZURE_ENDPOINT = os.getenv("AZURE_ENDPOINT")
if not AZURE_ENDPOINT:
    raise ValueError("AZURE_ENDPOINT environment variable is not set or is empty")
AZURE_API_KEY = os.getenv("AZURE_API_KEY")
if not AZURE_API_KEY:
    raise ValueError("AZURE_API_KEY environment variable is not set or is empty")

# Create a client
client = ComputerVisionClient(AZURE_ENDPOINT, CognitiveServicesCredentials(AZURE_API_KEY))

# Define image and analyze it
with open("frame_80.jpg", "rb") as f:
    visual_features = [VisualFeatureTypes.tags, VisualFeatureTypes.objects]
    analysis = client.analyze_image_in_stream(f, visual_features)

# Output results
print("Tags:", [tag.name for tag in analysis.tags])
print("Objects:", [obj.object_property for obj in analysis.objects])

print("Completed.")

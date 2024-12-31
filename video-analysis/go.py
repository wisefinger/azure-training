import cv2
import base64
import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY environment variable is not set or is empty")

# Initialize OpenAI client
client = OpenAI(api_key=OPENAI_API_KEY)

# Load the video file
video = cv2.VideoCapture("IMG_0302.MOV")
if not video.isOpened():
    raise ValueError("Error opening video file")

# Extract frames from the video
frames = []
while True:
    success, frame = video.read()
    if not success:
        break
    frames.append(frame)

video.release()
print(len(frames), "frames read.")

# Resize and encode every nth frame
base64Frames = []
step_size = 20  # Use every 20th frame
resize_dim = (256, 256)  # Smaller dimensions to reduce base64 size

for idx, frame in enumerate(frames):
    if idx % step_size == 0:
        resized_frame = cv2.resize(frame, resize_dim)
        _, buffer = cv2.imencode('.jpg', resized_frame)
        base64Frame = base64.b64encode(buffer).decode('utf-8')
        base64Frames.append(base64Frame)
        # save the frame to a file for debugging in the subdirectory "frames"
        cv2.imwrite(f"frames/frame_{idx}.jpg", resized_frame)

print(len(base64Frames), "base64-encoded frames created.")

# Reduce input to a single frame
if base64Frames:
    single_frame = base64Frames[4]  # Use only the first frame
else:
    raise ValueError("No frames available for encoding.")

# Send a single frame to OpenAI
PROMPT_MESSAGES = [
    {
        "role": "user",
        "content": "This is a frame from a video. list the type of objects you can identify in the image .",
        "image": single_frame
    }
]

params = {
    "model": "gpt-4o",
    "messages": PROMPT_MESSAGES,
    "max_tokens": 200,
}

try:
    result = client.chat.completions.create(**params)
    print(result.choices[0].message.content)
except Exception as e:
    print(f"Error communicating with OpenAI API: {e}")

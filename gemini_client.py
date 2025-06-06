import os
from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO
import base64
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

prompt = "alunos de uma pós graduação numa mesa programando no estilo cyberpunk"

# Configure the API key from environment variable
# genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

contents = "alunos de uma pós graduação numa mesa programando no estilo cyberpunk"

response = client.models.generate_content(
    model="gemini-2.0-flash-preview-image-generation",
    contents=contents,
    config=types.GenerateContentConfig(response_modalities=["TEXT", "IMAGE"]),
)

for part in response.candidates[0].content.parts:
    if part.text is not None:
        print(part.text)
    elif part.inline_data is not None:
        image = Image.open(BytesIO((part.inline_data.data)))
        image.save("gemini-native-image.png")
        image.show()

import os
import base64
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize the OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def generate_image_dall_e_3(prompt):
    try:
        # Generate image using DALL-E 3
        response = client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            size="1024x1024",
            quality="standard",
            n=1,
        )

        # Get the image URL
        image_url = response.data[0].url
        print(f"Image generated successfully! URL: {image_url}")
        return image_url

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None


if __name__ == "__main__":
    prompt = "alunos de uma pós graduação numa mesa programando no estilo cyberpunk"
    generate_image_dall_e_3(prompt)

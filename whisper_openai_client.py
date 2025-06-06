import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def transcribe_audio(audio_file_path):
    """
    Transcribe audio file using OpenAI's Whisper API
    """
    try:
        with open(audio_file_path, "rb") as audio_file:
            transcript = client.audio.transcriptions.create(
                model="whisper-1", file=audio_file
            )
        return transcript.text
    except Exception as e:
        print(f"Error during transcription: {e}")
        return None


if __name__ == "__main__":
    # Example usage
    audio_path = "./audio/posgenai.mp3"  # Replace with your audio file path
    transcription = transcribe_audio(audio_path)

    if transcription:
        print("Transcription:")
        print(transcription)

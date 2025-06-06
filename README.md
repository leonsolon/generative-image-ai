# AI Tutorial Scripts Collection

This repository contains a collection of Python scripts that demonstrate various AI capabilities for educational purposes, including video generation, image creation, and audio transcription.

## 🚀 Features

- **Video Generation**: Create videos using Google's Gemini Veo 2.0 model
- **Image Generation**: Generate images using both Google Gemini and OpenAI DALL-E 3
- **Audio Transcription**: Transcribe audio files using OpenAI's Whisper API

## 📋 Prerequisites

- Python 3.7+
- Google Gemini API key
- OpenAI API key

## 🛠️ Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd <repository-directory>
```

2. Install required dependencies:
```bash
pip install google-genai openai pillow python-dotenv
```

3. Create a `.env` file in the project root:
```env
GEMINI_API_KEY=your_gemini_api_key_here
OPENAI_API_KEY=your_openai_api_key_here
```

## 📁 Project Structure

```
├── gemini_video.py          # Video generation using Gemini Veo 2.0
├── gemini_client.py         # Image generation using Gemini
├── dall-e-3_client.py       # Image generation using DALL-E 3
├── whisper_openai_client.py # Audio transcription using Whisper
├── .env                     # Environment variables (create this)
└── README.md               # This file
```

## 🎯 Usage

### Video Generation (Gemini Veo 2.0)

Generate videos with custom prompts using Google's Veo 2.0 model:

```bash
python gemini_video.py
```

**Features:**
- Creates cyberpunk-style videos of graduate students programming
- Configurable aspect ratio (16:9 or 9:16)
- Person generation control
- Automatic video download and saving

### Image Generation (Gemini)

Generate images using Google's Gemini model:

```bash
python gemini_client.py
```

**Features:**
- Text and image generation capabilities
- Saves generated images as PNG files
- Automatic image display

### Image Generation (DALL-E 3)

Generate high-quality images using OpenAI's DALL-E 3:

```bash
python dall-e-3_client.py
```

**Features:**
- High-quality 1024x1024 image generation
- Returns image URLs
- Customizable prompts

### Audio Transcription (Whisper)

Transcribe audio files to text using OpenAI's Whisper:

```bash
python whisper_openai_client.py
```

**Features:**
- Supports various audio formats
- High-accuracy transcription
- Error handling and logging

**Note:** Make sure to place your audio file in the `./audio/` directory and update the file path in the script.

## 🔧 Configuration

### Environment Variables

The scripts require the following environment variables in your `.env` file:

- `GEMINI_API_KEY`: Your Google Gemini API key
- `OPENAI_API_KEY`: Your OpenAI API key

### API Keys Setup

1. **Google Gemini API Key:**
   - Visit [Google AI Studio](https://aistudio.google.com/)
   - Create a new project or select an existing one
   - Generate an API key

2. **OpenAI API Key:**
   - Visit [OpenAI Platform](https://platform.openai.com/)
   - Go to API Keys section
   - Create a new secret key

## 📝 Example Prompt

All scripts use the following example prompt (in Portuguese):
```
"alunos de uma pós graduação numa mesa programando no estilo cyberpunk"
```
Translation: "graduate students at a table programming in cyberpunk style"

Feel free to modify the prompts in each script to generate different content.

## 🚨 Important Notes

- **Rate Limits**: Be aware of API rate limits for both Google Gemini and OpenAI services
- **Costs**: These APIs may incur costs based on usage
- **Video Generation**: Video generation can take several minutes to complete
- **File Sizes**: Generated videos and images may be large files

## 🛡️ Error Handling

All scripts include basic error handling:
- Environment variable validation
- API request error catching
- File operation error handling

## 📄 License

This project is for educational purposes. Please ensure you comply with the terms of service for Google Gemini and OpenAI APIs.

## 🤝 Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

## 📞 Support

If you encounter any issues:
1. Check your API keys are correctly set in the `.env` file
2. Verify your internet connection
3. Check API service status
4. Review error messages for specific guidance 

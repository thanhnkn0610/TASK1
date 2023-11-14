from openai import OpenAI
from pathlib import Path
import os

#connect to openai
os.environ['OPENAI_API_KEY'] = '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'
client = OpenAI()

def text_to_speech( text = 'Hello', speech_file_path = Path(__file__).parent / "speech.mp3"):
    response = client.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=text
    )
    response.stream_to_file(speech_file_path)

text_to_speech()

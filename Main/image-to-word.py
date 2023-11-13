from openai import OpenAI
import json
import os

#var 
word = 'intelligent'

#connect to openai
os.environ['OPENAI_API_KEY'] = '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'
client = OpenAI()

#generate image
response = client.images.generate(
  model="dall-e-2",
  prompt="Smart Fridge with Intelligent Sensors",
  size="1024x1024",
  quality="standard",
  n=1,
)

image_url = response.data[0].url
print(image_url)


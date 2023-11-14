from openai import OpenAI
import os

os.environ['OPENAI_API_KEY'] = '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'
client = OpenAI()

response = client.images.generate(
  model="dall-e-2",
  prompt="intelligent",
  size="1024x1024",
  quality="standard",
  n=5,
)

image_url = response.data[0].url
print(image_url)
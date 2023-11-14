from openai import OpenAI
import json
import os

os.environ['OPENAI_API_KEY'] = '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'
client = OpenAI()
           
completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello!"}
  ]
)

# Serializing json
json_object = json.dumps(completion.choices[0].message.content, indent=4)
 
# Writing to sample.json
with open("sample.json", "w") as outfile:
    outfile.write(json_object)
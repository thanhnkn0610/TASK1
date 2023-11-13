from openai import OpenAI
import json
import os

#var
word = 'intelligent'
n = 5 #number questions
export_url = './TASK1/assets/multiple-choice/sample.json'

#connect to openai
os.environ['OPENAI_API_KEY'] = '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'
client = OpenAI()

#generate text
promt = 'Create '+ str(n) +' multiple-choice question for learning the new vocab word: '+ word + ' and give me answers for each question. Change it to json format.'
           
completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": promt}
  ]
)
json_object = completion.choices[0].message.content

#to json
with open(export_url, "w") as outfile:
    outfile.write(json_object)
from openai import OpenAI
import json
import os

#var
word = 'intelligent'
n = 5 #number questions
export_url = './TASK1/assets/multiple-choice/' + word +'.json'
promt = 'Create '+ str(n) +' multiple-choice question for learning the new vocab word: '+ word + ' and give me answers for each question. Change it to json format.'

#connect to openai
os.environ['OPENAI_API_KEY'] = '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'
client = OpenAI()

#generate text           
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
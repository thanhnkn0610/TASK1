from openai import OpenAI
import json
import os
import requests 
import time

#var 
word = 'intelligent'
nig = 2 #number img generate
export_url = './TASK1/assets/image-to-word/' + word + '/' + word
style = ['vivid', 'natural']

#connect to openai
os.environ['OPENAI_API_KEY'] = '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'
client = OpenAI()

def generate_image(i):

  response = client.images.generate(
    model="dall-e-3",
    prompt="intelligent",
    size="1024x1024",
    quality="standard",
    style=style[i],
    n=1,
  )
  data = requests.get(response.data[0].url).content

  export_url_last = export_url + str(i+1) +'.jpg'
  f = open(export_url_last,'wb')
  f.write(data) 
  f.close()

for i in range(nig):
  generate_image(i)
  time.sleep(60)














# #generate image
# response = client.images.generate(
#   model="dall-e-3",
#   prompt="intelligent",
#   size="1024x1024",
#   quality="standard",
#   n=1,
# )

# #download img
# for i in range(nig):
#   data = requests.get(response.data[i].url).content
#   export_url_last = export_url + str(i+1)
#   f = open(export_url_last,'wb')
#   f.write(data) 
#   f.close()




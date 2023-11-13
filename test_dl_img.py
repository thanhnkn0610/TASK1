import requests 
from PIL import Image 

url = 'https://oaidalleapiprodscus.blob.core.windows.net/private/org-bsB7cni2KADDSeEJNMQijEzz/user-IlWYvlCgQfQbU9MGrA1dpTpC/img-wNi7axBt7rtIMRcdeFBP9SFx.png?st=2023-11-13T09%3A58%3A11Z&se=2023-11-13T11%3A58%3A11Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2023-11-12T12%3A40%3A07Z&ske=2023-11-13T12%3A40%3A07Z&sks=b&skv=2021-08-06&sig=QFZ5Cj47qh9fNESlWvYxGVgqXSEcIwCupUj4r%2B0bCSA%3D'
data = requests.get(url).content 
f = open('img.jpg','wb') 
f.write(data) 
f.close()
img = Image.open('img.jpg') 
img.show()
import requests
import json

url = 'https://run.mocky.io/v3/83580f87-541f-468a-854c-1b2d8f78a56f'
response = requests.get(url)
data = response.json()

print (data['registration id'])

#respone = requests.get(url)
#data - response.json()
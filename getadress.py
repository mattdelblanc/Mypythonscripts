import json
import requests
import pprint

url = 'https://run.mocky.io/v3/bd2fa3b8-74f4-4781-bfc1-2ff23151dd27'

response = requests.get(url)
data = response.json()

#print(data['address'])

for item in data ['address']:
    if item ['pincode'] == 400002:
        print(item['identifier'])
        print(item['street_name'])
        print(item['address_1'])
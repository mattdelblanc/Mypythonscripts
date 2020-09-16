import json
import requests

url = 'https://run.mocky.io/v3/26573fbb-b04e-4215-9f25-57d8a21ccc00'
response = requests.get(url)
data = response.json()

print(data["player_name"])
print(data["position"])
print(data["jersey no"])

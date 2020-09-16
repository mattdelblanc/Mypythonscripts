import requests
import json


url = 'https://run.mocky.io/v3/80b00197-2ad7-41a5-8b61-48f79b8bc28a'

response = requests.get(url)
data = response.json()

print(data)

for player_type, player_name in data.items():
    print(player_type)
    for players in player_name:
        print(players)

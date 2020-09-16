import requests
import pdb
import datetime
url = "https://provider.kareo.com/patient-engagement-ui/api/AppointmentSchedule/AvailableTimeBlocks"

querystring = {"providerShortName":"melissa-chinn","serviceLocationGuid":"85cb0e01-3bf9-89b6-e053-c9371e0a572a","startRange":"2020-02-15T00:00:00-08:00","endRange":"2020-02-29T23:59:59-08:00","isRegularHours":"true"}

headers = {
    'Connection': "keep-alive",
    'Accept': "application/json, text/plain, */*",
    'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",
    'Sec-Fetch-Site': "same-origin",
    'Sec-Fetch-Mode': "cors",
    'Referer': "https://provider.kareo.com/dr-melissa-chinn",
    'Accept-Encoding': "gzip, deflate, br",
    'Accept-Language': "en-GB,en-US;q=0.9,en;q=0.8",
    'Cookie': "amplitude_id_7dc03f42fd7761eb87f8dd319f7176e8kareo.com=eyJkZXZpY2VJZCI6IjhkYTIxOWZhLWVmMGMtNGJlYy05ZDEzLTY5YmU4M2U0MGE3NVIiLCJ1c2VySWQiOm51bGwsIm9wdE91dCI6ZmFsc2UsInNlc3Npb25JZCI6MTU4MTUxMDIxMzYxMSwibGFzdEV2ZW50VGltZSI6MTU4MTUxMDIxMzYxMSwiZXZlbnRJZCI6MCwiaWRlbnRpZnlJZCI6MCwic2VxdWVuY2VOdW1iZXIiOjB9",
    'Cache-Control': "no-cache",
    'Postman-Token': "30a4ef19-9b74-44f9-ac84-4f7bfa7421e9,bd2f060b-754a-4d51-b7aa-cdf67025d296",
    'Host': "provider.kareo.com",
    'cache-control': "no-cache"
    }

response = requests.request("GET", url, headers=headers, params=querystring)
response_json = response.json()
print(response_json)
# pdb.set_trace()
for x in response_json:
    print(datetime.datetime.fromtimestamp(x['startTime']/1000).strftime('%c'))
    print(datetime.datetime.fromtimestamp(x['endTime']/1000).strftime('%c'))

#  a = requests.get("https://restcountries.eu/rest/v2/name/"+country)
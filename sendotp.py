import requests

url = "https://middleware.havells.com:50001/RESTAdapter/CommonAPP/RequestOTP"

payload = "{\r\n   \"MobileNumber\":\"9892847950\",\r\n   \"applicationName\":\"Your OTP is\"\r\n}"
headers = {
  'Authorization': 'Basic Q0hBVF9IQVZFTExTOlBSRENIQVRAMTIzNA==',
  'Content-Type': 'application/json',
  'Cookie': 'saplb_*=(J2EE3788920)3788953'
}

response = requests.request("POST", url, headers=headers, data = payload)

print(response.text.encode('utf8'))

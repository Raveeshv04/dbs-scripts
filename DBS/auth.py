import requests
import json

url = "https://wsa260.cs1:6443/wsa/api/v2.0/login"

payload = json.dumps({
  "data": {
    "userName": "YWRtaW4=",
    "passphrase": "aXJvbnBvcnQ="
  }
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
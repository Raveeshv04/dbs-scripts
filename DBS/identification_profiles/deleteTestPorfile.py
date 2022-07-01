import requests

url = "https://198.19.10.98:6443/wsa/api/v3.0/web_security/identification_profiles?profile_names=testProfile"

payload={}
headers = {
  'Authorization': 'Basic YWRtaW46Q2lzY28hMjM='
}

response = requests.request("DELETE", url, headers=headers, data=payload, verify=False)

print(response.text)

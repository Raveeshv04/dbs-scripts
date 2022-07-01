import requests
import json

url = "https://198.19.10.98:6443/wsa/api/v3.0/web_security/identification_profiles"

payload = json.dumps({
  "identification_profiles": [
    {
      "profile_name": "testProfile",
      "status": "enable",
      "order": 1,
      "members": {
        "protocols": [
          "http",
          "https",
          "ftp"
        ],
        "ip": [
          "10.10.10.0/32",
          "10.10.11.0/32",
          "172.31.3.174/32",
          "10.10.32.96/27"
        ]
      }
    }
  ]
})
headers = {
  'Authorization': 'Basic YWRtaW46Q2lzY28hMjM=',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload, verify= False)

print("Response Status\t:{}\n\nResponse Content\t:{}\n\nResponse-Headers\t:{}".format( response.text, response.content, response.headers))

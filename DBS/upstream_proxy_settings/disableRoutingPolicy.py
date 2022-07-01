import requests
import json

url = "https://198.19.10.98:6443/wsa/api/v3.0/web_security/routing_policies"

payload = json.dumps({
  "routing_policies": [
    {
      "policy_status": "disable",
      "policy_name": "testRoutinPolicy"
    }
  ]
})
headers = {
  'Authorization': 'Basic YWRtaW46Q2lzY28hMjM=',
  'Content-Type': 'application/json'
}

response = requests.request("PUT", url, headers=headers, data=payload, verify=False)

print("Response Status\t:{}\n\nResponse Content\t:{}\n\nResponse-Headers\t:{}".format( response.text, response.content, response.headers))

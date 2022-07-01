import requests
import json

url = "https://198.19.10.98:6443/wsa/api/v3.0/web_security/routing_policies"

payload = json.dumps({
  "routing_policies": [
    {
      "policy_status": "enable",
      "policy_name": "testRoutinPolicy",
      "policy_description": "test protcol policy",
      "policy_order": 1,
      "membership": {
        "identification_profiles": [
          {
            "profile_name": "testProfile",
            "auth": "No Authentication"
          }
        ]
      },
      "ip_spoofing": "Do not use IP Spoofing",
      "routing_destination": {
        "upstream_proxy_group": "TestUpstreamProxyGroup"
      }
    }
  ]
})
headers = {
  'Authorization': 'Basic YWRtaW46Q2lzY28hMjM=',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload, verify=False)

print("Response Content\t:{}\n\nResponse-Headers\t:{}".format( response.text, response.headers))

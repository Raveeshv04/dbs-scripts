import requests
import json

url = "https://198.19.10.98:6443/wsa/api/v3.0/web_security/access_policies"

payload = json.dumps({
  "access_policies": [
    {
      "policy_status": "disable",
      "policy_name": "testAccessPolicy",
      "policy_order": 1,
      "membership": {
        "identification_profiles": [
          {
            "profile_name": "testProfile",
            "auth": "No Authentication"
          }
        ],
        "user_agents": {
          "predefined": [
            "Firefox",
            "Safari",
            "MSIE/10"
          ],
          "custom": [
            "Mozilla/. Gecko/. Firefox/"
          ],
          "is_inverse": 0
        }
      },
      "protocols_user_agents": {
        "state": "custom",
        "allow_connect_ports": [
          "20",
          "21",
          "1-65535"
        ],
        "block_protocols": [
          "ftp",
          "http"
        ],
        "block_custom_user_agents": [
          "Mozilla/.* Gecko/.* Firefox/, Mozilla/4.0 (compatible; MSIE 5.5;)",
          "test"
        ]
      }
    }
  ]
})
headers = {
  'Authorization': 'Basic YWRtaW46Q2lzY28hMjM=',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload, verify=False)

print("Response Status\t:{}\n\nResponse Content\t:{}\n\nResponse-Headers\t:{}".format( response.text, response.content, response.headers))

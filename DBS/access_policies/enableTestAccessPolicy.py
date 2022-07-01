import requests
import json

url = "https://198.19.10.98:6443/wsa/api/v3.0/web_security/access_policies"

payload = json.dumps({
  "access_policies": [
    {
      "policy_status": "enable",
      "policy_name": "testAccessPolicy ",
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
            "MSIE/11"
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
      },
      "objects": {
        "state": "use_global"
      },
      "http_rewrite_profile": "use_global",
      "avc": {
        "state": "use_global"
      },
      "policy_description": "new test policy",
      "policy_order": 1,
      "url_filtering": {
        "safe_search": {
          "status": "use_global"
        },
        "content_rating": {
          "status": "use_global"
        },
        "state": "custom",
        "exception_referred_embedded_content": {
          "state": "disable"
        },
        "update_cats_action": "use_global",
        "predefined_cats": {
          "block": [
            "Advertisements",
            "Alcohol"
          ],
          "warn": [
            "Arts",
            "Astrology"
          ],
          "monitor": [
            "Web-based Email"
          ]
        }
      },
      "amw_reputation": {
        "state": "use_global"
      }
    }
  ]
})
headers = {
  'Authorization': 'Basic YWRtaW46Q2lzY28hMjM=',
  'Content-Type': 'application/json'
}

response = requests.request("PUT", url, headers=headers, data=payload, verify=False)


print("Response Status\t:{}\n\nResponse Content\t:{}\n\nResponse-Headers\t:{}".format( response.text, response.content, response.headers))
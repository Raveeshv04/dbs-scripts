import requests
import json

url = "https://198.19.10.98:6443/wsa/api/v2.0/configure/network/upstream_proxy"

payload = json.dumps({
  "group_name": "TestUpstreamProxyGroup",
  "failure_handling": "connect",
  "load_balancing": "none",
  "proxy_servers": [
    {
      "host": "10.10.192.31",
      "retries": 1,
      "port": 22
    }
  ]
})
headers = {
  'Authorization': 'Basic YWRtaW46Q2lzY28hMjM=',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload, verify=False)

print("Response Content\t:{}\n\nResponse-Headers\t:{}".format( response.text, response.headers))
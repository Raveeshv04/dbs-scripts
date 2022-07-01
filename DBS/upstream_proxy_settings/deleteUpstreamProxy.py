import requests
import json

url = "https://198.19.10.98:6443/wsa/api/v2.0/configure/network/upstream_proxy/"

payload = json.dumps({
  "proxy_group": "TestUpstreamProxyGroup"
})
headers = {
  'Authorization': 'Basic YWRtaW46Q2lzY28hMjM=',
  'Content-Type': 'application/json'
}

response = requests.request("DELETE", url, headers=headers, data=payload, verify=False)

print("Response Status\t:{}\n\nResponse Content\t:{}\n\nResponse-Headers\t:{}".format( response.text, response.content, response.headers))

import requests

url = "https://198.19.10.98:6443/wsa/api/v2.0/configure/network/upstream_proxy"

payload={}
headers = {
  'Authorization': 'Basic YWRtaW46Q2lzY28hMjM='
}

response = requests.request("GET", url, headers=headers, data=payload, verify=False)

print("Response Content\t:{}\n\nResponse-Headers\t:{}".format( response.text, response.headers))

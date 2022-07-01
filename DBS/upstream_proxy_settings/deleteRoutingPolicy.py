import requests

url = "https://198.19.10.98:6443/wsa/api/v3.0/web_security/routing_policies?policy_names=testRoutinPolicy"

payload = ""
headers = {
  'Authorization': 'Basic YWRtaW46Q2lzY28hMjM='
}

response = requests.request("DELETE", url, headers=headers, data=payload, verify=False)

print("Response Status\t:{}\n\nResponse Content\t:{}\n\nResponse-Headers\t:{}".format( response.text, response.content, response.headers))

import requests

url = "https://198.19.10.98:6443/wsa/api/v3.0/system_admin/configuration_file"

payload={'action': 'save',
'filename': 'save_config_file.xml',
'passphrase_action': 'encrypt'}
files=[

]
headers = {
  'Authorization': 'Basic YWRtaW46Q2lzY28hMjM='
}

response = requests.request("PUT", url, headers=headers, data=payload, files=files, verify=False)

print("Response Status\t:{}\n\nResponse Content\t:{}\n\nResponse-Headers\t:{}".format( response.text, response.content, response.headers))
import requests

url = "https://198.19.10.98:6443/wsa/api/v3.0/system_admin/configuration_file"

payload = ""
headers = {
  'Authorization': 'Basic YWRtaW46Q2lzY28hMjM='
}

response = requests.request("GET", url, headers=headers, data=payload, verify=False)

cfg_file = open ("swa_config_sample.xml", "w")
cfg_file.write(response.text)
cfg_file.close()
import requests, urllib3
import base64, sys
import json, yaml


urllib3.disable_warnings() #suppress output about insecure requests

class wsa:

    def __getToken__(self):
        self.username = base64.b64encode(self.username.encode("utf-8"))
        self.password = base64.b64encode(self.password.encode("utf-8"))

        login_endpoint = "/wsa/api/v2.0/login"
        body = {
            "data":
                {
                    "userName": str(self.username, "utf-8"),
                    "passphrase": str(self.password, "utf-8")
                }
        }
        resp = requests.post(self.wsa_base_url + login_endpoint, headers=self.headers, json=body, verify=False)
        resp_json = json.loads(resp.text)
        self.__token = resp_json["data"]["jwtToken"]

    def __init__(self, username, password , wsa_base_url , file_save_location):
        self.username = username
        self.password = password
        self.file_save_location = file_save_location
        self.policy_endpoint = "/wsa/api/v3.0/web_security/access_policies"
        self.config_files_endpoint = "wsa/api/v3.0/system_admin/configuration_file"
        self.wsa_base_url = wsa_base_url
        self.headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
        self.headers["jwtToken"] = self.__getToken




    def add_policy(self,access_policies):
        try:
            resp = requests.post(self.wsa_base_url + self.policy_endpoint, headers=self.headers, json=access_policies, verify=False)

        except requests.exceptions.RequestException as e:
            raise SystemExit(e)


    def retrive_policy(self):
        try:
            resp = requests.get(self.wsa_base_url + self.policy_endpoint, headers=self.headers, verify=False)
            resp_json = json.loads(resp.text)
            print(resp_json)

        except requests.exceptions.RequestException as e:
            raise SystemExit(e)


    def update_policy(self, policy):
        try:
            resp = requests.put(self.wsa_base_url + self.policy_endpoint, headers=self.headers, json=access_policies, verify=False)

        except requests.exceptions.RequestException as e:
            raise SystemExit(e)


    def get_config_file(self , filename):
        try:
            get_config_header = self.headers
            get_config_header["filename"] = filename
            resp = requests.get(self.wsa_base_url + self.config_files_endpoint, headers = get_config_header, verify=False)

            filePath = './data.csv'
            with open(filePath, "wb") as f: 
                f.write(resp.content)
            print("File saved")

        except requests.exceptions.RequestException as e:
            raise SystemExit(e)


    def update_config_files(self, config_file):
        try:
            get_config_header = self.headers
            get_config_header["Content-Type"] = "multipart/form-data"
            resp = requests.put(self.wsa_base_url + self.config_files_endpoint, headers=self.headers, json = config_file, verify=False)

        except requests.exceptions.RequestException as e:
            raise SystemExit(e)

 

if __name__ == '__main__':
    wsa_obj = wsa("admin" , "Cisco!23" , "http://198.19.10.98:6443" , "./")
    wsa_obj.retrive_policy()
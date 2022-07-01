import sys
import base64
import json
import yaml
import argparse
import requests
import pprint
import urllib3

urllib3.disable_warnings()

class WSAUtil(object):
    def __init__(self,wsa,headers):
        self.wsa=wsa
        self.headers=headers

        parser = argparse.ArgumentParser(usage='''WSAUtil.py <command> [<args>]
The available <command>'s are:
    get     get an exisiting WSA Resource
    create  to create an new WSA Resource
    update    to update an existing WSA Resource
        ''')
        parser.add_argument('command')

        # Read the first argument (get/create)
        args = parser.parse_args(sys.argv[1:2])
        # use dispatch pattern to invoke method with same name of the argument
        getattr(self, args.command)()

    def get(self):
        parser = argparse.ArgumentParser(usage='''WSAUtil.py get <resource> [<args>]
The available <resource>'s are:
    routing-policy    get an exisiting WSA Resource
    access-policy     to create an new WSA Resource
        ''')
        parser.add_argument('resource')
        parser.add_argument('-e','--export',required=False,help='Exporting the JSON content to file')

        args = parser.parse_args(sys.argv[2:])
        getattr(self,'get_'+args.resource.replace('-','_'))(self.wsa,self.headers,args.export)

    def create(self):
        parser = argparse.ArgumentParser(usage='''WSAUtil.py create <resource> [<args>]
The available <resource>'s are:
    routing-policy    get an exisiting WSA Resource
    access-policy     to create an new WSA Resource
        ''')
        parser.add_argument('resource')
        parser.add_argument('-f', '--file', required = True, help="supported file fo creating resource")

        args = parser.parse_args(sys.argv[2:])
        getattr(self, 'create_' + args.resource.replace('-', '_'))(self.wsa, self.headers,args.file)

    def update(self):
        parser = argparse.ArgumentParser(usage='''WSAUtil.py edit <resource> [<args>]
The available <resource>'s are:
    routing-policy    get an exisiting WSA Resource
    access-policy     to create an new WSA Resource
            ''')
        parser.add_argument('resource')
        parser.add_argument('-f', '--file', required=True, help="supported file fo creating resource")

        args = parser.parse_args(sys.argv[2:])
        getattr(self, 'update_' + args.resource.replace('-', '_'))(self.wsa, self.headers, args.file)

    def getToken(self,wsa, headers):
        # username and password must be specified as base64 encoded strings in the body of the token request
        username = base64.b64encode(wsa["username"].encode("utf-8"))
        password = base64.b64encode(wsa["password"].encode("utf-8"))

        login_endpoint = "/wsa/api/v2.0/login"
        body = {
            "data":
                {
                    "userName": str(username, "utf-8"),
                    "passphrase": str(password, "utf-8")
                }
        }

        # make POST request to WSA with login endpoint
        resp = requests.post(wsa["url"] + login_endpoint, headers=headers, json=body, verify=False)
        resp_json = json.loads(resp.text)
        token = resp_json["data"]["jwtToken"]

        return token

    def get_access_policy(self,wsa, headers,export=None):
        token = self.getToken(wsa, headers)
        headers["jwtToken"] = token

        policy_endpoint = "/wsa/api/v3.0/web_security/access_policies"

        # Make GET request to WSA
        resp = requests.get(wsa["url"] + policy_endpoint, headers=headers, verify=False)
        if export:
            with open(export,mode='w') as fw:
                fw.write(resp.text)

        if resp.text:
            pprint.pprint(resp.status_code, resp.text)
        else:
            pprint.pprint(resp.status_code)  # Print result of API call

    def create_access_policy(self,wsa, headers, file):
        token = self.getToken(wsa, headers)
        headers["jwtToken"] = token

        policy_endpoint = "/wsa/api/v3.0/web_security/access_policies"
        json_data = {}
        with open(file) as fp:
            json_data = fp.read()
        # Make POST request to WSA
        print('Creating Access Policy ...')
        resp = requests.post(wsa["url"] + policy_endpoint, headers=headers, json=json.loads(json_data), verify=False)
        if resp.text:
            pprint.pprint(resp.status_code+'\n'+resp.text,indent=2)
        else:
            pprint.pprint(resp.status_code,indent=2)

    def update_access_policy(self,wsa, headers, file):
        token = self.getToken(wsa, headers)
        headers["jwtToken"] = token

        policy_endpoint = "/wsa/api/v3.0/web_security/access_policies"
        json_data = {}
        with open(file) as fp:
            json_data = fp.read()
        # Make PUT request to WSA
        print('Updating Existing Access Policy ...')
        resp = requests.put(wsa["url"] + policy_endpoint, headers=headers, json=json.loads(json_data), verify=False)
        if resp.text:
            pprint.pprint(resp.status_code+'\n'+resp.text,indent=2)
        else:
            pprint.pprint(resp.status_code,indent=2)

    def get_routing_policy(self,wsa, headers,export):
        token = self.getToken(wsa, headers)
        headers["jwtToken"] = token

        policy_endpoint = "/wsa/api/v3.0/web_security/routing_policies"

        # Make GET request to WSA
        resp = requests.get(wsa["url"] + policy_endpoint, headers=headers, verify=False)
        if export:
            with open(export,mode='w') as fw:
                fw.write(resp.text)

        if resp.text:
            pprint.pprint(resp.status_code+'\n'+resp.text,indent=2)
        else:
            pprint.pprint(resp.status_code,indent=2)  # Print result of API call

    def create_routing_policy(self,wsa, headers, file):
        # Retrieve token to authenticate request and save it in request headers
        token = self.getToken(wsa, headers)
        headers["jwtToken"] = token

        policy_endpoint = "/wsa/api/v3.0/web_security/routing_policies"
        json_data = {}
        with open(file) as fp:
            json_data = fp.read()

        print("Creating Routing Policy ...")
        # Make POST request to WSA
        resp = requests.post(wsa["url"] + policy_endpoint, headers=headers, json=json.loads(json_data), verify=False)
        if resp.text:
            pprint.pprint(resp.status_code+'\n'+resp.text,indent=2)
        else:
            pprint.pprint(resp.status_code,indent=2)

    def update_routing_policy(self,wsa, headers, file):
        # Retrieve token to authenticate request and save it in request headers
        token = self.getToken(wsa, headers)
        headers["jwtToken"] = token

        policy_endpoint = "/wsa/api/v3.0/web_security/routing_policies"
        json_data = {}
        with open(file) as fp:
            json_data = fp.read()

        print("Updating Existing Routing Policy ...")
        # Make PUT request to WSA
        resp = requests.put(wsa["url"] + policy_endpoint, headers=headers, json=json.loads(json_data), verify=False)
        if resp.text:
            pprint.pprint(resp.status_code+'\n'+resp.text,indent=2)
        else:
            pprint.pprint(resp.status_code,indent=2)


if __name__ == '__main__':
    wsa = yaml.safe_load(open("wsa_cred.yml"))
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    WSAUtil(wsa,headers)
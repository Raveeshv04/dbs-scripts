#!/usr/bin/env python3
'''
Copyright (c) 2020 Cisco and/or its affiliates.
This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.1 (the "License"). You may obtain a copy of the
License at
               https://developer.cisco.com/docs/licenses
All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.
'''
import requests, urllib3
import base64, sys
import json, yaml

urllib3.disable_warnings() #suppress output about insecure requests

#Each API call to the WSA must be authenticated with a token.
#This function returns a JSON web token that can then be used to authenticate future requests
def getToken(wsa, headers):
    #username and password must be specified as base64 encoded strings in the body of the token request
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

    #make POST request to WSA with login endpoint
    resp = requests.post(wsa["url"]+login_endpoint, headers=headers, json=body, verify=False)
    resp_json = json.loads(resp.text)
    token = resp_json["data"]["jwtToken"]

    return token

def getAccessPolicy(wsa, headers):

    #Retrieve token to authenticate request and save it in request headers
    token = getToken(wsa, headers)
    headers["jwtToken"] = token

    policy_endpoint = "/wsa/api/v3.0/web_security/access_policies"

    #Make PUT request to WSA with bypass proxy endpoint with the body specified in the add_bypass.yml file
    resp = requests.get(wsa["url"]+policy_endpoint, headers=headers, verify=False)

    from pprint import pprint
    pprint(resp.text) #Print result of API call

def createAccessPolicy(wsa, headers,file):

    #Retrieve token to authenticate request and save it in request headers
    token = getToken(wsa, headers)
    headers["jwtToken"] = token

    policy_endpoint = "/wsa/api/v3.0/web_security/access_policies"
    json_data={}
    with open(file) as fp:
        json_data=fp.read()
    #Make PUT request to WSA with bypass proxy endpoint with the body specified in the add_bypass.yml file
    resp = requests.post(wsa["url"]+policy_endpoint, headers=headers,json=json.loads(json_data),verify=False)

    print(resp.status_code,resp.text)

if __name__ == '__main__':
    #URL/IP address, username, and password of the WSA are all specified in the wsa_cred.yml file
    wsa = yaml.safe_load(open("wsa_cred.yml"))

    #Necessary headers for each request
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    #Check to make sure a function is provided when the program is run
    n = len(sys.argv)
    if n <= 1:
        print("Script requires at least one argument from list: getAccessPolicy createAccessPolicy")

    funcs = sys.argv[1:]

    #Check which options are specified as arguments and run the functions associated with each option. If an invalid option is provided, print out an error message
    for func in funcs:
        if str(func) == "getAccessPolicy":
            getAccessPolicy(wsa, headers)
        elif str(func) == "createAccessPolicy":
            createAccessPolicy(wsa, headers,'test-AP1.json')
        else:
            print("Invalid argument: {}. Provide argument from the following: getAccessPolicy createAccessPolicy".format(str(func)))
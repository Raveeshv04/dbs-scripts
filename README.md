# gve_devnet_wsa_capabilities_script
for exploring WSA capabilities via python through API

## Contacts
* Harsh PV (hpv@cisco.com)
* Raveesh V (rmalyava@ciso.com)

## Solution Components
* python
* requests
* WSA API
* Ansible

## Related Sandbox/Lab Environment
Have used the Dcloud Web Security Applicance V12.0 Lab

## Installation/Configuration
Create Virtual environment and activate it
```commandline
python3 -m venv venv
source venv/bin/activate
```

Install Python Dependecies for the script
```commandline
pip install -r requirements.txt
```

please update device specific information in `wsa_cred.yml`.

```python
# wsa_cred.yml
url: "https://<ip>:<port>"
username: "username"
password: "passowrd"
```

## Usage

#### `wsa.py`
to get help message type the command as follows

    $ python wsa.py 
run respective functions of the command as follows

    $ python wsa.py getAccessPolicy
    $ python wsa.py createAccessPolicy

#### `WSAUtil.py`
to get help message type the command as follows
```python
python WSAUtil.py -h
python WSAUtil.py <command> <resource> <args>
```
######supported *command* 
- **get** to get the WSA Resource.  
- **create** to create new WSA Resource.

######supported *resources*  
- **routing-policy** Routing policy of WSA
- **access-policy** Access policy of WSA

Examples
```python
python WSAUtil.py get access-policy
python WSAUtil.py get access-policy -e <output-file>
python WSAUtil.py create access-policy -f <input-file>
```

#### Ansible Playbook `wsa-playbook.yml`
Running ansible playbook
```python
ansible-playbook wsa-playbook.yml
ansible-playbook wsa-playbook.yml -vvv
ansible-playbook wsa-playbook.yml -t access-policies
```


# Screenshots

![/IMAGES/0image.png](/IMAGES/0image.png)

### LICENSE

Provided under Cisco Sample Code License, for details see [LICENSE](LICENSE.md)

### CODE_OF_CONDUCT

Our code of conduct is available [here](CODE_OF_CONDUCT.md)

### CONTRIBUTING

See our contributing guidelines [here](CONTRIBUTING.md)

#### DISCLAIMER:
<b>Please note:</b> This script is meant for demo purposes only. All tools/ scripts in this repo are released for use "AS IS" without any warranties of any kind, including, but not limited to their installation, use, or performance. Any use of these scripts and tools is at your own risk. There is no guarantee that they have been through thorough testing in a comparable environment and we are not responsible for any damage or data loss incurred with their use.
You are responsible for reviewing and testing any scripts you run thoroughly before use in any non-testing environment.
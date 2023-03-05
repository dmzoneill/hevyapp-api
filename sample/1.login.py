from pprint import pprint
import requests
import os
import sys

strong_username = os.getenv('strong_username')
strong_password = os.environ.get('strong_password')
strong_device_uuid = os.environ.get('strong_device_uuid')
strong_application_id = os.environ.get('strong_application_id')

if strong_username is None:
    sys.exit(1)

if strong_password is None:
    sys.exit(2)

if strong_device_uuid is None:
    sys.exit(3)

if strong_application_id is None:
    sys.exit(4)

headers = {
    'Host': 'ws13.strongapp.co',
    'x-parse-application-id': strong_application_id,
    'x-parse-app-build-version': '257',
    'x-parse-app-display-version': '2.7.9',
    'x-parse-os-version': '13',
    'user-agent': 'Parse Android SDK API Level 33',
    'x-parse-installation-id': strong_device_uuid,
    'content-type': 'application/json',
    'pragma': 'no-cache',
    'cache-control': 'no-cache'
}

data = '{"password":"' + strong_password + '","username":"' + strong_username + '","_method":"GET"}'
endpoint = "https://ws13.strongapp.co/parse/login"

response = requests.post(endpoint, headers=headers, data=data)

pprint(headers)
pprint(data)
pprint(response.json())
pprint(response.ok)
pprint(response.status_code)
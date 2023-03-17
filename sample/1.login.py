from pprint import pprint
import requests
import os
import sys

hevy_username = os.getenv("hevy_username")
hevy_password = os.environ.get("hevy_password")

if hevy_username is None:
    sys.exit(1)

if hevy_password is None:
    sys.exit(2)

headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Type": "application/json",
    "DNT": "1",
    "Origin": "https://www.hevy.com",
    "Pragma": "no-cache",
    "Referer": "https://www.hevy.com/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "cross-site",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
    "sec-ch-ua": '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Linux"',
    "x-api-key": "shelobs_hevy_web",
}

json_data = {
    "emailOrUsername": hevy_username,
    "password": hevy_password,
}

response = requests.post(
    "https://api.hevyapp.com/login", headers=headers, json=json_data
)

pprint(headers)
pprint(json_data)
pprint(response.json())
pprint(response.ok)
pprint(response.status_code)

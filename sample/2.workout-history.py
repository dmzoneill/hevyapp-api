from pprint import pprint
import requests
from requests_toolbelt.utils import dump
import os
import sys
import json


class Hevy:
    def __init__(self):
        self.endpoint = "https://api.hevyapp.com"
        self.hevy_username = os.getenv("hevy_username")
        self.hevy_password = os.environ.get("hevy_password")
        self.request_no = 0

        if self.hevy_username is None:
            sys.exit(1)

        if self.hevy_password is None:
            sys.exit(2)

        self.headers = {
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

    def WebRequest(self, method, query, data=None):
        self.request_no += 1
        print("==================" + str(self.request_no) + "===================")

        if method == "POST":
            self.response = requests.post(
                self.endpoint + query, json=data, headers=self.headers
            )
        else:
            self.response = requests.get(self.endpoint + query, headers=self.headers)

        data = dump.dump_all(self.response)
        print(data.decode("utf-8"))

        print(self.response.status_code)
        pprint(self.response.text)

    def Login(self):
        data = {}
        data["password"] = self.hevy_password
        data["emailOrUsername"] = self.hevy_username

        self.WebRequest("POST", "/login", data)

        self.headers["x-api-key"] = "klean_kanteen_insulated"
        self.headers["auth-token"] = self.response.json()["auth_token"]

    def GetUser(self):
        self.WebRequest("GET", "/account")

    def GetWorkouts(self):
        all_workouts = []
        workouts = []
        cache_file = "workouts.json"

        if os.path.isfile(cache_file):
            with open(cache_file) as f:
                return json.loads(f.read())

        self.WebRequest("GET", "/workouts_batch/0")
        workouts = self.response.json()
        all_workouts += workouts

        while len(workouts) == 20:
            self.WebRequest("GET", "/workouts_batch/" + str(workouts[19]["index"]))
            workouts = self.response.json()
            all_workouts += workouts

        with open(cache_file, "w") as file1:
            file1.write(json.dumps(all_workouts))
            file1.close()

    def GetWorkOutsCount(self):
        self.WebRequest("GET", "/workout_count")


s = Hevy()
s.Login()
s.GetUser()
s.GetWorkouts()
s.GetWorkOutsCount()

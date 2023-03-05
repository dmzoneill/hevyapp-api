## login

### request

```
import requests

headers = {
    'accept': 'application/json, text/plain, */*',
    'x-api-key': 'klean_kanteen_insulated',
    'Content-Type': 'application/json',
    'Host': 'api.hevyapp.com',
    'User-Agent': 'okhttp/4.9.3',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
}

json_data = {
    'emailOrUsername': 'xxxxxxxxxxxxxxxx',
    'password': 'xxxxxxxxxxxxxxxx',
}

response = requests.post('https://api.hevyapp.com/login', headers=headers, json=json_data)
```

### response
```
{
	"auth_token": "73cbb807-zzzz-xxxx-yyyy-611e773c2b1b"
}
```
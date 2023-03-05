## Feed workouts paged

### request

```
import requests

headers = {
    'accept': 'application/json, text/plain, */*',
    'x-api-key': 'klean_kanteen_insulated',
    'auth-token': '73cbb807-a563-4b22-902c-611e773c2b1b',
    'Host': 'api.hevyapp.com',
    'User-Agent': 'okhttp/4.9.3',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
}

response = requests.get('https://api.hevyapp.com/feed_workouts_paged', headers=headers)
```

### response
```
{
	"workouts": []
}
```
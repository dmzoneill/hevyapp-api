## Workout count

### request

```
import requests

headers = {
    'accept': 'application/json, text/plain, */*',
    'x-api-key': 'klean_kanteen_insulated',
    'auth-token': '.......-.....-....-....-.............',
    'Host': 'api.hevyapp.com',
    'User-Agent': 'okhttp/4.9.3',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
}

response = requests.get('https://api.hevyapp.com/workout_count', headers=headers)
```

### response
```
{
	"workout_count": 0
}
```
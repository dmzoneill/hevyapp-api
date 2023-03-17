## User preferences

### request

```
import requests

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'DNT': '1',
    'Origin': 'https://www.hevy.com',
    'Pragma': 'no-cache',
    'Referer': 'https://www.hevy.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    'auth-token': '.......-.....-....-....-.............',
    'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'x-api-key': 'shelobs_hevy_web',
}

response = requests.get('https://api.hevyapp.com/user_preferences', headers=headers)
```

### response
```
{
	"username": "ddddddddddd",
	"language": null,
	"weight_unit": "kg",
	"distance_unit": "kilometers",
	"body_measurement_unit": "cm",
	"first_weekday": null,
	"default_rest_timer_seconds": null,
	"workout_keep_awake": null,
	"disabled_review_request": null,
	"superset_scrolling": false,
	"plate_calculator_enabled": true,
	"previous_workout_values_from_routine": null,
	"rpe_enabled": false,
	"timer_volume": null,
	"inline_set_timer_enabled": true
}
```
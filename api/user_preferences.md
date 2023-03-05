## User preferences

### request

```
import requests

headers = {
    'accept': 'application/json, text/plain, */*',
    'x-api-key': 'klean_kanteen_insulated',
    'auth-token': 'xxxxxxxxxxxx-xxxx-zzzz-yyyy-ccccccccccccccc',
    'Host': 'api.hevyapp.com',
    'User-Agent': 'okhttp/4.9.3',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
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
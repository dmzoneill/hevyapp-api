## New routine

### request

```
import requests

headers = {
    'accept': 'application/json, text/plain, */*',
    'x-api-key': 'klean_kanteen_insulated',
    'auth-token': '.......-.....-....-....-.............',
    'Content-Type': 'application/json',
    'Host': 'api.hevyapp.com',
    'User-Agent': 'okhttp/4.9.3',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
}

json_data = {
    'routine': {
        'title': '2. Quads/Calves',
        'folder_id': None,
        'index': -1,
        'exercises': [
            {
                'exercise_template_id': '3303376C',
                'notes': '',
                'sets': [
                    {
                        'index': 0,
                        'indicator': 'normal',
                        'distance_meters': 0,
                        'duration_seconds': 15,
                    },
                ],
                'rest_seconds': 0,
            },
            {
                'exercise_template_id': '062AB91A',
                'notes': '',
                'sets': [
                    {
                        'index': 0,
                        'indicator': 'normal',
                        'weight_kg': 86,
                        'reps': 8,
                    },
                    {
                        'index': 1,
                        'indicator': 'normal',
                        'weight_kg': 81,
                        'reps': 8,
                    },
                    {
                        'index': 2,
                        'indicator': 'normal',
                        'weight_kg': 76,
                        'reps': 8,
                    },
                ],
                'rest_seconds': 120,
            },
            {
                'exercise_template_id': '75A4F6C4',
                'notes': '',
                'sets': [
                    {
                        'index': 0,
                        'indicator': 'normal',
                        'weight_kg': 69,
                        'reps': 8,
                    },
                    {
                        'index': 1,
                        'indicator': 'normal',
                        'weight_kg': 69,
                        'reps': 8,
                    },
                    {
                        'index': 2,
                        'indicator': 'normal',
                        'weight_kg': 69,
                        'reps': 8,
                    },
                ],
                'rest_seconds': 120,
            },
        ],
        'program_id': None,
    },
}

response = requests.post('https://api.hevyapp.com/routine', headers=headers, json=json_data)
```

### response
```

```
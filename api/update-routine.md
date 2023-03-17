## Update routine

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
        'title': '1. Shoulders/Lats',
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
                'exercise_template_id': '67280085',
                'notes': '',
                'sets': [
                    {
                        'index': 0,
                        'indicator': 'normal',
                        'weight_kg': 35,
                        'reps': 8,
                    },
                    {
                        'index': 1,
                        'indicator': 'normal',
                        'weight_kg': 35,
                        'reps': 8,
                    },
                    {
                        'index': 2,
                        'indicator': 'normal',
                        'weight_kg': 35,
                        'reps': 8,
                    },
                ],
                'rest_seconds': 0,
            },
            {
                'exercise_template_id': 'F1E57334',
                'notes': '',
                'sets': [
                    {
                        'index': 0,
                        'indicator': 'normal',
                        'weight_kg': 40,
                        'reps': 8,
                    },
                    {
                        'index': 1,
                        'indicator': 'normal',
                        'weight_kg': 40,
                        'reps': 8,
                    },
                    {
                        'index': 2,
                        'indicator': 'normal',
                        'weight_kg': 40,
                        'reps': 8,
                    },
                ],
                'rest_seconds': 0,
            },
            {
                'exercise_template_id': '3601968B',
                'notes': '',
                'sets': [
                    {
                        'index': 0,
                        'indicator': 'normal',
                        'weight_kg': 50,
                        'reps': 8,
                    },
                    {
                        'index': 1,
                        'indicator': 'normal',
                        'weight_kg': 50,
                        'reps': 8,
                    },
                    {
                        'index': 2,
                        'indicator': 'normal',
                        'weight_kg': 50,
                        'reps': 8,
                    },
                ],
                'rest_seconds': 0,
            },
            {
                'exercise_template_id': 'F1D60854',
                'notes': '',
                'sets': [
                    {
                        'index': 0,
                        'indicator': 'normal',
                        'weight_kg': 91,
                        'reps': 8,
                    },
                    {
                        'index': 1,
                        'indicator': 'normal',
                        'weight_kg': 91,
                        'reps': 8,
                    },
                    {
                        'index': 2,
                        'indicator': 'normal',
                        'weight_kg': 91,
                        'reps': 8,
                    },
                ],
                'rest_seconds': 0,
            },
            {
                'exercise_template_id': '36E8F14E',
                'notes': '',
                'sets': [
                    {
                        'index': 0,
                        'indicator': 'normal',
                        'weight_kg': 50,
                        'reps': 8,
                    },
                    {
                        'index': 1,
                        'indicator': 'normal',
                        'weight_kg': 50,
                        'reps': 8,
                    },
                    {
                        'index': 2,
                        'indicator': 'normal',
                        'weight_kg': 50,
                        'reps': 8,
                    },
                ],
                'rest_seconds': 0,
            },
            {
                'exercise_template_id': '6A6C31A5',
                'notes': '',
                'sets': [
                    {
                        'index': 0,
                        'indicator': 'normal',
                        'weight_kg': 68,
                        'reps': 8,
                    },
                    {
                        'index': 1,
                        'indicator': 'normal',
                        'weight_kg': 68,
                        'reps': 8,
                    },
                    {
                        'index': 2,
                        'indicator': 'normal',
                        'weight_kg': 68,
                        'reps': 8,
                    },
                ],
                'rest_seconds': 0,
            },
            {
                'exercise_template_id': '08A2974E',
                'notes': '',
                'sets': [
                    {
                        'index': 0,
                        'indicator': 'normal',
                        'weight_kg': 25,
                        'reps': 8,
                    },
                    {
                        'index': 1,
                        'indicator': 'normal',
                        'weight_kg': 25,
                        'reps': 8,
                    },
                    {
                        'index': 2,
                        'indicator': 'normal',
                        'weight_kg': 25,
                        'reps': 8,
                    },
                ],
                'rest_seconds': 0,
            },
            {
                'exercise_template_id': 'BC10A922',
                'notes': '',
                'sets': [
                    {
                        'index': 0,
                        'indicator': 'normal',
                        'reps': 8,
                    },
                    {
                        'index': 1,
                        'indicator': 'normal',
                        'reps': 8,
                    },
                    {
                        'index': 2,
                        'indicator': 'normal',
                        'reps': 8,
                    },
                ],
                'rest_seconds': 0,
            },
            {
                'exercise_template_id': 'F8356514',
                'notes': '',
                'sets': [
                    {
                        'index': 0,
                        'indicator': 'normal',
                        'reps': 8,
                    },
                    {
                        'index': 1,
                        'indicator': 'normal',
                        'reps': 8,
                    },
                    {
                        'index': 2,
                        'indicator': 'normal',
                        'reps': 8,
                    },
                ],
                'rest_seconds': 0,
            },
            {
                'exercise_template_id': '09C9F635',
                'notes': '',
                'sets': [
                    {
                        'index': 0,
                        'indicator': 'normal',
                        'reps': 8,
                    },
                    {
                        'index': 1,
                        'indicator': 'normal',
                        'reps': 8,
                    },
                    {
                        'index': 2,
                        'indicator': 'normal',
                        'reps': 8,
                    },
                ],
                'rest_seconds': 0,
            },
        ],
        'program_id': None,
    },
}

response = requests.put('https://api.hevyapp.com/routine/89db8e68-e28b-4ce6-b8fe-aef4b236db21', headers=headers, json=json_data)
```

### response
```

```
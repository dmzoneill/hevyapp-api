## Feed workouts paged

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

response = requests.get('https://api.hevyapp.com/account', headers=headers)

```

### response
```
{
   "id":".......-.....-....-....-.............",
   "username":"................",
   "email":"................",
   "full_name":"...............",
   "description":"Gym bro",
   "profile_pic":"https://pump-app.s3.eu-west-2.amazonaws.com/profile-images/.....................jpg",
   "likes_push_enabled":true,
   "follows_push_enabled":true,
   "comments_push_enabled":true,
   "comment_mention_push_enabled":true,
   "comment_discussion_push_enabled":true,
   "private_profile":true,
   "follower_count":0,
   "following_count":0,
   "created_at":"2023-03-05T17:50:28.769Z",
   "last_workout_at":"2023-03-15T10:49:39.873Z",
   "comment_replies_push_enabled":true,
   "accepted_terms_and_conditions":true,
   "is_coached":false
}
```
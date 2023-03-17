## Feed workouts paged

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

response = requests.get('https://api.hevyapp.com/feed_workouts_paged', headers=headers)
```

### response
```
{
   "workouts":[
      {
         "id":"6c10fadc-5b5c-43f0-9b95-6c38caf99944",
         "short_id":"9zxJ5CLFduN",
         "index":13490647,
         "name":"4. Abs / Cardio",
         "description":"",
         "start_time":1678869822,
         "end_time":1678877371,
         "created_at":"2023-03-15T10:49:39.119Z",
         "updated_at":"2023-03-15T10:49:39.119Z",
         "routine_id":"81272c28-2788-41d0-892f-fc94803f6f48",
         "apple_watch":false,
         "user_id":"93620a45-5bef-4a70-baab-5c1058a88046",
         "username":"bitwiseshift",
         "profile_image":"https://pump-app.s3.eu-west-2.amazonaws.com/profile-images/bitwiseshift-e4a12928-f0f3-4a87-adc5-99c1daae5951.jpg",
         "verified":false,
         "nth_workout":181,
         "like_count":0,
         "is_liked_by_user":false,
         "like_images":[
            
         ],
         "comments":[
            
         ],
         "comment_count":0,
         "media":[
            
         ],
         "image_urls":[
            
         ],
         "exercises":[
            {
               "id":"2918c5ad-f313-41b6-8a60-a91b40049b91",
               "title":"Elliptical Trainer",
               "es_title":"Entrenador Elíptico",
               "de_title":"Crosstrainer",
               "fr_title":"Vélo Elliptique",
               "it_title":"Ellittica",
               "pt_title":"Elíptico",
               "ko_title":null,
               "ja_title":null,
               "tr_title":"Eliptik Bisiklet",
               "ru_title":"Эллиптический тренажер",
               "zh_cn_title":"椭圆机",
               "zh_tw_title":"橢圓機",
               "superset_id":null,
               "rest_seconds":120,
               "notes":"",
               "exercise_template_id":"3303376C",
               "url":"https://pump-app.s3.eu-west-2.amazonaws.com/exercise-assets/21921201-Elliptical-Machine-Walk_Cardio.mp4",
               "exercise_type":"distance_duration",
               "equipment_category":"machine",
               "media_type":"video",
               "custom_exercise_image_url":null,
               "custom_exercise_image_thumbnail_url":"https://pump-app.s3.eu-west-2.amazonaws.com/exercise-thumbnails/21921201-Elliptical-Machine-Walk_Cardio_thumbnail@3x.jpg",
               "thumbnail_url":"https://pump-app.s3.eu-west-2.amazonaws.com/exercise-thumbnails/21921201-Elliptical-Machine-Walk_Cardio_thumbnail@3x.jpg",
               "muscle_group":"cardio",
               "other_muscles":[
                  
               ],
               "priority":8,
               "sets":[
                  {
                     "id":310860050,
                     "index":0,
                     "indicator":"normal",
                     "weight_kg":null,
                     "reps":null,
                     "distance_meters":0,
                     "duration_seconds":15,
                     "rpe":null,
                     "prs":[
                        
                     ],
                     "personalRecords":[
                        
                     ]
                  }
               ]
            },
            {
               "id":"95c7dfa9-5ca9-4bf6-8494-02e4f3d56eff",
               "title":"Hanging Leg Raise",
               "es_title":"Levantamiento de Piernas en Barra",
               "de_title":"Beinheben hängend",
               "fr_title":"Relevé de Jambes Suspendu",
               "it_title":"Leg Raise Appeso",
               "pt_title":"Elevação De Pernas Na Barra Fixa",
               "ko_title":null,
               "ja_title":null,
               "tr_title":"Hanging Leg Raise",
               "ru_title":"Подъем ног в висе",
               "zh_cn_title":"单杠曲腿上举",
               "zh_tw_title":"單槓曲腿上舉",
               "superset_id":null,
               "rest_seconds":120,
               "notes":"",
               "exercise_template_id":"F8356514",
               "url":"https://pump-app.s3.eu-west-2.amazonaws.com/exercise-assets/17641201-Hanging-Leg-Hip-Raise_Waist.mp4",
               "exercise_type":"reps_only",
               "equipment_category":"none",
               "media_type":"video",
               "custom_exercise_image_url":null,
               "custom_exercise_image_thumbnail_url":"https://pump-app.s3.eu-west-2.amazonaws.com/exercise-thumbnails/17641201-Hanging-Leg-Hip-Raise_Waist_thumbnail@3x.jpg",
               "thumbnail_url":"https://pump-app.s3.eu-west-2.amazonaws.com/exercise-thumbnails/17641201-Hanging-Leg-Hip-Raise_Waist_thumbnail@3x.jpg",
               "muscle_group":"abdominals",
               "other_muscles":[
                  
               ],
               "priority":0,
               "sets":[
                  {
                     "id":310860051,
                     "index":0,
                     "indicator":"normal",
                     "weight_kg":null,
                     "reps":6,
                     "distance_meters":null,
                     "duration_seconds":null,
                     "rpe":null,
                     "prs":[
                        
                     ],
                     "personalRecords":[
                        
                     ]
                  },
                  {
                     "id":310860052,
                     "index":1,
                     "indicator":"normal",
                     "weight_kg":null,
                     "reps":6,
                     "distance_meters":null,
                     "duration_seconds":null,
                     "rpe":null,
                     "prs":[
                        
                     ],
                     "personalRecords":[
                        
                     ]
                  },
                  {
                     "id":310860053,
                     "index":2,
                     "indicator":"normal",
                     "weight_kg":null,
                     "reps":6,
                     "distance_meters":null,
                     "duration_seconds":null,
                     "rpe":null,
                     "prs":[
                        
                     ],
                     "personalRecords":[
                        
                     ]
                  },
                  {
                     "id":310860054,
                     "index":3,
                     "indicator":"normal",
                     "weight_kg":null,
                     "reps":6,
                     "distance_meters":null,
                     "duration_seconds":null,
                     "rpe":null,
                     "prs":[
                        
                     ],
                     "personalRecords":[
                        
                     ]
                  }
               ]
            },
            {
               "id":"0a5f260f-2b3f-4c39-8909-0b99a62c8e2c",
               "title":"Lying Leg Raise",
               "es_title":"Levantamiento de Piernas Tumbado",
               "de_title":"Liegendes Beinheben",
               "fr_title":"Relevé de Jambes Allongé",
               "it_title":"Leg Raise Sdraiato",
               "pt_title":"Elevação De Pernas (Deitado)",
               "ko_title":null,
               "ja_title":null,
               "tr_title":"Çakı Hareketi",
               "ru_title":"Подъем ног лежа",
               "zh_cn_title":"躺式抬腿",
               "zh_tw_title":"躺式抬腿",
               "superset_id":null,
               "rest_seconds":120,
               "notes":"",
               "exercise_template_id":"09C9F635",
               "url":"https://pump-app.s3.eu-west-2.amazonaws.com/exercise-assets/11631201-Lying-Leg-Raise_Waist.mp4",
               "exercise_type":"reps_only",
               "equipment_category":"none",
               "media_type":"video",
               "custom_exercise_image_url":null,
               "custom_exercise_image_thumbnail_url":"https://pump-app.s3.eu-west-2.amazonaws.com/exercise-thumbnails/11631201-Lying-Leg-Raise_Waist_thumbnail@3x.jpg",
               "thumbnail_url":"https://pump-app.s3.eu-west-2.amazonaws.com/exercise-thumbnails/11631201-Lying-Leg-Raise_Waist_thumbnail@3x.jpg",
               "muscle_group":"abdominals",
               "other_muscles":[
                  
               ],
               "priority":8,
               "sets":[
                  {
                     "id":310860055,
                     "index":0,
                     "indicator":"normal",
                     "weight_kg":null,
                     "reps":8,
                     "distance_meters":null,
                     "duration_seconds":null,
                     "rpe":null,
                     "prs":[
                        
                     ],
                     "personalRecords":[
                        
                     ]
                  },
                  {
                     "id":310860056,
                     "index":1,
                     "indicator":"normal",
                     "weight_kg":null,
                     "reps":8,
                     "distance_meters":null,
                     "duration_seconds":null,
                     "rpe":null,
                     "prs":[
                        
                     ],
                     "personalRecords":[
                        
                     ]
                  },
                  {
                     "id":310860057,
                     "index":2,
                     "indicator":"normal",
                     "weight_kg":null,
                     "reps":8,
                     "distance_meters":null,
                     "duration_seconds":null,
                     "rpe":null,
                     "prs":[
                        
                     ],
                     "personalRecords":[
                        
                     ]
                  },
                  {
                     "id":310860058,
                     "index":3,
                     "indicator":"normal",
                     "weight_kg":null,
                     "reps":8,
                     "distance_meters":null,
                     "duration_seconds":null,
                     "rpe":null,
                     "prs":[
                        
                     ],
                     "personalRecords":[
                        
                     ]
                  },
                  {
                     "id":310860059,
                     "index":4,
                     "indicator":"normal",
                     "weight_kg":null,
                     "reps":8,
                     "distance_meters":null,
                     "duration_seconds":null,
                     "rpe":null,
                     "prs":[
                        
                     ],
                     "personalRecords":[
                        
                     ]
                  }
               ]
            },
            {
               "id":"8d764819-6d95-434f-a78c-a5c554b8f5da",
               "title":"Decline Crunch",
               "es_title":"Abdominal Corto en Banco Inclinado",
               "de_title":"Negativer Crunch",
               "fr_title":"Crunch Décliné",
               "it_title":"Crunch Declinato",
               "pt_title":"Abdominal Declinado",
               "ko_title":null,
               "ja_title":null,
               "tr_title":"Eğik Sehpada Yarım Mekik",
               "ru_title":"Скручивание в наклоне",
               "zh_cn_title":"斜板卷腹",
               "zh_tw_title":"斜板捲腹",
               "superset_id":null,
               "rest_seconds":120,
               "notes":"",
               "exercise_template_id":"BC10A922",
               "url":"https://pump-app.s3.eu-west-2.amazonaws.com/exercise-assets/02771201-Decline-Crunch_Waist.mp4",
               "exercise_type":"reps_only",
               "equipment_category":"none",
               "media_type":"video",
               "custom_exercise_image_url":null,
               "custom_exercise_image_thumbnail_url":"https://pump-app.s3.eu-west-2.amazonaws.com/exercise-thumbnails/02771201-Decline-Crunch_Waist_thumbnail@3x.jpg",
               "thumbnail_url":"https://pump-app.s3.eu-west-2.amazonaws.com/exercise-thumbnails/02771201-Decline-Crunch_Waist_thumbnail@3x.jpg",
               "muscle_group":"abdominals",
               "other_muscles":[
                  
               ],
               "priority":9,
               "sets":[
                  {
                     "id":310860060,
                     "index":0,
                     "indicator":"normal",
                     "weight_kg":null,
                     "reps":8,
                     "distance_meters":null,
                     "duration_seconds":null,
                     "rpe":null,
                     "prs":[
                        
                     ],
                     "personalRecords":[
                        
                     ]
                  },
                  {
                     "id":310860061,
                     "index":1,
                     "indicator":"normal",
                     "weight_kg":null,
                     "reps":8,
                     "distance_meters":null,
                     "duration_seconds":null,
                     "rpe":null,
                     "prs":[
                        
                     ],
                     "personalRecords":[
                        
                     ]
                  },
                  {
                     "id":310860062,
                     "index":2,
                     "indicator":"normal",
                     "weight_kg":null,
                     "reps":8,
                     "distance_meters":null,
                     "duration_seconds":null,
                     "rpe":null,
                     "prs":[
                        
                     ],
                     "personalRecords":[
                        
                     ]
                  },
                  {
                     "id":310860063,
                     "index":3,
                     "indicator":"normal",
                     "weight_kg":null,
                     "reps":8,
                     "distance_meters":null,
                     "duration_seconds":null,
                     "rpe":null,
                     "prs":[
                        
                     ],
                     "personalRecords":[
                        
                     ]
                  },
                  {
                     "id":310860064,
                     "index":4,
                     "indicator":"normal",
                     "weight_kg":null,
                     "reps":8,
                     "distance_meters":null,
                     "duration_seconds":null,
                     "rpe":null,
                     "prs":[
                        
                     ],
                     "personalRecords":[
                        
                     ]
                  }
               ]
            },
            {
               "id":"72222465-ff9f-41b2-b7b7-c178a21d8dd0",
               "title":"Rowing Machine",
               "es_title":"Máquina de Remo",
               "de_title":"Rudermaschine",
               "fr_title":"Rameur",
               "it_title":"Macchina Rematore",
               "pt_title":"Máquina De Remo",
               "ko_title":null,
               "ja_title":null,
               "tr_title":"Kürek Çekme",
               "ru_title":"Гребной тренажер",
               "zh_cn_title":"划船机",
               "zh_tw_title":"划船機",
               "superset_id":null,
               "rest_seconds":120,
               "notes":"",
               "exercise_template_id":"0222DB42",
               "url":"https://pump-app.s3.eu-west-2.amazonaws.com/exercise-assets/22701201-Rowing-Straight-Back-(with-rowing-machine)-(female)_Cardio.mp4",
               "exercise_type":"distance_duration",
               "equipment_category":"machine",
               "media_type":"video",
               "custom_exercise_image_url":null,
               "custom_exercise_image_thumbnail_url":"https://pump-app.s3.eu-west-2.amazonaws.com/exercise-thumbnails/22701201-Rowing-Straight-Back-(with-rowing-machine)-(female)_Cardio_thumbnail@3x.jpg",
               "thumbnail_url":"https://pump-app.s3.eu-west-2.amazonaws.com/exercise-thumbnails/22701201-Rowing-Straight-Back-(with-rowing-machine)-(female)_Cardio_thumbnail@3x.jpg",
               "muscle_group":"cardio",
               "other_muscles":[
                  
               ],
               "priority":8,
               "sets":[
                  {
                     "id":310860065,
                     "index":0,
                     "indicator":"normal",
                     "weight_kg":null,
                     "reps":null,
                     "distance_meters":0,
                     "duration_seconds":2,
                     "rpe":null,
                     "prs":[
                        
                     ],
                     "personalRecords":[
                        
                     ]
                  },
                  {
                     "id":310860066,
                     "index":1,
                     "indicator":"normal",
                     "weight_kg":null,
                     "reps":null,
                     "distance_meters":0,
                     "duration_seconds":2,
                     "rpe":null,
                     "prs":[
                        
                     ],
                     "personalRecords":[
                        
                     ]
                  },
                  {
                     "id":310860067,
                     "index":2,
                     "indicator":"normal",
                     "weight_kg":null,
                     "reps":null,
                     "distance_meters":0,
                     "duration_seconds":2,
                     "rpe":null,
                     "prs":[
                        
                     ],
                     "personalRecords":[
                        
                     ]
                  },
                  {
                     "id":310860068,
                     "index":3,
                     "indicator":"normal",
                     "weight_kg":null,
                     "reps":null,
                     "distance_meters":0,
                     "duration_seconds":2,
                     "rpe":null,
                     "prs":[
                        
                     ],
                     "personalRecords":[
                        
                     ]
                  },
                  {
                     "id":310860069,
                     "index":4,
                     "indicator":"normal",
                     "weight_kg":null,
                     "reps":null,
                     "distance_meters":0,
                     "duration_seconds":2,
                     "rpe":null,
                     "prs":[
                        
                     ],
                     "personalRecords":[
                        
                     ]
                  },
                  {
                     "id":310860070,
                     "index":5,
                     "indicator":"normal",
                     "weight_kg":null,
                     "reps":null,
                     "distance_meters":0,
                     "duration_seconds":2,
                     "rpe":null,
                     "prs":[
                        
                     ],
                     "personalRecords":[
                        
                     ]
                  }
               ]
            },
            {
               "id":"733d62b9-b97a-4753-a812-1d5147c4f4a0",
               "title":"Ab Wheel",
               "es_title":"Rueda Abdominal",
               "de_title":"Ab Wheel",
               "fr_title":"Roue Abdominale",
               "it_title":"Ruota Addominali",
               "pt_title":"Roda Abdominal ",
               "ko_title":null,
               "ja_title":null,
               "tr_title":"Ab Wheel",
               "ru_title":"Колесо для пресса",
               "zh_cn_title":"健腹轮",
               "zh_tw_title":"健腹輪",
               "superset_id":null,
               "rest_seconds":120,
               "notes":"",
               "exercise_template_id":"99D5F10E",
               "url":"https://pump-app.s3.eu-west-2.amazonaws.com/exercise-assets/08571201-Wheel-Rollout_Waist.mp4",
               "exercise_type":"reps_only",
               "equipment_category":"other",
               "media_type":"video",
               "custom_exercise_image_url":null,
               "custom_exercise_image_thumbnail_url":"https://pump-app.s3.eu-west-2.amazonaws.com/exercise-thumbnails/08571201-Wheel-Rollout_Waist_thumbnail@3x.jpg",
               "thumbnail_url":"https://pump-app.s3.eu-west-2.amazonaws.com/exercise-thumbnails/08571201-Wheel-Rollout_Waist_thumbnail@3x.jpg",
               "muscle_group":"abdominals",
               "other_muscles":[
                  
               ],
               "priority":0,
               "sets":[
                  {
                     "id":310860071,
                     "index":0,
                     "indicator":"normal",
                     "weight_kg":null,
                     "reps":8,
                     "distance_meters":null,
                     "duration_seconds":null,
                     "rpe":null,
                     "prs":[
                        
                     ],
                     "personalRecords":[
                        
                     ]
                  },
                  {
                     "id":310860072,
                     "index":1,
                     "indicator":"normal",
                     "weight_kg":null,
                     "reps":8,
                     "distance_meters":null,
                     "duration_seconds":null,
                     "rpe":null,
                     "prs":[
                        
                     ],
                     "personalRecords":[
                        
                     ]
                  },
                  {
                     "id":310860073,
                     "index":2,
                     "indicator":"normal",
                     "weight_kg":null,
                     "reps":8,
                     "distance_meters":null,
                     "duration_seconds":null,
                     "rpe":null,
                     "prs":[
                        
                     ],
                     "personalRecords":[
                        
                     ]
                  },
                  {
                     "id":310860074,
                     "index":3,
                     "indicator":"normal",
                     "weight_kg":null,
                     "reps":8,
                     "distance_meters":null,
                     "duration_seconds":null,
                     "rpe":null,
                     "prs":[
                        
                     ],
                     "personalRecords":[
                        
                     ]
                  },
                  {
                     "id":310860075,
                     "index":4,
                     "indicator":"normal",
                     "weight_kg":null,
                     "reps":8,
                     "distance_meters":null,
                     "duration_seconds":null,
                     "rpe":null,
                     "prs":[
                        
                     ],
                     "personalRecords":[
                        
                     ]
                  }
               ]
            },
            {
               "id":"d5ef43f8-730e-494e-afbc-b5e65b237edc",
               "title":"Plank",
               "es_title":"Plancha",
               "de_title":"Plank",
               "fr_title":"Planche",
               "it_title":"Plank",
               "pt_title":"Prancha Abdominal",
               "ko_title":null,
               "ja_title":null,
               "tr_title":"Plank",
               "ru_title":"Планка",
               "zh_cn_title":"棒式",
               "zh_tw_title":"棒式",
               "superset_id":null,
               "rest_seconds":120,
               "notes":"",
               "exercise_template_id":"C6C9B8A0",
               "url":"https://pump-app.s3.eu-west-2.amazonaws.com/exercise-assets/04631201-Front-Plank-m_waist.mp4",
               "exercise_type":"duration",
               "equipment_category":"none",
               "media_type":"video",
               "custom_exercise_image_url":null,
               "custom_exercise_image_thumbnail_url":"https://pump-app.s3.eu-west-2.amazonaws.com/exercise-thumbnails/04631201-Front-Plank-m_waist_thumbnail@3x.jpg",
               "thumbnail_url":"https://pump-app.s3.eu-west-2.amazonaws.com/exercise-thumbnails/04631201-Front-Plank-m_waist_thumbnail@3x.jpg",
               "muscle_group":"abdominals",
               "other_muscles":[
                  
               ],
               "priority":0,
               "sets":[
                  {
                     "id":310860076,
                     "index":0,
                     "indicator":"normal",
                     "weight_kg":null,
                     "reps":null,
                     "distance_meters":null,
                     "duration_seconds":2,
                     "rpe":null,
                     "prs":[
                        
                     ],
                     "personalRecords":[
                        
                     ]
                  },
                  {
                     "id":310860077,
                     "index":1,
                     "indicator":"normal",
                     "weight_kg":null,
                     "reps":null,
                     "distance_meters":null,
                     "duration_seconds":2,
                     "rpe":null,
                     "prs":[
                        
                     ],
                     "personalRecords":[
                        
                     ]
                  },
                  {
                     "id":310860078,
                     "index":2,
                     "indicator":"normal",
                     "weight_kg":null,
                     "reps":null,
                     "distance_meters":null,
                     "duration_seconds":2,
                     "rpe":null,
                     "prs":[
                        
                     ],
                     "personalRecords":[
                        
                     ]
                  },
                  {
                     "id":310860079,
                     "index":3,
                     "indicator":"normal",
                     "weight_kg":null,
                     "reps":null,
                     "distance_meters":null,
                     "duration_seconds":2,
                     "rpe":null,
                     "prs":[
                        
                     ],
                     "personalRecords":[
                        
                     ]
                  }
               ]
            },
            {
               "id":"927cbb1f-def5-41c1-bef9-4840bded0ac0",
               "title":"Side Plank",
               "es_title":"Plancha Lateral",
               "de_title":"Seitlicher Plank",
               "fr_title":"Planche Latérale",
               "it_title":"Plank Laterale",
               "pt_title":"Prancha Lateral",
               "ko_title":null,
               "ja_title":null,
               "tr_title":"Side Plank",
               "ru_title":"Боковая планка",
               "zh_cn_title":"侧棒式",
               "zh_tw_title":"側棒式",
               "superset_id":null,
               "rest_seconds":120,
               "notes":"",
               "exercise_template_id":"E3EDA509",
               "url":"https://pump-app.s3.eu-west-2.amazonaws.com/exercise-assets/07151201-Side-Plank-m_Waist.mp4",
               "exercise_type":"duration",
               "equipment_category":"none",
               "media_type":"video",
               "custom_exercise_image_url":null,
               "custom_exercise_image_thumbnail_url":"https://pump-app.s3.eu-west-2.amazonaws.com/exercise-thumbnails/07151201-Side-Plank-m_Waist_thumbnail@3x.jpg",
               "thumbnail_url":"https://pump-app.s3.eu-west-2.amazonaws.com/exercise-thumbnails/07151201-Side-Plank-m_Waist_thumbnail@3x.jpg",
               "muscle_group":"abdominals",
               "other_muscles":[
                  
               ],
               "priority":0,
               "sets":[
                  {
                     "id":310860080,
                     "index":0,
                     "indicator":"normal",
                     "weight_kg":null,
                     "reps":null,
                     "distance_meters":null,
                     "duration_seconds":2,
                     "rpe":null,
                     "prs":[
                        
                     ],
                     "personalRecords":[
                        
                     ]
                  },
                  {
                     "id":310860081,
                     "index":1,
                     "indicator":"normal",
                     "weight_kg":null,
                     "reps":null,
                     "distance_meters":null,
                     "duration_seconds":2,
                     "rpe":null,
                     "prs":[
                        
                     ],
                     "personalRecords":[
                        
                     ]
                  },
                  {
                     "id":310860082,
                     "index":2,
                     "indicator":"normal",
                     "weight_kg":null,
                     "reps":null,
                     "distance_meters":null,
                     "duration_seconds":2,
                     "rpe":null,
                     "prs":[
                        
                     ],
                     "personalRecords":[
                        
                     ]
                  },
                  {
                     "id":310860083,
                     "index":3,
                     "indicator":"normal",
                     "weight_kg":null,
                     "reps":null,
                     "distance_meters":null,
                     "duration_seconds":2,
                     "rpe":null,
                     "prs":[
                        
                     ],
                     "personalRecords":[
                        
                     ]
                  }
               ]
            },
            {
               "id":"d6feaefe-916d-4b7b-9015-f58ff0551510",
               "title":"Sit Up",
               "es_title":"Sit Up",
               "de_title":"Rumpfbeugen",
               "fr_title":"Sit Up",
               "it_title":"Sit Up",
               "pt_title":"Abdominal Tradicional",
               "ko_title":null,
               "ja_title":null,
               "tr_title":"Mekik",
               "ru_title":"Приседания",
               "zh_cn_title":"仰卧起坐",
               "zh_tw_title":"仰臥起坐",
               "superset_id":null,
               "rest_seconds":120,
               "notes":"",
               "exercise_template_id":"022DF610",
               "url":"https://pump-app.s3.eu-west-2.amazonaws.com/exercise-assets/00011201-3-4-Sit-up_Waist.mp4",
               "exercise_type":"reps_only",
               "equipment_category":"none",
               "media_type":"video",
               "custom_exercise_image_url":null,
               "custom_exercise_image_thumbnail_url":"https://pump-app.s3.eu-west-2.amazonaws.com/exercise-thumbnails/00011201-3-4-Sit-up_Waist_thumbnail@3x.jpg",
               "thumbnail_url":"https://pump-app.s3.eu-west-2.amazonaws.com/exercise-thumbnails/00011201-3-4-Sit-up_Waist_thumbnail@3x.jpg",
               "muscle_group":"abdominals",
               "other_muscles":[
                  
               ],
               "priority":10,
               "sets":[
                  {
                     "id":310860084,
                     "index":0,
                     "indicator":"normal",
                     "weight_kg":null,
                     "reps":20,
                     "distance_meters":null,
                     "duration_seconds":null,
                     "rpe":null,
                     "prs":[
                        
                     ],
                     "personalRecords":[
                        
                     ]
                  },
                  {
                     "id":310860085,
                     "index":1,
                     "indicator":"normal",
                     "weight_kg":null,
                     "reps":10,
                     "distance_meters":null,
                     "duration_seconds":null,
                     "rpe":null,
                     "prs":[
                        
                     ],
                     "personalRecords":[
                        
                     ]
                  },
                  {
                     "id":310860086,
                     "index":2,
                     "indicator":"normal",
                     "weight_kg":null,
                     "reps":10,
                     "distance_meters":null,
                     "duration_seconds":null,
                     "rpe":null,
                     "prs":[
                        
                     ],
                     "personalRecords":[
                        
                     ]
                  },
                  {
                     "id":310860087,
                     "index":3,
                     "indicator":"normal",
                     "weight_kg":null,
                     "reps":10,
                     "distance_meters":null,
                     "duration_seconds":null,
                     "rpe":null,
                     "prs":[
                        
                     ],
                     "personalRecords":[
                        
                     ]
                  }
               ]
            },
            {
               "id":"4a0362a2-f516-42f7-b1d4-a61a14a331f7",
               "title":"Overhead Press (Barbell)",
               "es_title":"Press de Hombros (Barra)",
               "de_title":"Schulterdrücken (Langhantel)",
               "fr_title":"Développé Militaire (Barre)",
               "it_title":"Lento in Avanti (Bilanciere)",
               "pt_title":"Desenvolvimento (Barra)",
               "ko_title":null,
               "ja_title":null,
               "tr_title":"Overhead Press (Bar)",
               "ru_title":"Жим над головой (Штанга)",
               "zh_cn_title":"肩推 (杠铃）",
               "zh_tw_title":"肩推 (槓鈴）",
               "superset_id":null,
               "rest_seconds":60,
               "notes":"",
               "exercise_template_id":"7B8D84E8",
               "url":"https://pump-app.s3.eu-west-2.amazonaws.com/exercise-assets/11651201-Barbell-Standing-Military-Press-(without-rack)_Shoulders.mp4",
               "exercise_type":"weight_reps",
               "equipment_category":"barbell",
               "media_type":"video",
               "custom_exercise_image_url":null,
               "custom_exercise_image_thumbnail_url":"https://pump-app.s3.eu-west-2.amazonaws.com/exercise-thumbnails/11651201-Barbell-Standing-Military-Press-(without-rack)_Shoulders_thumbnail@3x.jpg",
               "thumbnail_url":"https://pump-app.s3.eu-west-2.amazonaws.com/exercise-thumbnails/11651201-Barbell-Standing-Military-Press-(without-rack)_Shoulders_thumbnail@3x.jpg",
               "muscle_group":"shoulders",
               "other_muscles":[
                  "triceps"
               ],
               "priority":10,
               "sets":[
                  {
                     "id":310860088,
                     "index":0,
                     "indicator":"normal",
                     "weight_kg":40,
                     "reps":1,
                     "distance_meters":null,
                     "duration_seconds":null,
                     "rpe":null,
                     "prs":[
                        
                     ],
                     "personalRecords":[
                        
                     ]
                  },
                  {
                     "id":310860089,
                     "index":1,
                     "indicator":"normal",
                     "weight_kg":40,
                     "reps":3,
                     "distance_meters":null,
                     "duration_seconds":null,
                     "rpe":null,
                     "prs":[
                        
                     ],
                     "personalRecords":[
                        
                     ]
                  },
                  {
                     "id":310860090,
                     "index":2,
                     "indicator":"normal",
                     "weight_kg":0,
                     "reps":1,
                     "distance_meters":null,
                     "duration_seconds":null,
                     "rpe":null,
                     "prs":[
                        
                     ],
                     "personalRecords":[
                        
                     ]
                  }
               ]
            }
         ],
         "estimated_volume_kg":160
      },
      {
         "id":"3d08434a-4bf6-4225-a6c9-a27f91548aef",
         "short_id":"1dy6oVgjf9a",
         "index":13414706,
         "name":"3. Chest / Upper Back",
         "description":"",
         "start_time":1678783435,
         "end_time":1678790745,
         "created_at":"2023-03-14T10:46:39.475Z",
         "updated_at":"2023-03-14T10:46:39.475Z",
         "routine_id":"5f02e2a3-ce97-4576-bfc8-4ca9e1ea4868",
         "apple_watch":false,
         "user_id":"93620a45-5bef-4a70-baab-5c1058a88046",
         "username":"bitwiseshift",
         "profile_image":"https://pump-app.s3.eu-west-2.amazonaws.com/profile-images/bitwiseshift-e4a12928-f0f3-4a87-adc5-99c1daae5951.jpg",
         "verified":false,
         "nth_workout":180,
         "like_count":0,
         "is_liked_by_user":false,
         "like_images":[
            
         ],
         "comments":[
            
         ],
         "comment_count":0,
         "media":[
            
         ],
         "image_urls":[
            
         ],
         "exercises":[
            {
               "id":"5c658ffd-828f-4e4c-924f-f3e320fc0a80",
               "title":"Elliptical Trainer",
               "es_title":"Entrenador Elíptico",
               "de_title":"Crosstrainer",
               "fr_title":"Vélo Elliptique",
               "it_title":"Ellittica",
               "pt_title":"Elíptico",
               "ko_title":null,
               "ja_title":null,
               "tr_title":"Eliptik Bisiklet",
               "ru_title":"Эллиптический тренажер",
               "zh_cn_title":"椭圆机",
               "zh_tw_title":"橢圓機",
               "superset_id":null,
               "rest_seconds":120,
               "notes":"",
               "exercise_template_id":"3303376C",
               "url":"https://pump-app.s3.eu-west-2.amazonaws.com/exercise-assets/21921201-Elliptical-Machine-Walk_Cardio.mp4",
               "exercise_type":"distance_duration",
               "equipment_category":"machine",
               "media_type":"video",
               "custom_exercise_image_url":null,
               "custom_exercise_image_thumbnail_url":"https://pump-app.s3.eu-west-2.amazonaws.com/exercise-thumbnails/21921201-Elliptical-Machine-Walk_Cardio_thumbnail@3x.jpg",
               "thumbnail_url":"https://pump-app.s3.eu-west-2.amazonaws.com/exercise-thumbnails/21921201-Elliptical-Machine-Walk_Cardio_thumbnail@3x.jpg",
               "muscle_group":"cardio",
               "other_muscles":[
                  
               ],
               "priority":8,
               "sets":[
                  {
                     "id":309117293,
                     "index":0,
                     "indicator":"normal",
                     "weight_kg":null,
                     "reps":null,
                     "distance_meters":0,
                     "duration_seconds":15,
                     "rpe":null,
                     "prs":[
                        
                     ],
                     "personalRecords":[
                        
                     ]
                  }
               ]
            },
            {
               "id":"5c8f1ca1-5575-4f7b-b734-82c9e9c9b184",
               "title":"Bench Press (Barbell)",
               "es_title":"Press de Banca (Barra)",
               "de_title":"Bankdrücken (Langhantel)",
               "fr_title":"Développé Couché (Barre)",
               "it_title":"Panca Piana (Bilanciere)",
               "pt_title":"Supino (Barra)",
               "ko_title":null,
               "ja_title":null,
               "tr_title":"Bench Press (Bar)",
               "ru_title":"Жим лежа (Штанга)",
               "zh_cn_title":"卧推 （杠铃）",
               "zh_tw_title":"平板臥推 （槓鈴）",
               "superset_id":null,
               "rest_seconds":120,
               "notes":"",
               "exercise_template_id":"79D0BB3A",
               "url":"https://pump-app.s3.eu-west-2.amazonaws.com/exercise-assets/00251201-Barbell-Bench-Press_Chest.mp4",
               "exercise_type":"weight_reps",
               "equipment_category":"barbell",
               "media_type":"video",
               "custom_exercise_image_url":null,
               "custom_exercise_image_thumbnail_url":"https://pump-app.s3.eu-west-2.amazonaws.com/exercise-thumbnails/00251201-Barbell-Bench-Press_Chest_thumbnail@3x.jpg",
               "thumbnail_url":"https://pump-app.s3.eu-west-2.amazonaws.com/exercise-thumbnails/00251201-Barbell-Bench-Press_Chest_thumbnail@3x.jpg",
               "muscle_group":"chest",
               "other_muscles":[
                  "triceps",
                  "shoulders"
               ],
               "priority":10,
               "sets":[
                  {
                     "id":309117294,
                     "index":0,
                     "indicator":"normal",
                     "weight_kg":60,
                     "reps":4,
                     "distance_meters":null,
                     "duration_seconds":null,
                     "rpe":null,
                     "prs":[
                        
                     ],
                     "personalRecords":[
                        
                     ]
                  },
                  {
                     "id":309117295,
                     "index":1,
                     "indicator":"normal",
                     "weight_kg":55,
                     "reps":8,
                     "distance_meters":null,
                     "duration_seconds":null,
                     "rpe":null,
                     "prs":[
                        
                     ],
                     "personalRecords":[
                        
                     ]
                  },
                  {
                     "id":309117296,
                     "index":2,
                     "indicator":"normal",
                     "weight_kg":55,
                     "reps":8,
                     "distance_meters":null,
                     "duration_seconds":null,
                     "rpe":null,
                     "prs":[
                        
                     ],
                     "personalRecords":[
                        
                     ]
                  },
                  {
                     "id":309117297,
                     "index":3,
                     "indicator":"normal",
                     "weight_kg":52.5,
                     "reps":8,
                     "distance_meters":null,
                     "duration_seconds":null,
                     "rpe":null,
                     "prs":[
                        
                     ],
                     "personalRecords":[
                        
                     ]
                  },
                  {
                     "id":309117298,
                     "index":4,
                     "indicator":"normal",
                     "weight_kg":50,
                     "reps":8,
                     "distance_meters":null,
                     "duration_seconds":null,
                     "rpe":null,
                     "prs":[
                        
                     ],
                     "personalRecords":[
                        
                     ]
                  },
                  {
                     "id":309117299,
                     "index":5,
                     "indicator":"normal",
                     "weight_kg":50,
                     "reps":8,
                     "distance_meters":null,
                     "duration_seconds":null,
                     "rpe":null,
                     "prs":[
                        
                     ],
                     "personalRecords":[
                        
                     ]
                  },
                  {
                     "id":309117300,
                     "index":6,
                     "indicator":"normal",
                     "weight_kg":60,
                     "reps":4,
                     "distance_meters":null,
                     "duration_seconds":null,
                     "rpe":null,
                     "prs":[
                        
                     ],
                     "personalRecords":[
                        
                     ]
                  }
               ]
            },
            {
               "id":"e5e4986f-4bbc-4572-94b7-c6eb42bd76c8",
               "title":"Chest Fly (Dumbbell)",
               "es_title":"Aperturas (Mancuerna)",
               "de_title":"Fliegende (Kurzhantel)",
               "fr_title":"Écarté (Haltère)",
               "it_title":"Croci (Manubrio)",
               "pt_title":"Crucifixo Reto (Halter)",
               "ko_title":null,
               "ja_title":null,
               "tr_title":"Chest Fly (Dambıl)",
               "ru_title":"Разводка (Гантель)",
               "zh_cn_title":"飞鸟夹胸（哑铃）",
               "zh_tw_title":"飛鳥夾胸（啞鈴）",
               "superset_id":null,
               "rest_seconds":120,
               "notes":"",
               "exercise_template_id":"12017185",
               "url":"https://pump-app.s3.eu-west-2.amazonaws.com/exercise-assets/03081201-Dumbbell-Fly_Chest.mp4",
               "exercise_type":"weight_reps",
               "equipment_category":"dumbbell",
               "media_type":"video",
               "custom_exercise_image_url":null,
               "custom_exercise_image_thumbnail_url":"https://pump-app.s3.eu-west-2.amazonaws.com/exercise-thumbnails/03081201-Dumbbell-Fly_Chest_thumbnail@3x.jpg",
               "thumbnail_url":"https://pump-app.s3.eu-west-2.amazonaws.com/exercise-thumbnails/03081201-Dumbbell-Fly_Chest_thumbnail@3x.jpg",
               "muscle_group":"chest",
               "other_muscles":[
                  
               ],
               "priority":8,
               "sets":[
                  {
                     "id":309117301,
                     "index":0,
                     "indicator":"normal",
                     "weight_kg":25,
                     "reps":8,
                     "distance_meters":null,
                     "duration_seconds":null,
                     "rpe":null,
                     "prs":[
                        
                     ],
                     "personalRecords":[
                        
                     ]
                  },
                  {
                     "id":309117302,
                     "index":1,
                     "indicator":"normal",
                     "weight_kg":30,
                     "reps":8,
                     "distance_meters":null,
                     "duration_seconds":null,
                     "rpe":null,
                     "prs":[
                        
                     ],
                     "personalRecords":[
                        
                     ]
                  },
                  {
                     "id":309117303,
                     "index":2,
                     "indicator":"normal",
                     "weight_kg":35,
                     "reps":8,
                     "distance_meters":null,
                     "duration_seconds":null,
                     "rpe":null,
                     "prs":[
                        
                     ],
                     "personalRecords":[
                        
                     ]
                  },
                  {
                     "id":309117304,
                     "index":3,
                     "indicator":"normal",
                     "weight_kg":40,
                     "reps":4,
                     "distance_meters":null,
                     "duration_seconds":null,
                     "rpe":null,
                     "prs":[
                        
                     ],
                     "personalRecords":[
                        
                     ]
                  },
                  {
                     "id":309117305,
                     "index":4,
                     "indicator":"normal",
                     "weight_kg":30,
                     "reps":8,
                     "distance_meters":null,
                     "duration_seconds":null,
                     "rpe":null,
                     "prs":[
                        
                     ],
                     "personalRecords":[
                        
                     ]
                  }
               ]
            },
            {
               "id":"663bd3fd-b839-4c32-8f8e-1db961589abd",
               "title":"T Bar Row",
               "es_title":"Remo en Punta",
               "de_title":"T-Bar Rudern",
               "fr_title":"Rowing Barre T",
               "it_title":"Rematore T Bar",
               "pt_title":"Remada na Barra T",
               "ko_title":null,
               "ja_title":null,
               "tr_title":"T Bar Row",
               "ru_title":"Тяга Т грифа",
               "zh_cn_title":"T杠划船",
               "zh_tw_title":"T槓划船",
               "superset_id":null,
               "rest_seconds":120,
               "notes":"",
               "exercise_template_id":"08A2974E",
               "url":"https://pump-app.s3.eu-west-2.amazonaws.com/exercise-assets/06061201-Lever-T-bar-Row-(plate-loaded)_Back.mp4",
               "exercise_type":"weight_reps",
               "equipment_category":"barbell",
               "media_type":"video",
               "custom_exercise_image_url":null,
               "custom_exercise_image_thumbnail_url":"https://pump-app.s3.eu-west-2.amazonaws.com/exercise-thumbnails/06061201-Lever-T-bar-Row-(plate-loaded)_Back_thumbnail@3x.jpg",
               "thumbnail_url":"https://pump-app.s3.eu-west-2.amazonaws.com/exercise-thumbnails/06061201-Lever-T-bar-Row-(plate-loaded)_Back_thumbnail@3x.jpg",
               "muscle_group":"upper_back",
               "other_muscles":[
                  
               ],
               "priority":0,
               "sets":[
                  {
                     "id":309117306,
                     "index":0,
                     "indicator":"normal",
                     "weight_kg":20,
                     "reps":8,
                     "distance_meters":null,
                     "duration_seconds":null,
                     "rpe":null,
                     "prs":[
                        
                     ],
                     "personalRecords":[
                        
                     ]
                  },
                  {
                     "id":309117307,
                     "index":1,
                     "indicator":"normal",
                     "weight_kg":25,
                     "reps":8,
                     "distance_meters":null,
                     "duration_seconds":null,
                     "rpe":null,
                     "prs":[
                        
                     ],
                     "personalRecords":[
                        
                     ]
                  },
                  {
                     "id":309117308,
                     "index":2,
                     "indicator":"normal",
                     "weight_kg":32.5,
                     "reps":8,
                     "distance_meters":null,
                     "duration_seconds":null,
                     "rpe":null,
                     "prs":[
                        
                     ],
                     "personalRecords":[
                        
                     ]
                  },
                  {
                     "id":309117309,
                     "index":3,
                     "indicator":"normal",
                     "weight_kg":30,
                     "reps":4,
                     "distance_meters":null,
                     "duration_seconds":null,
                     "rpe":null,
                     "prs":[
                        
                     ],
                     "personalRecords":[
                        
                     ]
                  }
               ]
            },
            {
               "id":"ef9182ad-9834-44cc-bad3-8ec0e1d2742f",
               "title":"Lat Pulldown (Cable)",
               "es_title":"Jalón al Pecho (Cable)",
               "de_title":"Latzug (Kabel)",
               "fr_title":"Tirage Poitrine (Poulie)",
               "it_title":"Lat Pulldown (Cavo)",
               "pt_title":"Puxada Alta na Polia (Máquina)",
               "ko_title":null,
               "ja_title":null,
               "tr_title":"Lat Pulldown (Cable)",
               "ru_title":"Вкртикальная тяга Широчайшими (Блок)",
               "zh_cn_title":"阔背肌下拉 （滑轮机）",
               "zh_tw_title":"闊背肌下拉 （滑輪機）",
               "superset_id":null,
               "rest_seconds":120,
               "notes":"",
               "exercise_template_id":"6A6C31A5",
               "url":"https://pump-app.s3.eu-west-2.amazonaws.com/exercise-assets/01501201-Cable-Bar-Lateral-Pulldown_Back.mp4",
               "exercise_type":"weight_reps",
               "equipment_category":"machine",
               "media_type":"video",
               "custom_exercise_image_url":null,
               "custom_exercise_image_thumbnail_url":"https://pump-app.s3.eu-west-2.amazonaws.com/exercise-thumbnails/01501201-Cable-Bar-Lateral-Pulldown_Back_thumbnail@3x.jpg",
               "thumbnail_url":"https://pump-app.s3.eu-west-2.amazonaws.com/exercise-thumbnails/01501201-Cable-Bar-Lateral-Pulldown_Back_thumbnail@3x.jpg",
               "muscle_group":"lats",
               "other_muscles":[
                  
               ],
               "priority":10,
               "sets":[
                  {
                     "id":309117310,
                     "index":0,
                     "indicator":"normal",
                     "weight_kg":46,
                     "reps":8,
                     "distance_meters":null,
                     "duration_seconds":null,
                     "rpe":null,
                     "prs":[
                        
                     ],
                     "personalRecords":[
                        
                     ]
                  },
                  {
                     "id":309117311,
                     "index":1,
                     "indicator":"normal",
                     "weight_kg":59,
                     "reps":8,
                     "distance_meters":null,
                     "duration_seconds":null,
                     "rpe":null,
                     "prs":[
                        
                     ],
                     "personalRecords":[
                        
                     ]
                  },
                  {
                     "id":309117312,
                     "index":2,
                     "indicator":"normal",
                     "weight_kg":64,
                     "reps":8,
                     "distance_meters":null,
                     "duration_seconds":null,
                     "rpe":null,
                     "prs":[
                        
                     ],
                     "personalRecords":[
                        
                     ]
                  },
                  {
                     "id":309117313,
                     "index":3,
                     "indicator":"normal",
                     "weight_kg":59,
                     "reps":6,
                     "distance_meters":null,
                     "duration_seconds":null,
                     "rpe":null,
                     "prs":[
                        
                     ],
                     "personalRecords":[
                        
                     ]
                  }
               ]
            },
            {
               "id":"47190c24-1cb2-47f6-9c35-eb7ebe253d51",
               "title":"Seated Cable Row",
               "es_title":"Remo Sentado con Cable",
               "de_title":"Rudern am Kabel sitzend",
               "fr_title":"Rowing Poulie Assis",
               "it_title":"Rematore al Cavo da Seduto",
               "pt_title":"Remada (Corda) Sentado",
               "ko_title":null,
               "ja_title":null,
               "tr_title":"Oturarak Cable Row",
               "ru_title":"Горизонтальная тяга блока",
               "zh_cn_title":"坐式滑轮划船",
               "zh_tw_title":"坐式滑輪划船",
               "superset_id":null,
               "rest_seconds":90,
               "notes":"",
               "exercise_template_id":"F1D60854",
               "url":"https://pump-app.s3.eu-west-2.amazonaws.com/exercise-assets/01801201-Cable-Low-Seated-Row_Back.mp4",
               "exercise_type":"weight_reps",
               "equipment_category":"machine",
               "media_type":"video",
               "custom_exercise_image_url":null,
               "custom_exercise_image_thumbnail_url":"https://pump-app.s3.eu-west-2.amazonaws.com/exercise-thumbnails/01801201-Cable-Low-Seated-Row_Back_thumbnail@3x.jpg",
               "thumbnail_url":"https://pump-app.s3.eu-west-2.amazonaws.com/exercise-thumbnails/01801201-Cable-Low-Seated-Row_Back_thumbnail@3x.jpg",
               "muscle_group":"upper_back",
               "other_muscles":[
                  
               ],
               "priority":10,
               "sets":[
                  {
                     "id":309117314,
                     "index":0,
                     "indicator":"normal",
                     "weight_kg":91,
                     "reps":8,
                     "distance_meters":null,
                     "duration_seconds":null,
                     "rpe":null,
                     "prs":[
                        
                     ],
                     "personalRecords":[
                        
                     ]
                  },
                  {
                     "id":309117315,
                     "index":1,
                     "indicator":"normal",
                     "weight_kg":64,
                     "reps":8,
                     "distance_meters":null,
                     "duration_seconds":null,
                     "rpe":null,
                     "prs":[
                        
                     ],
                     "personalRecords":[
                        
                     ]
                  },
                  {
                     "id":309117316,
                     "index":2,
                     "indicator":"normal",
                     "weight_kg":64,
                     "reps":8,
                     "distance_meters":null,
                     "duration_seconds":null,
                     "rpe":null,
                     "prs":[
                        
                     ],
                     "personalRecords":[
                        
                     ]
                  },
                  {
                     "id":309117317,
                     "index":3,
                     "indicator":"normal",
                     "weight_kg":64,
                     "reps":8,
                     "distance_meters":null,
                     "duration_seconds":null,
                     "rpe":null,
                     "prs":[
                        
                     ],
                     "personalRecords":[
                        
                     ]
                  },
                  {
                     "id":309117318,
                     "index":4,
                     "indicator":"normal",
                     "weight_kg":64,
                     "reps":8,
                     "distance_meters":null,
                     "duration_seconds":null,
                     "rpe":null,
                     "prs":[
                        
                     ],
                     "personalRecords":[
                        
                     ]
                  },
                  {
                     "id":309117319,
                     "index":5,
                     "indicator":"normal",
                     "weight_kg":59,
                     "reps":8,
                     "distance_meters":null,
                     "duration_seconds":null,
                     "rpe":null,
                     "prs":[
                        
                     ],
                     "personalRecords":[
                        
                     ]
                  },
                  {
                     "id":309117320,
                     "index":6,
                     "indicator":"normal",
                     "weight_kg":59,
                     "reps":8,
                     "distance_meters":null,
                     "duration_seconds":null,
                     "rpe":null,
                     "prs":[
                        
                     ],
                     "personalRecords":[
                        
                     ]
                  },
                  {
                     "id":309117321,
                     "index":7,
                     "indicator":"normal",
                     "weight_kg":59,
                     "reps":8,
                     "distance_meters":null,
                     "duration_seconds":null,
                     "rpe":null,
                     "prs":[
                        
                     ],
                     "personalRecords":[
                        
                     ]
                  },
                  {
                     "id":309117322,
                     "index":8,
                     "indicator":"normal",
                     "weight_kg":59,
                     "reps":8,
                     "distance_meters":null,
                     "duration_seconds":null,
                     "rpe":null,
                     "prs":[
                        
                     ],
                     "personalRecords":[
                        
                     ]
                  },
                  {
                     "id":309117323,
                     "index":9,
                     "indicator":"normal",
                     "weight_kg":59,
                     "reps":8,
                     "distance_meters":null,
                     "duration_seconds":null,
                     "rpe":null,
                     "prs":[
                        
                     ],
                     "personalRecords":[
                        
                     ]
                  },
                  {
                     "id":309117324,
                     "index":10,
                     "indicator":"normal",
                     "weight_kg":59,
                     "reps":8,
                     "distance_meters":null,
                     "duration_seconds":null,
                     "rpe":null,
                     "prs":[
                        
                     ],
                     "personalRecords":[
                        
                     ]
                  }
               ]
            },
            {
               "id":"b4d22fcb-feea-4cc5-8d14-f33e145a84f7",
               "title":"Decline Crunch",
               "es_title":"Abdominal Corto en Banco Inclinado",
               "de_title":"Negativer Crunch",
               "fr_title":"Crunch Décliné",
               "it_title":"Crunch Declinato",
               "pt_title":"Abdominal Declinado",
               "ko_title":null,
               "ja_title":null,
               "tr_title":"Eğik Sehpada Yarım Mekik",
               "ru_title":"Скручивание в наклоне",
               "zh_cn_title":"斜板卷腹",
               "zh_tw_title":"斜板捲腹",
               "superset_id":null,
               "rest_seconds":60,
               "notes":"",
               "exercise_template_id":"BC10A922",
               "url":"https://pump-app.s3.eu-west-2.amazonaws.com/exercise-assets/02771201-Decline-Crunch_Waist.mp4",
               "exercise_type":"reps_only",
               "equipment_category":"none",
               "media_type":"video",
               "custom_exercise_image_url":null,
               "custom_exercise_image_thumbnail_url":"https://pump-app.s3.eu-west-2.amazonaws.com/exercise-thumbnails/02771201-Decline-Crunch_Waist_thumbnail@3x.jpg",
               "thumbnail_url":"https://pump-app.s3.eu-west-2.amazonaws.com/exercise-thumbnails/02771201-Decline-Crunch_Waist_thumbnail@3x.jpg",
               "muscle_group":"abdominals",
               "other_muscles":[
                  
               ],
               "priority":9,
               "sets":[
                  {
                     "id":309117325,
                     "index":0,
                     "indicator":"normal",
                     "weight_kg":null,
                     "reps":16,
                     "distance_meters":null,
                     "duration_seconds":null,
                     "rpe":null,
                     "prs":[
                        
                     ],
                     "personalRecords":[
                        
                     ]
                  },
                  {
                     "id":309117326,
                     "index":1,
                     "indicator":"normal",
                     "weight_kg":null,
                     "reps":8,
                     "distance_meters":null,
                     "duration_seconds":null,
                     "rpe":null,
                     "prs":[
                        
                     ],
                     "personalRecords":[
                        
                     ]
                  },
                  {
                     "id":309117327,
                     "index":2,
                     "indicator":"normal",
                     "weight_kg":null,
                     "reps":8,
                     "distance_meters":null,
                     "duration_seconds":null,
                     "rpe":null,
                     "prs":[
                        
                     ],
                     "personalRecords":[
                        
                     ]
                  }
               ]
            },
            {
               "id":"507345da-8c4e-4cef-8ea1-9a129928f53b",
               "title":"Lying Leg Raise",
               "es_title":"Levantamiento de Piernas Tumbado",
               "de_title":"Liegendes Beinheben",
               "fr_title":"Relevé de Jambes Allongé",
               "it_title":"Leg Raise Sdraiato",
               "pt_title":"Elevação De Pernas (Deitado)",
               "ko_title":null,
               "ja_title":null,
               "tr_title":"Çakı Hareketi",
               "ru_title":"Подъем ног лежа",
               "zh_cn_title":"躺式抬腿",
               "zh_tw_title":"躺式抬腿",
               "superset_id":null,
               "rest_seconds":120,
               "notes":"",
               "exercise_template_id":"09C9F635",
               "url":"https://pump-app.s3.eu-west-2.amazonaws.com/exercise-assets/11631201-Lying-Leg-Raise_Waist.mp4",
               "exercise_type":"reps_only",
               "equipment_category":"none",
               "media_type":"video",
               "custom_exercise_image_url":null,
               "custom_exercise_image_thumbnail_url":"https://pump-app.s3.eu-west-2.amazonaws.com/exercise-thumbnails/11631201-Lying-Leg-Raise_Waist_thumbnail@3x.jpg",
               "thumbnail_url":"https://pump-app.s3.eu-west-2.amazonaws.com/exercise-thumbnails/11631201-Lying-Leg-Raise_Waist_thumbnail@3x.jpg",
               "muscle_group":"abdominals",
               "other_muscles":[
                  
               ],
               "priority":8,
               "sets":[
                  {
                     "id":309117328,
                     "index":0,
                     "indicator":"normal",
                     "weight_kg":null,
                     "reps":8,
                     "distance_meters":null,
                     "duration_seconds":null,
                     "rpe":null,
                     "prs":[
                        
                     ],
                     "personalRecords":[
                        
                     ]
                  },
                  {
                     "id":309117329,
                     "index":1,
                     "indicator":"normal",
                     "weight_kg":null,
                     "reps":8,
                     "distance_meters":null,
                     "duration_seconds":null,
                     "rpe":null,
                     "prs":[
                        
                     ],
                     "personalRecords":[
                        
                     ]
                  },
                  {
                     "id":309117330,
                     "index":2,
                     "indicator":"normal",
                     "weight_kg":null,
                     "reps":8,
                     "distance_meters":null,
                     "duration_seconds":null,
                     "rpe":null,
                     "prs":[
                        
                     ],
                     "personalRecords":[
                        
                     ]
                  },
                  {
                     "id":309117331,
                     "index":3,
                     "indicator":"normal",
                     "weight_kg":null,
                     "reps":8,
                     "distance_meters":null,
                     "duration_seconds":null,
                     "rpe":null,
                     "prs":[
                        
                     ],
                     "personalRecords":[
                        
                     ]
                  }
               ]
            },
            {
               "id":"e3e03735-8dd4-4949-b1db-cc18267e3b4c",
               "title":"Hanging Leg Raise",
               "es_title":"Levantamiento de Piernas en Barra",
               "de_title":"Beinheben hängend",
               "fr_title":"Relevé de Jambes Suspendu",
               "it_title":"Leg Raise Appeso",
               "pt_title":"Elevação De Pernas Na Barra Fixa",
               "ko_title":null,
               "ja_title":null,
               "tr_title":"Hanging Leg Raise",
               "ru_title":"Подъем ног в висе",
               "zh_cn_title":"单杠曲腿上举",
               "zh_tw_title":"單槓曲腿上舉",
               "superset_id":null,
               "rest_seconds":120,
               "notes":"",
               "exercise_template_id":"F8356514",
               "url":"https://pump-app.s3.eu-west-2.amazonaws.com/exercise-assets/17641201-Hanging-Leg-Hip-Raise_Waist.mp4",
               "exercise_type":"reps_only",
               "equipment_category":"none",
               "media_type":"video",
               "custom_exercise_image_url":null,
               "custom_exercise_image_thumbnail_url":"https://pump-app.s3.eu-west-2.amazonaws.com/exercise-thumbnails/17641201-Hanging-Leg-Hip-Raise_Waist_thumbnail@3x.jpg",
               "thumbnail_url":"https://pump-app.s3.eu-west-2.amazonaws.com/exercise-thumbnails/17641201-Hanging-Leg-Hip-Raise_Waist_thumbnail@3x.jpg",
               "muscle_group":"abdominals",
               "other_muscles":[
                  
               ],
               "priority":0,
               "sets":[
                  {
                     "id":309117332,
                     "index":0,
                     "indicator":"normal",
                     "weight_kg":null,
                     "reps":8,
                     "distance_meters":null,
                     "duration_seconds":null,
                     "rpe":null,
                     "prs":[
                        
                     ],
                     "personalRecords":[
                        
                     ]
                  },
                  {
                     "id":309117333,
                     "index":1,
                     "indicator":"normal",
                     "weight_kg":null,
                     "reps":7,
                     "distance_meters":null,
                     "duration_seconds":null,
                     "rpe":null,
                     "prs":[
                        
                     ],
                     "personalRecords":[
                        
                     ]
                  },
                  {
                     "id":309117334,
                     "index":2,
                     "indicator":"normal",
                     "weight_kg":null,
                     "reps":6,
                     "distance_meters":null,
                     "duration_seconds":null,
                     "rpe":null,
                     "prs":[
                        
                     ],
                     "personalRecords":[
                        
                     ]
                  }
               ]
            }
         ],
         "estimated_volume_kg":11754
      }
   ]
}
```
# strong-api

## Welcome

- 1.login.py  - fairly self explanatory
- 2.workout-history.py - slightly larger exmaple, also saves workouts.json, used for the following examples
- 3.create-charts.py - uses workouts.json and matplotlib.pyplot to create charts found in graphs/
- 4.create-stats.py - takes workouts and simplifies the data 
- 5.chart.html - uses stats.json and chartjs to give and clean example of use in webpage.

## You will need to define these:

- export strong_device_uuid=$(uuidgen)
- export strong_application_id=$(date | sha1sum | awk '{print $1}')
- export strong_username="ddddddddddddddddd"
- export strong_password="gggggggggggggggggg"
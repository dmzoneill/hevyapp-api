import json

stats = {}

names = []
workout_exercises = {}
workout_time = {}
workout_volume = {}

wos = json.loads(open("workouts.json").read())

for X in wos:
    index = X["nth_workout"]
    name = X["name"]
    names.append(name.replace(" ", ""))
    workout_time[index] = round((X["end_time"] - X["start_time"]) / 60)
    workout_volume[index] = round(X["estimated_volume_kg"])

    for exercise in X["exercises"]:
        exercise_title = exercise["title"]

        if exercise_title not in workout_exercises.keys():
            workout_exercises[exercise_title] = {}

        volume = 0
        max = 0
        reps = 0

        for set in exercise["sets"]:
            if set["weight_kg"] is not None and set["reps"] is not None:
                volume += round(set["weight_kg"] * set["reps"])
            else:
                volume += 0

            reps += set["reps"] if set["reps"] is not None else 0

            if set["weight_kg"] is not None:
                max = set["weight_kg"] if set["weight_kg"] > max else max

        workout_exercises[exercise_title][index] = {}
        workout_exercises[exercise_title][index]["total_volume"] = round(volume)
        workout_exercises[exercise_title][index]["max_weight"] = max
        workout_exercises[exercise_title][index]["total_reps"] = reps


names.sort()

stats = {
    "workout_exercises": workout_exercises,
    "workout_time": workout_time,
    "workout_volume": workout_volume,
}

with open("stats.json", "w") as file1:
    file1.write(json.dumps(stats))
    file1.close()

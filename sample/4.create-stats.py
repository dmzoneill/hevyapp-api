import json

stats = {}

workouts = open("workouts.json").read()
workouts_obj = json.loads(workouts)
sessions_obj = workouts_obj["results"]

for session in sessions_obj:
    for exercise in session["parseSetGroups"]:

        name = exercise["parseExercise"]["name"]

        if name not in stats:
            stats[name] = {}

        date = exercise["createdAt"].split("T")[0]

        if name not in stats:
            stats[name] = {}

        if date not in stats[name]:
            stats[name][date] = {}
            stats[name][date]["total_volume"] = 0
            stats[name][date]["total_reps"] = 0
            stats[name][date]["max_weight"] = 0
            stats[name][date]["average_weight"] = 0
            average_count = 0
            average = 0

            for set in exercise["parseSetsDictionary"]:
                if set["isChecked"]:
                    if "kilograms" in set and set["kilograms"] != 0:
                        stats[name][date]["total_volume"] += set["reps"] * \
                            set["kilograms"]
                        stats[name][date]["total_reps"] += set["reps"]
                        stats[name][date]["max_weight"] = set["kilograms"] if set["kilograms"] > stats[
                            name][date]["max_weight"] else stats[name][date]["max_weight"]
                        average_count += set["reps"]
                        average += set["reps"] * set["kilograms"]
            if average_count > 0:
                stats[name][date]["average_weight"] = round(
                    average / average_count)

        if stats[name][date]["total_volume"] == 0 or stats[name][date]["total_reps"] == 0:
            del (stats[name][date])


save_file = open("stats.json", "w")
save_file.write(json.dumps(stats))
save_file.close()
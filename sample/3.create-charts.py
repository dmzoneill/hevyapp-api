import matplotlib.pyplot as plt
import pandas as pd
import json

path = "graphs/"

plt.style.use(
    'https://github.com/dhaitz/matplotlib-stylesheets/raw/master/pitayasmoothie-dark.mplstyle')

stats = {
    "skip": {
        "date": {
            "total_volume": "(kilo * reps) + set",
            "total_reps": "add up all repos from each set",
            "max_weight": "max",
            "average_weight": "average",
            "median": ""
        }
    }
}

del (stats["skip"])

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


for exercise in stats.keys():
    if len(list(stats[exercise].keys())) < 10:
        continue
    if all(x["total_volume"] == 0 for x in stats[exercise].values()):
        continue

    pdate = list(stats[exercise].keys())
    pdate = pdate[len(pdate) - 20:] if len(pdate) > 19 else pdate
    pvolume = [x["total_volume"] for x in stats[exercise].values()]
    pvolume = pvolume[len(pvolume) - 20:] if len(pvolume) > 19 else pvolume

    data = {
        'date': pdate,
        'volume': pvolume
    }

    df = pd.DataFrame(data)
    plt.figure()
    plt.plot(df['date'], df['volume'], color='red', marker='o')
    plt.title(exercise + ' volume', fontsize=14)
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Kilos', fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.grid(True)
    # plt.show()
    plt.savefig(path + exercise + '-volume.png', bbox_inches='tight')
    plt.close()


for exercise in stats.keys():
    if len(list(stats[exercise].keys())) < 10:
        continue
    if all(x["total_reps"] == 0 for x in stats[exercise].values()):
        continue

    pdate = list(stats[exercise].keys())
    pdate = pdate[len(pdate) - 20:] if len(pdate) > 19 else pdate
    preps = [x["total_reps"] for x in stats[exercise].values()]
    preps = preps[len(preps) - 20:] if len(preps) > 19 else preps

    data = {
        'date': pdate,
        'reps': preps
    }

    df = pd.DataFrame(data)
    plt.figure()
    plt.plot(df['date'], df['reps'], color='red', marker='o')
    plt.title(exercise + ' reps', fontsize=14)
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Reps', fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.grid(True)
    # plt.show()
    plt.savefig(path + exercise + '-reps.png', bbox_inches='tight')
    plt.close()


for exercise in stats.keys():
    if len(list(stats[exercise].keys())) < 10:
        continue
    if all(x["max_weight"] == 0 for x in stats[exercise].values()):
        continue

    pdate = list(stats[exercise].keys())
    pdate = pdate[len(pdate) - 20:] if len(pdate) > 19 else pdate
    pweight = [x["max_weight"] for x in stats[exercise].values()]
    pweight = pweight[len(pweight) - 20:] if len(pweight) > 19 else pweight

    data = {
        'date': pdate,
        'weight': pweight
    }

    df = pd.DataFrame(data)
    plt.figure()
    plt.plot(df['date'], df['weight'], color='red', marker='o')
    plt.title(exercise + ' max weight', fontsize=14)
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Kilos', fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.grid(True)
    # plt.show()
    plt.savefig(path + exercise + '-weight.png', bbox_inches='tight')
    plt.close()

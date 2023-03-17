import matplotlib.pyplot as plt
import pandas as pd
import json

path = "graphs/"

plt.style.use(
    "https://github.com/dhaitz/matplotlib-stylesheets/raw/master/pitayasmoothie-dark.mplstyle"
)

stats = {
    "skip": {
        "date": {
            "total_volume": "(kilo * reps) + set",
            "total_reps": "add up all repos from each set",
            "max_weight": "max",
            "average_weight": "average",
            "median": "",
        }
    }
}

del stats["skip"]

names = []
workout_time = {}
workout_volume = {}

workouts = open("workouts.json").read()
wos = json.loads(workouts)

for X in wos:
    index = X["nth_workout"]
    name = X["name"]
    names.append(name.replace(" ", ""))
    workout_time[index] = round((X["end_time"] - X["start_time"]) / 60)
    workout_volume[index] = round(X["estimated_volume_kg"])

    for exercise in X["exercises"]:
        exercise_title = exercise["title"]

        if exercise_title not in stats.keys():
            stats[exercise_title] = {}

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

        stats[exercise_title][index] = {}
        stats[exercise_title][index]["total_volume"] = round(volume)
        stats[exercise_title][index]["max_weight"] = max
        stats[exercise_title][index]["total_reps"] = reps
        stats[exercise_title][index]["average_weight"] = reps


for exercise in stats.keys():
    if len(list(stats[exercise].keys())) < 10:
        continue
    if all(x["total_volume"] == 0 for x in stats[exercise].values()):
        continue

    pdate = list(stats[exercise].keys())
    pdate = pdate[len(pdate) - 20 :] if len(pdate) > 19 else pdate
    pvolume = [x["total_volume"] for x in stats[exercise].values()]
    pvolume = pvolume[len(pvolume) - 20 :] if len(pvolume) > 19 else pvolume

    data = {"date": pdate, "volume": pvolume}

    df = pd.DataFrame(data)
    plt.figure()
    plt.plot(df["date"], df["volume"], color="red", marker="o")
    plt.title(exercise + " volume", fontsize=14)
    plt.xlabel("Date", fontsize=12)
    plt.ylabel("Kilos", fontsize=12)
    plt.xticks(rotation=45, ha="right")
    plt.grid(True)
    # plt.show()
    plt.savefig(path + exercise + "-volume.png", bbox_inches="tight")
    plt.close()


for exercise in stats.keys():
    if len(list(stats[exercise].keys())) < 10:
        continue
    if all(x["total_reps"] == 0 for x in stats[exercise].values()):
        continue

    pdate = list(stats[exercise].keys())
    pdate = pdate[len(pdate) - 20 :] if len(pdate) > 19 else pdate
    preps = [x["total_reps"] for x in stats[exercise].values()]
    preps = preps[len(preps) - 20 :] if len(preps) > 19 else preps

    data = {"date": pdate, "reps": preps}

    df = pd.DataFrame(data)
    plt.figure()
    plt.plot(df["date"], df["reps"], color="red", marker="o")
    plt.title(exercise + " reps", fontsize=14)
    plt.xlabel("Date", fontsize=12)
    plt.ylabel("Reps", fontsize=12)
    plt.xticks(rotation=45, ha="right")
    plt.grid(True)
    # plt.show()
    plt.savefig(path + exercise + "-reps.png", bbox_inches="tight")
    plt.close()


for exercise in stats.keys():
    if len(list(stats[exercise].keys())) < 10:
        continue
    if all(x["max_weight"] == 0 for x in stats[exercise].values()):
        continue

    pdate = list(stats[exercise].keys())
    pdate = pdate[len(pdate) - 20 :] if len(pdate) > 19 else pdate
    pweight = [x["max_weight"] for x in stats[exercise].values()]
    pweight = pweight[len(pweight) - 20 :] if len(pweight) > 19 else pweight

    data = {"date": pdate, "weight": pweight}

    df = pd.DataFrame(data)
    plt.figure()
    plt.plot(df["date"], df["weight"], color="red", marker="o")
    plt.title(exercise + " max weight", fontsize=14)
    plt.xlabel("Date", fontsize=12)
    plt.ylabel("Kilos", fontsize=12)
    plt.xticks(rotation=45, ha="right")
    plt.grid(True)
    # plt.show()
    plt.savefig(path + exercise + "-weight.png", bbox_inches="tight")
    plt.close()

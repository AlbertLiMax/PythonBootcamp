from module import *

data = get_exercise_data()

for exercise in data["exercises"]:
    exercise_name = exercise["name"].title()
    duration = exercise["duration_min"]
    calories = exercise["nf_calories"]
    update_google_sheet(exercise_name, duration, calories)
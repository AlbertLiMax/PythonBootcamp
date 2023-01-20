import os
import requests
from datetime import datetime

NUTRITIONIX_APP_ID = os.environ.get("NUTRITIONIX_APP_ID")
NUTRITIONIX_API_KEY = os.environ.get("NUTRITIONIX_API_KEY")
SHEETY_AUTH = os.environ.get("SHEETY_AUTH")
SHEETY_USER = os.environ.get("SHEETY_USER")

def get_exercise_data():
    nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

    nutritionix_headers = {
        "x-app-id": NUTRITIONIX_APP_ID,
        "x-app-key": NUTRITIONIX_API_KEY,
    }

    nutritionix_exercise_parameters = {
        "query": input("Tell me which exercises you did: "),
        "gender": "male",
        "weight_kg": 68,
        "height_cm": 175,
        "age": 30
    }

    response = requests.post(url=nutritionix_endpoint,
                             json=nutritionix_exercise_parameters, headers=nutritionix_headers)
    response.raise_for_status()
    data = response.json()
    return data

def update_google_sheet(exercise_type, duration, calories):
    sheety_endpoint = f"https://api.sheety.co/{SHEETY_USER}/workouts/sheet1"

    sheety_headers = {
        "Authorization": f"Basic {SHEETY_AUTH}",
        "Content-Type": "application/json",
    }

    today = datetime.now()
    today_date = today.strftime("%d/%m/%Y")
    today_time = today.strftime("%X")

    sheety_parameters = {
        "sheet1" : {
            "date" : today_date,
            "time" : today_time,
            "exercise" : exercise_type,
            "duration" : duration,
            "calories": calories,
        }
    }

    response = requests.post(url=sheety_endpoint, json=sheety_parameters, headers=sheety_headers)
    response.raise_for_status()
    print(response.text)
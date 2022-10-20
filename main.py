import requests
from datetime import datetime
import os

APP_ID = '9f9cb1e8'
API_KEY = 'd26cd935034493cea50a23f2f46b4677'
TRACK_API_ENDPOINT = 'https://trackapi.nutritionix.com'
NATURAL_ENDPOINT = f'{TRACK_API_ENDPOINT}/v2/natural/exercise'
SHEETY_ENDPOINT = 'https://api.sheety.co/00af5c36f063e0a922f4aaffbe3a5cac/copyOfMyWorkouts/workouts'
exercise_entry = input('Tell me which exercises you did: ')

user_params = {
    'query': exercise_entry,
    'gender': 'male',
    'weight_kg': 75,
    'height_cm': 180,
    'age': 22
}
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

bearer_headers = {

    'Authorization': 'Bearer tyfneiwrntyweituqepot'
}

response = requests.post(url=NATURAL_ENDPOINT, json=user_params, headers=headers)
data = (response.json())

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in data["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(url=SHEETY_ENDPOINT, json=sheet_inputs, headers=bearer_headers)

    print(sheet_response.text)

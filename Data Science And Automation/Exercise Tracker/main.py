import requests
from datetime import datetime
import os


GENDER = "male"
WEIGHT_KG = 65
HEIGHT_CM = 150
AGE = 20

APP_ID = os.environ["ET_APP_ID"]
API_KEY = os.environ["ET_API_KEY"]

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)

sheet_endpoint = os.environ["SHEET_ENDPOINT"]
TOKEN = os.environ["TOKEN"]

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    # # No Authentication
    # sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)

    # # Basic Authentication
    # USERNAME = "solution"
    # PASSWORD = "password"
    # sheet_response = requests.post(
    #     sheet_endpoint,
    #     json=sheet_inputs,
    #     auth=(USERNAME,
    #           PASSWORD,
    #           )
    # )

    # print(sheet_response.status_code)
    # Bearer Token Authentication
    bearer_headers = {
        "Authorization": f"Bearer {TOKEN}"
    }
    sheet_response = requests.post(
        sheet_endpoint,
        json=sheet_inputs,
        headers=bearer_headers
    )
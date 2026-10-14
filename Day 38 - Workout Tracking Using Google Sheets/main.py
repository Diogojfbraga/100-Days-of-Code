
import os
import requests
from datetime import datetime
from requests.auth import HTTPBasicAuth

# ---------------------------------------------------------
# 1. API SETTINGS
# ---------------------------------------------------------

# Nutrition API credentials
APP_ID = os.environ["NUTRITION_APP_ID"]
API_KEY = os.environ["NUTRITION_API_KEY"]

# Sheety login credentials
LOGIN = os.environ["SHEETY_USERNAME"]
PASSWORD = os.environ["SHEETY_PASSWORD"]

# API endpoints
EXERCISE_ENDPOINT = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"
SHEETY_ENDPOINT = "https://api.sheety.co/378fa0a198e6726962528fd0992dc370/myWorkouts/workout"


# ---------------------------------------------------------
# 2. USER INPUT
# ---------------------------------------------------------

# Collect personal information for calorie calculations
weight_kg = int(input("What is your weight in kg? "))
height_cm = int(input("What is your height in cm? "))
age = int(input("How old are you? "))
gender = input("What is your gender ('male' or 'female')? ")
exercise = input("What exercise did you do? ")


# ---------------------------------------------------------
# 3. NUTRITION API REQUEST
# ---------------------------------------------------------

# Authentication headers
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

# Exercise information sent to the API
exercise_config = {
    "query": exercise,
    "gender": gender,
    "weight_kg": weight_kg,
    "height_cm": height_cm,
    "age": age,
}

# Request exercise duration and estimated calories
response = requests.post(
    url=EXERCISE_ENDPOINT,
    json=exercise_config,
    headers=headers,
    timeout=30,
)

# Stop if the request failed
response.raise_for_status()

result = response.json()


# ---------------------------------------------------------
# 4. DATE AND TIME
# ---------------------------------------------------------

# Record when the workout was completed
now = datetime.now()

today_date = now.strftime("%d/%m/%Y")
now_time = now.strftime("%H:%M:%S")


# ---------------------------------------------------------
# 5. SAVE WORKOUTS TO GOOGLE SHEETS
# ---------------------------------------------------------

# Set up Sheety Basic Authentication
basic_auth = HTTPBasicAuth(LOGIN, PASSWORD)

# Save each exercise as a separate row
for exercise in result["exercises"]:

    # Prepare the workout information
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

    # Send the workout to Sheety
    sheety_response = requests.post(
        url=SHEETY_ENDPOINT,
        json=sheet_inputs,
        auth=basic_auth,
        timeout=30,
    )

    # Check whether the workout was saved
    sheety_response.raise_for_status()
    print(f"Saved: {exercise['name'].title()}")
    print(sheety_response.text)

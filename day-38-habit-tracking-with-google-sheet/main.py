import os
import requests
import json
import datetime as dt


NLP_API_ID = os.environ["API_ID"]
NLP_API_KEY = os.environ["API_KEY"]
NLP_URL = "https://trackapi.nutritionix.com/v2/natural/exercise"

NLP_HEADERS = {
    "x-app-id": NLP_API_ID,
    "x-app-key": NLP_API_KEY
}


def exercise_text_nlp(exercise_text="ran 3 miles"):

    params = {
        "query": exercise_text
    }

    response = requests.post(NLP_URL, json=params, headers=NLP_HEADERS)
    response.raise_for_status()
    print(json.dumps(response.json(), indent=4))

    return response.json()


SHEETY_URL = "https://api.sheety.co/28317aaac2e1b81628c20171aa1d3eb9/myFakeWorkout/workouts"
SHEETY_TOKEN = os.environ.get('SHEETY_TOKEN')


def write_to_sheet(record):
    '''
    example of record: 
    {"date": "22/03/2022",
                    "time": "12:00",
                    "exercise": "Swimming",
                    "duration": "19",
                    "calories": "100"}
    '''

    headers = {
        "Content-Type": "application/json",
        "Authorization": SHEETY_TOKEN
    }

    params = {
        "workout":
        record
    }

    # response = requests.get(sheety_url)
    response = requests.post(SHEETY_URL, json=params, headers=headers)
    response.raise_for_status()
    print(json.dumps(response.json(), indent=4))


def delete_record(row_num):
    response = requests.delete(f"{SHEETY_URL}/{row_num}")
    response.raise_for_status()
    # print(json.dumps(response.json(), indent=4))


if __name__ == "__main__":
    data = exercise_text_nlp(input("What have you exercised today?\n"))
    record = {
        "date": dt.datetime.now().strftime("%d/%m/%y"),
        "time": dt.datetime.now().strftime("%H:%M:%S"),
        "exercise": "",
        "duration": "",
        "calories": ""
    }
    for exercise in data["exercises"]:
        record["exercise"] = exercise["user_input"]
        record["duration"] = exercise["duration_min"]
        record["calories"] = exercise["nf_calories"]
        print(record)
        write_to_sheet(record)

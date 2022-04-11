import requests
import os
import json
import pyperclip
from collections import namedtuple


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self, url, API_KEY):
        self.URL = url 
        self.API_KEY = API_KEY
        self.headers = {
            "apikey": self.API_KEY
        }

    def search(self, fly_from, fly_to, date_from, date_to, max_stopovers):
        '''
        returns the flights data (direct flight)
        '''
        # get data 
        param = {
            "fly_from": fly_from,
            "fly_to": fly_to,
            "date_from": date_from,
            "date_to": date_to,
            'max_stopovers': max_stopovers
        }
        response = requests.get(self.URL, headers=self.headers, params=param)
        response.raise_for_status()
        flights = response.json()["data"]
        return flights


if __name__ == "__main__":
    url = "https://tequila-api.kiwi.com/v2/search"
    API_KEY = os.environ.get("FLIGHT_API_KEY")
    flight_search = FlightSearch(url, API_KEY)
    fly_from = "PAR"
    fly_to = "BER"
    date_from = "11/04/2022"
    date_to = "11/06/2022"
    best_flight = flight_search.search_for_best_flight(fly_from, fly_to, date_from, date_to)
    print(best_flight)
    # print(json.dumps(best_flight, indent=4))

import requests
import os
import json
from collections import namedtuple
from flight_search import FlightSearch


class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self, url, API_KEY):
        self.flight_search = FlightSearch(url, API_KEY)

    def search_for_best_flight(self, fly_from, fly_to, date_from, date_to):
        '''
        returns the best deal flight's (direct flight)
        airine + flight_number, from-city-airport-code, to-city-airport-code, date

        If no direct flight was not found, return None 
        '''
        # search best by price 
        flights = self.flight_search.search(fly_from, fly_to, date_from, date_to)
        if flights is None:
            return None

        best_flight = None
        for flight in flights:
            if flight["availability"]["seats"] is not None:
                if best_flight is None:
                    best_flight = flight
                if flight["price"] < best_flight["price"]:
                    best_flight = flight
        if best_flight is None:
            return None 
        Info = namedtuple("Info", "price flight_number fly_from fly_to city_from city_to local_departure local_arrival")
        return Info(
            best_flight["price"],
            str(best_flight["route"][0]["airline"]) + " " + str(best_flight["route"][0]["flight_no"]), 
            best_flight["flyFrom"], 
            best_flight["flyTo"],
            best_flight["cityFrom"],
            best_flight["cityTo"],
            best_flight["local_departure"],
            best_flight["local_arrival"]
        )


if __name__ == "__main__":
    url = "https://tequila-api.kiwi.com/v2/search"
    API_KEY = os.environ.get("FLIGHT_API_KEY")
    flight_data = FlightData(url, API_KEY)
    fly_from = "PAR"
    fly_to = "BER"
    date_from = "11/04/2022"
    date_to = "11/06/2022"
    best_flight = flight_data.search_for_best_flight(fly_from, fly_to, date_from, date_to)
    print(best_flight)

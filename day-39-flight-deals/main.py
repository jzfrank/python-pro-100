# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch
from notification_manager import NotificationManager
import os 

# --------- load data manager ---------
data_manager = DataManager(
    SHEETY_TOKEN=os.environ.get('SHEETY_TOKEN'), 
    SHEETY_URL="https://api.sheety.co/28317aaac2e1b81628c20171aa1d3eb9/travelPlaneTicket/tickets"
)
data = data_manager.get()
tickets = data.json()["tickets"]
# --------- load flight data ----------
url = "https://tequila-api.kiwi.com/v2/search"
API_KEY = os.environ.get("FLIGHT_API_KEY")
flight_data = FlightData(url, API_KEY)
# --------- load notification manager ----------
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
from_number = "+15408024366"
notification_manager = NotificationManager(
    account_sid=account_sid, auth_token=auth_token, 
    from_number=from_number)

# driver code
fly_from = "ZRH"
date_from = "11/04/2022"
date_to = "11/06/2022"
for ticket in tickets:
    fly_to = ticket["iataCode"]
    lowestPrice = ticket.get("lowestPrice", float("inf"))
    best_flight = flight_data.search_for_best_flight(fly_from, fly_to, date_from, date_to)
    print(best_flight.price, type(best_flight.price))
    print(ticket.get("lowestPrice", float("inf")), type(ticket.get("lowestPrice", float("inf"))))
    if best_flight.price < ticket.get("lowestPrice", float("inf")):
        record = {
            "ticket": {
                "lowestPrice": best_flight.price
            }
        }
        data_manager.put(record=record, row_num=ticket["id"])
        message = f"Low price alert! Only €{best_flight.price} to " \
            f"fly from {best_flight.city_from}-{best_flight.fly_from} " \
            f"to {best_flight.city_to}-{best_flight.fly_to}, from {date_from} to {date_to}.\n" \
            f"The flight is {best_flight.flight_number}, " \
            f"departs at {best_flight.local_departure}, arrives at {best_flight.local_arrival}"
        print(message)
        notification_manager.send_message(message=message, to_number="+41765182495")
        print("-------------------")

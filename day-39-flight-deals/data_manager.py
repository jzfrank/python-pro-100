import requests 
import os 
import json


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self, SHEETY_TOKEN, SHEETY_URL):
        self.TOKEN = SHEETY_TOKEN
        self.SHEETY_URL = SHEETY_URL
        self.headers = {
            'Authorization': self.TOKEN,
            "Content-Type": "application/json"
        }

    def get(self):
        response = requests.get(url=self.SHEETY_URL, headers=self.headers)
        response.raise_for_status()
        return response

    def post(self, record):
        response = requests.post(url=self.SHEETY_URL, headers=self.headers, json=record)
        response.raise_for_status()
        return response

    def delete(self, row_num):
        response = requests.delete(url=f"{self.SHEETY_URL}/{row_num}", 
                                   headers={"Authorization": self.TOKEN})
        response.raise_for_status()

    def put(self, row_num, record):
        response = requests.put(url=f"{self.SHEETY_URL}/{row_num}", 
                                headers=self.headers, json=record)
        response.raise_for_status()
        return response        


if __name__ == '__main__':
    data_manager = DataManager(
        SHEETY_TOKEN=os.environ.get('SHEETY_TOKEN'), 
        SHEETY_URL="https://api.sheety.co/28317aaac2e1b81628c20171aa1d3eb9/travelPlaneTicket/tickets"
    )
    # ------- test get --------
    # data = data_manager.get()
    # print(json.dumps(data.json(), indent=4))
    # # ------- test post -------
    # record = {
    #     'ticket': {
    #         'city': "London",
    #         'iataCode': "LON", 
    #         'lowestPrice': '500'
    #     }
    # }
    # data = data_manager.post(record)
    # print(json.dumps(data.json(), indent=4))
    # # ------- test delete -------
    # for i in range(4, 8):
    #     data_manager.delete(row_num=5)
    # # ------- test put -------
    # record = {
    #     'ticket': {
    #         'lowestPrice': '4500'
    #     }
    # }
    # data_manager.put(record=record, row_num=3)

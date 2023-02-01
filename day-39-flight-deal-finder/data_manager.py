import os
import requests

class DataManager:
    #This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.SHEETY_AUTH = os.environ.get("SHEETY_AUTH")
        self.SHEETY_USER = os.environ.get("SHEETY_USER")
        self.sheety_endpoint = f"https://api.sheety.co/{self.SHEETY_USER}/flightDeals/prices"

        self.sheety_headers = {
            "Authorization": f"Basic {self.SHEETY_AUTH}",
            "Content-Type": "application/json",
        }

        self.KIWI_APIKEY = os.environ.get("KIWI_APIKEY")
        self.kiwi_endpoint = "https://api.tequila.kiwi.com/"

        self.kiwi_headers = {
            "apikey": self.KIWI_APIKEY
        }

    def get_data_from_price_sheet(self):
        response = requests.get(url=self.sheety_endpoint, headers=self.sheety_headers)
        response.raise_for_status()
        data = response.json()["prices"]
        return data

    def populate_price_sheet_with_iata(self, iata_list):
        for city in iata_list:
            sheety_parameters = {
                "price": {
                    "iataCode": city
                }
            }

            index = iata_list.index(city)
            response = requests.put(url=self.sheety_endpoint + f"/{index + 2}", json=sheety_parameters, headers=self.sheety_headers)
            response.raise_for_status()
            print(response.text)

    def update_price_sheet_by_city(self, data):
        sheety_parameters = {
            "price": {
                "lowestPrice": data["lowestPrice"]
            }
        }

        index = data["id"]
        response = requests.put(url=self.sheety_endpoint + f"/{index}", json=sheety_parameters,
                                headers=self.sheety_headers)
        response.raise_for_status()
import os
import requests
from datetime import datetime
from dateutil.relativedelta import relativedelta
class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.KIWI_APIKEY = os.environ.get("KIWI_APIKEY")
        self.kiwi_endpoint = "https://api.tequila.kiwi.com/"

        self.kiwi_headers = {
            "apikey": self.KIWI_APIKEY
        }

    def query_city_iata(self, city):
        kiwi_parameters = {
            "term": city
        }

        query_endpoint = self.kiwi_endpoint + "locations/query"
        response = requests.get(url=query_endpoint, params=kiwi_parameters, headers=self.kiwi_headers)
        response.raise_for_status()
        data = response.json()["locations"][0]["code"]
        return data

    def search_flight_data(self, iata):
        today = datetime.now()
        half_year_after_today = today + relativedelta(months=6)
        today_date = today.strftime("%d/%m/%Y")
        half_year_after_today_date = half_year_after_today.strftime("%d/%m/%Y")

        kiwi_parameters = {
            "fly_from": "TPE",
            "fly_to": iata,
            "date_from": today_date,
            "date_to": half_year_after_today_date,
            "curr": "USD"
        }

        search_endpoint = self.kiwi_endpoint + "v2/search"
        response = requests.get(url=search_endpoint, params=kiwi_parameters, headers=self.kiwi_headers)
        response.raise_for_status()
        result = response.json()["data"][0]
        return result

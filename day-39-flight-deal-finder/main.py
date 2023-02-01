#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

# ----------------------------Initialize-------------------------------#
dm = DataManager()
fs = FlightSearch()

data = dm.get_data_from_price_sheet()
city_list = [item["city"] for item in data]
iata_list = [fs.query_city_iata(city) for city in city_list]
dm.populate_price_sheet_with_iata(iata_list)

fd = FlightData(data)
nm = NotificationManager()

# ----------------------------Search Flight Deals----------------------#
data = dm.get_data_from_price_sheet()
for item in data:
    result = fs.search_flight_data(item["iataCode"])
    price = result["price"]
    lowest_price = fd.check_lowest_price_by_city(item["iataCode"])
    if price < lowest_price:
        # Update price sheet
        item["lowestPrice"] = price
        dm.update_price_sheet_by_city(item)
        # Send SMS
        city_to = item["city"]
        iata_to = item["iataCode"]
        outbound_date = result["local_departure"][:10]
        inbound_date = result["local_arrival"][:10]
        sms = f"Low price alert! Only ${price} to fly from Taipei-TPE to {city_to}-{iata_to}," \
              f" from {outbound_date} to {inbound_date}"
        nm.send_sms(sms)
class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, data):
        self.flight_data = []
        for item in data:
            single_city_data = {
                "city": item["city"],
                "iata": item["iataCode"],
                "price": item["lowestPrice"],
                "id": item["id"]
            }
            self.flight_data.append(single_city_data)

    def check_lowest_price_by_city(self, iata):
        for item in self.flight_data:
            if item["iata"] == iata:
                return item["price"]


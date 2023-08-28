class FlightData:
    def __init__(self, flight):
        self.flight = flight

    def structure_data(self):
        if self.flight["data"]:
            data = {
                "cityFrom": self.flight["data"][0]["cityFrom"],
                "cityTo": self.flight["data"][0]["cityTo"],
                "cityCodeFrom": self.flight["data"][0]["cityCodeFrom"],
                "cityCodeTo": self.flight["data"][0]["cityCodeTo"],
                "utc_departure": self.flight["data"][0]["utc_departure"].split("T")[0],
                "utc_arrival": self.flight["data"][0]["utc_arrival"].split("T")[0],
                "price": self.flight["data"][0]["price"]
            }
            return data

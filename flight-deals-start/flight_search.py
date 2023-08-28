import requests

FLY_FROM = "ALA"
FLY_END_POINT = "https://api.tequila.kiwi.com/v2/search"
API_KEY = "YOUR_API"


class FlightSearch:
    def __init__(self, fly_to, date_from, date_to, price_to):
        self.fly_from = FLY_FROM
        self.fly_to = fly_to
        self.date_from = date_from
        self.date_to = date_to
        self.curr = "USD"
        self.price_to = price_to
        self.max_fly_duration = 24
        self.sort = "price"
        self.limit = 1

    def make_request(self):
        fly_header = {
            "apikey": API_KEY
        }
        fly_params = {
            "fly_from": self.fly_from,
            "fly_to": self.fly_to,
            "date_from": self.date_from,
            "date_to": self.date_to,
            "curr": self.curr,
            "price_to": self.price_to,
            "max_fly_duration": self.max_fly_duration,
            "sort": self.sort,
            "limit": self.limit
        }
        response = requests.get(url=FLY_END_POINT, headers=fly_header, params=fly_params)
        response.raise_for_status()
        return response.json()

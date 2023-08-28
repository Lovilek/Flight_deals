import requests

URL_SHEETY = "https://api.sheety.co/dbee778e57aa6cc1c15d2ce3021a91e1/flightDeals/prices"


class DataManager:
    def get_data(self):
        response = requests.get(url=URL_SHEETY)
        return response.json()

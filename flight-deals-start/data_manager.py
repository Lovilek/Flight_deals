import requests

URL_SHEETY = "SHEETY_API"


class DataManager:
    def get_data(self):
        response = requests.get(url=URL_SHEETY)
        return response.json()

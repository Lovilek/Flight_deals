from data_manager import DataManager
from flight_data import FlightData
from notification_manager import NotificationManager
from flight_search import FlightSearch
from datetime import datetime

date_f = datetime.now()
now_date = date_f.strftime("%d/%m/%Y")
if date_f.month + 6 > 12:
    future_date = datetime(date_f.year + 1, date_f.month + 6 - 12, date_f.day)
    future_date = future_date.strftime("%d/%m/%Y")
else:
    future_date = datetime(date_f.year, date_f.month + 6, date_f.day)
    future_date = future_date.strftime("%d/%m/%Y")


data_manager = DataManager()
sheet_data = data_manager.get_data()

all_cheap_flights = []

for data in sheet_data["prices"]:
    flight_search = FlightSearch(fly_to=data["iataCode"], date_from=now_date, date_to=future_date,
                                 price_to=data["lowestPrice"])
    flight = flight_search.make_request()
    flight_data = FlightData(flight=flight)
    structured_data = flight_data.structure_data()
    if structured_data:
        all_cheap_flights.append(structured_data)


notification_manager = NotificationManager(all_cheap_flights=all_cheap_flights)
notification_manager.send_message()

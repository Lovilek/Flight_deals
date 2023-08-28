from twilio.rest import Client

ACCOUNT_ID = "AC4c067a311cb216e274a864024eab570e"
TOKEN = "1ee3076cf97c142875a4b5f9b9c5c50b"


class NotificationManager:
    def __init__(self, all_cheap_flights):
        self.all_cheap_flights = all_cheap_flights

    def send_message(self):
        client = Client(ACCOUNT_ID, TOKEN)
        for flight in self.all_cheap_flights:
            message = client.messages.create(
                from_='+18642522521',
                to='+77787329544',
                body=f"\nLow price alert! Only {flight['price']}$ to fly \nfrom {flight['cityFrom']}-{flight['cityCodeFrom']} to {flight['cityTo']}-{flight['cityCodeTo']}\nfrom {flight['utc_departure']} to {flight['utc_arrival']}"
            )

import os
from twilio.rest import Client

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.TWILIO_SID = os.environ.get("TWILIO_SID")
        self.TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
        self.client = Client(self.TWILIO_SID, self.TWILIO_AUTH_TOKEN)
        self.phone = os.environ.get("PHONE_NUM")
    def send_sms(self, sms):
        message = self.client.messages.create(
            body=sms,
            from_="+18787688974",
            to=self.phone
        )
        print(message.status)
import requests
import os
import datetime
from twilio.rest import Client

TWILIO_SID = os.environ.get("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")

client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

WAPI_Endpoint = "http://api.weatherapi.com/v1/forecast.json"

WAPI_KEY = os.environ.get("WAPI_KEY")

umbrella = False

tomorrow = datetime.date.today() + datetime.timedelta(days=1)

weather_parameters = {
    "q": "24.8383,121.0078",
    "dt": tomorrow,
    "key": WAPI_KEY,
}

response = requests.get(url=WAPI_Endpoint, params=weather_parameters)
response.raise_for_status()
weather_data = response.json()

hour_data = weather_data["forecast"]["forecastday"][0]["hour"]
for data in hour_data[8:18]:
    condition = data["condition"]["text"].lower()
    if "rain" in condition or "snow" in condition or \
        "thunder" in condition or "blizzard" in condition or \
        "sleet" in condition or "pellets" in condition:
        umbrella = True
        break

if umbrella:
    message = client.messages.create(
        body="It's going to rain tomorrow. Remember to bring an ☂️",
        from_="+18787688974",
        to="+886123456789"
    )
    print(message.status)
import os
import requests
from twilio.rest import Client

ALPHA_API = "https://www.alphavantage.co/query"
ALPHA_KEY = os.environ.get("ALPHA_KEY")
NEWS_API = "https://newsapi.org/v2/everything"
NEWS_KEY = os.environ.get("NEWS_KEY")
TWILIO_SID = os.environ.get("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")

client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

def percentage(part, whole):
    return 100 * float(part)/float(whole)

# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then return True.
def security_price_check(symbol):
    alpha_parameters = {
        "function": "TIME_SERIES_DAILY_ADJUSTED",
        "symbol": symbol,
        "apikey": ALPHA_KEY,
    }

    response = requests.get(url=ALPHA_API, params=alpha_parameters)
    response.raise_for_status()
    data = response.json()["Time Series (Daily)"]
    last_two_days_data = list(data.items())[:2]
    volatility = percentage(
        float(last_two_days_data[0][1]["4. close"]) - float(last_two_days_data[1][1]["4. close"]),
        float(last_two_days_data[1][1]["4. close"]))

    return volatility


def get_news(key_word):
    news_parameters = {
        "q": key_word,
        "apiKey": NEWS_KEY,
    }

    response = requests.get(url=NEWS_API, params=news_parameters)
    response.raise_for_status()
    data = response.json()["articles"]
    raw_news = data[:3]
    latest_three_news = [(item["title"], item["description"]) for item in raw_news]
    return latest_three_news

def send_sms(message):
    phone = os.environ.get("PHONE_NUM")
    message = client.messages.create(
        body=message,
        from_="+18787688974",
        to=phone
    )
    print(message.status)
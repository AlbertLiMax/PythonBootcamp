from modules import *

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

# check security price
volatility = security_price_check(STOCK)

# get news and send sms if needed
if abs(volatility) >= 5:
    news = get_news(COMPANY_NAME)
    if volatility > 0:
        mark = "🔺"
    else:
        mark = "🔻"

    for item in news:
        sms_body = f"{STOCK}:  {mark}{abs(volatility):.2f}%\n" \
               f"Headline: {item[0]}.\n" \
               f"Brief: {item[1]}."
        send_sms(sms_body)
import requests
from datetime import datetime, timezone
import smtplib
import time

MY_LAT = 24.826990 # Your latitude
MY_LONG = 121.013000 # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.
def is_iss_over_head():
    lat_diff = abs(iss_latitude - MY_LAT)
    long_diff = abs(iss_longitude - MY_LONG)
    if lat_diff <= 5 and long_diff <= 5:
        return True
    else:
        return False

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now(timezone.utc).hour
# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
def is_night():
    if sunset <= time_now <= sunrise:
        return True
    else:
        return False

def send_notify_email():
    my_email = "alissa.cpr@gmail.com"
    password = "placeholder"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=my_email,
                            msg=f"Subject:ISS overhead now, look up!\n\n"
                                f"The ISS is above you in the sky!")

while True:
    time.sleep(60)
    if is_iss_over_head() and is_night():
            send_notify_email()

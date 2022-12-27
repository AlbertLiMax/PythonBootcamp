from random import choice
import datetime as dt
import smtplib

now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 0:
    with open("quotes.txt") as file:
        quote_list = file.readlines()
        quote = choice(quote_list)

    my_email = "alissa.cpr@gmail.com"
    password = "placeholder"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="asura.cpr@gmail.com",
                            msg=f"Subject:Motivational Quotes on Mondays!\n\n"
                                f"{quote}")
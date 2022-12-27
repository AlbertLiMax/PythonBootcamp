##################### Extra Hard Starting Project ######################
import smtplib
import datetime as dt
from random import choice
import pandas

# ---------------------------- LOAD DATABASE ----------------------------------------- #
df = pandas.read_csv("birthdays.csv")
database = df.to_dict(orient="records")

letters = []
for i in range(1, 4):
    with open(f"letter_templates/letter_{i}.txt") as file:
        letters.append(file.read())


# ---------------------------- PREPARE LETTER ---------------------------------------- #
def prepare_letter(name):
    letter = choice(letters).replace("[NAME]", name)
    return letter


# ---------------------------- SEND LETTERS ------------------------------------------ #
EMAIL = "alissa.cpr@gmail.com"
PASSWORD = "placeholder"

def send_letter(addr, title, msg):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=EMAIL, to_addrs=f"{addr}", msg=f"Subject:{title}\n\n{msg}")


# ---------------------------- CHECK IF BIRTHDAY MATCH ------------------------------- #
def is_birthday(date):
    today = dt.datetime.now()
    if date.month == today.month and date.day == today.day:
        return True
    else:
        return False


# ---------------------------- LOOP THROUGH DATABASE --------------------------------- #
for item in database:
    date = dt.datetime(year=item["year"], month=item["month"], day=item["day"])
    if is_birthday(date):
        letter = prepare_letter(item["name"])
        send_letter(item["email"], "Happy Birthday!", letter)
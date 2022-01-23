import smtplib
import datetime as dt
import random

MY_EMAIL = "afsar291722@gmail.com"
MY_PASSWORD = "29172222"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 5: # Saturday
    with open("quotes.txt") as quote_file:
        all_quote = quote_file.readlines()
        quote = random.choice(all_quote)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="ak0090764@gmail.com",
            msg=f"Subject: Monday Motivation\n\n{quote}"
        )

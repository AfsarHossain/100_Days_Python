import smtplib

my_email = "afsar291722@gmail.com"
password = "29172222"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="ak0090764@gmail.com",
                        msg="Subject:Hello\n\nThis is the body of my code."
                        )

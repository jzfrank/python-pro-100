import smtplib 
from getpass import getpass 
import datetime as dt 
import random 
import os 

my_email = os.environ.get("MY_EMAIL")
TO_EMAIL = os.environ.get("TO_EMAIL")
pswd = getpass()

with open("quotes.txt", "r") as file:
    quotes = file.readlines()

print(quotes[:4])


if dt.datetime.now().weekday() == 0:
    msg = f"""Subject:Today wil be a good day\n\nDear Frank,\n
	{random.choice(quotes)}
\nBest,\nJin"""


with smtplib.SMTP_SSL("smtp.gmail.com") as connection:
    # connection.starttls()
    connection.login(user=my_email, password=pswd)
    connection.sendmail(
        my_email,
        TO_EMAIL,
        msg
    )

import smtplib 
from getpass import getpass 
import datetime as dt 
import random 

my_email = "zhangjin0001999@gmail.com"
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
		"frankjinzhang@gmail.com",
		msg
		)




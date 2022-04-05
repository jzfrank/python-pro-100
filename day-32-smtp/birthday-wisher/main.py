##################### Extra Hard Starting Project ######################


import pandas as pd 
import random 
import datetime as dt 
import smtplib
from getpass import getpass 

def replate_name(template, user_name):
	start = template[0].find("[")
	end = template[0].find("]")
	template[0] = (template[0][:start] 
		+ user_name + template[0][end+1:])


my_email = "zhangjin0001999@gmail.com"
my_pswd = getpass()

# 1. Update the birthdays.csv
birthdays = pd.read_csv("birthdays.csv")
user_names = list(birthdays.name)

for user_name in user_names:
	user_name = "Jin"
	user = birthdays[birthdays['name'] == user_name]
	user_email = user.email 
	user_birthday = dt.datetime(year=int(user.year), month=int(user.month), day=int(user.day))
	print(user_birthday)

	# 2. Check if today matches a birthday in the birthdays.csv
	today = dt.datetime.now()
	is_birthday = False 
	if today.day == user_birthday.day and today.month == user_birthday.month:
		is_birthday = True 

	# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
	templates = []
	for file_name in ["letter_1.txt", "letter_2.txt", "letter_3.txt"]:
		with open(f"letter_templates/{file_name}", "r") as file:
			templates.append(file.readlines())

	template = random.choice(templates)
	replate_name(template, user_name)
	print("".join(template))
	msg = f'''Subject:Happy Birthday
	\n\n{"".join(template)}
	'''

	# 4. Send the letter generated in step 3 to that person's email address.
	

	with smtplib.SMTP_SSL("smtp.gmail.com") as conn:
		conn.login(user=my_email, password=my_pswd)
		conn.sendmail(
			my_email,
			user_email,
			msg 
			)





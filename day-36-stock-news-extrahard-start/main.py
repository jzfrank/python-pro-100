import os 
import requests
import pandas as pd 


# STOCK = "TSLA"
# COMPANY_NAME = "Tesla Inc"


STOCK = "AMZN"
COMPANY_NAME = "Amazon"



## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

def get_movement_percentage():
	url = 'https://www.alphavantage.co/query'
	params = {
		"function": "TIME_SERIES_DAILY",
		"symbol": STOCK,
		"apikey": os.environ["ALPHA_API_KEY"]
	}

	r = requests.get(url, params=params)
	data = r.json()

	df = pd.DataFrame.from_dict(data['Time Series (Daily)'], orient='index')

	close = "4. close"
	yesterday_price = float(df.iloc[0][close] )
	day_before_yesterday_price = float(df.iloc[1][close])

	# print(yesterday_price, day_before_yesterday_price)

	movement_percentage = (yesterday_price - day_before_yesterday_price) / yesterday_price
	return movement_percentage



## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

def get_top3_news():
	url = "https://newsapi.org/v2/everything"
	params = {
		"q": COMPANY_NAME, 
		"apiKey": os.environ["NEWS_API_KEY"]
	}

	response = requests.get(url=url, params=params)
	data = response.json()
	news = ""
	for article in data["articles"][:3]:
		news += f"Headline: {article['title']}\nBrief: {article['description']}\n\n"
	return news 

def prepare_message(movement_percentage):
	if movement_percentage > 0:
			msg = "🔺"
	else:
		msg = "🔻"
	msg += f'''{STOCK}: {round(movement_percentage * 100, 2)}%\n\n'''
	msg += get_top3_news()
	return msg 


## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


def send_message(msg_body):
	from twilio.rest import Client 
	account_sid = os.environ['TWILIO_ACCOUNT_SID']
	auth_token = os.environ['TWILIO_AUTH_TOKEN']

	client = Client(account_sid, auth_token)

	message = client.messages \
	    .create(
	         body=msg_body,
	         from_='+15408024366',
	         to='+41765182495'
	     )

	print(message.status)



if __name__ == '__main__':
	movement_percentage = get_movement_percentage()
	if abs(movement_percentage) > 0.01:
		msg = prepare_message(movement_percentage) 
		send_message(msg_body=msg)




#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

# for testing code 
while True:
	command = input("what to do next?\n") 
	if command == "exit":
		break
	try:  
		eval(command)
	except Exception as e:
		print(e) 


import requests


# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']

weather_api_key = os.environ["WEATHER_API_KEY"]

print(account_sid, auth_token, weather_api_key)

city2latlon = {
	'Zurich': (47.376888, 8.541694),
	'Shanghai': (31.2304, 121.4737)
}
# lat, lon = city2latlon['Shanghai']
lat, lon = city2latlon['Zurich']
url = "https://api.openweathermap.org/data/2.5/onecall"
params = {
	'lat': lat,
	'lon': lon,
	'exclude': "current,minutely,daily",
	"appid": weather_api_key
}
response = requests.get(url=url, params=params)

data = response.json()
will_rain = False
for i in data["hourly"][:12]:
	if i['weather'][0]['id'] < 700:
		will_rain = True

if will_rain:
	client = Client(account_sid, auth_token)

	message = client.messages \
	    .create(
	         body='It is raining today. Remember to bring an umbrella.',
	         from_='+15408024366',
	         to='+41765182495'
	     )

	print(message.status)
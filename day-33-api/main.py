import requests  
import datetime as dt 
import smtplib
from getpass import getpass
import os 
import time 

MY_LAT = 47.376888
MY_LONG = 8.541694


MY_EMAIL = os.environ.get('MY_EMAIL')
MY_PASSWORD = getpass()


def iss_is_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data = response.json()
    iss_position = (data["iss_position"]["longitude"], data["iss_position"]["latitude"])
    print(f"iss_position: {iss_position}")
    if (abs(float(iss_position[0]) - MY_LAT) < 5 
            or abs(float(iss_position[1]) - MY_LONG) < 5):
        return True 


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0
    }
    response = requests.get(url="http://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = data["results"]["sunrise"]
    sunset = data["results"]["sunset"]
    time_now = dt.datetime.now().hour
    if time_now >= sunset or time_now <= sunrise:
        return True


while True:
    time.sleep(60)
    TO_EMAIL = os.environ.get("TO_EMAIL")
    if iss_is_overhead() and not is_night():
        conn = smtplib.SMTP("smtp.gmail.com")
        conn.starttls()
        conn.login(MY_EMAIL, MY_PASSWORD)
        conn.sendmail(MY_EMAIL, TO_EMAIL, msg="Subject:Look Up\n\nISS is overhead!")

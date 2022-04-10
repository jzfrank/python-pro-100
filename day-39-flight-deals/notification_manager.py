import requests
import os
from twilio.rest import Client


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self, account_sid, auth_token, from_number):
        self.SID = account_sid
        self.TOKEN = auth_token 
        self.client = Client(self.SID, self.TOKEN)
        self.from_number = from_number

    def send_message(self, message, to_number):
        msg = self.client.messages.\
            create(
                body=message,
                from_=self.from_number,
                to=to_number
            )
        print(msg.sid)


if __name__ == '__main__':
    # Find your Account SID and Auth Token at twilio.com/console
    # and set the environment variables. See http://twil.io/secure
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    from_number = os.environ["TWILIO_FROM_NUMBER"]
    to_number = os.environ["TWILIO_VERIFIED_NUMBER"]
    notification_manager = NotificationManager(
        account_sid=account_sid, auth_token=auth_token, 
        from_number=from_number)
    notification_manager.send_message(message="Hi, how its everything going?", 
                                      to_number=to_number)

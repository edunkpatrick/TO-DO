# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
# from secrets import TWILIO_AUTH_TOKEN
# Set environment variables for your credentials
# Read more at http://twil.io/secure
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']

client = Client(account_sid, auth_token)

message = client.messages.create(
  body="Hello from Twilio",
  from_="",
  to=""
)

print(message.sid)
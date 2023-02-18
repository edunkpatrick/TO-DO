# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client

# Set environment variables for your credentials
# Read more at http://twil.io/secure
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']

client = Client(account_sid, auth_token)

message = client.messages.create(
  body="Hello from TO-DO, please log-in and complete your task(s)",
  from_= os.environ['PHONE_ORIGIN'],
  to= os.environ['PHONE_DESTINATION']
)

print(message.sid)
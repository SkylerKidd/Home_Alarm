from twilio.rest import TwilioRestClient

# put your own credentials here

config = {}
execfile("settings.conf", config)

ACCOUNT_SID = config["ACCOUNT_SID"]
AUTH_TOKEN = config["AUTH_TOKEN"]

client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

client.messages.create(
	to=config["to"],
	from_=config["from"],
	body="Alert!",
)

print "Message sent!"

from twilio.rest import TwilioRestClient
import sys

if 'ACCOUNT_SID' in os.environ:
	ACCOUNT_SID = str(os.environ['ACCOUNT_SID'])
	AUTH_TOKEN = str(os.environ['AUTH_TOKEN'])
	password = str(os.environ['password'])
	toNum = str(os.environ['toNum'])
	fromNum = str(os.environ['fromNum'])
else:
	config = {}
	execfile('settings.conf', config)
	ACCOUNT_SID = config['ACCOUNT_SID']
	AUTH_TOKEN = config['AUTH_TOKEN']
	password = config['password']
	toNum = config["toNum"]
	fromNum = config["fromNum"]

client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

msgAlert = "Alert!!"

try:
    msgAlert = sys.args[0]
except Exception:
    continue

client.messages.create(
	to = toNum,
	from_ = fromNum,
	body = msgAlert,
)

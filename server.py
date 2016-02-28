from twilio.rest import TwilioRestClient
from flask import Flask, jsonify, request
import os

if 'ACCOUNT_SID' in os.environ:
	ACCOUNT_SID = os.environ['ACCOUNT_SID']
	AUTH_TOKEN = os.environ['AUTH_TOKEN']
	password = os.environ['password']
	toNum = os.environ["toNum"],
	fromNum = os.environ["fromNum"],
else:
	config = {}
	execfile("settings.conf", config)
	ACCOUNT_SID = config["ACCOUNT_SID"]
	AUTH_TOKEN = config["AUTH_TOKEN"]
	password = config['password']
	toNum = config["toNum"],
	fromNum = config["fromNum"],

client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

app = Flask(__name__)

#--------------------



@app.route('/api/v1.0/alert', methods=['POST'])
def alert_me():
    if not request.json or not 'title' in request.json:
        abort(400)
	if request.json.password != password:
		abort(400)

	client.messages.create(
		to = toNum,
		from_ = fromNum,
		body = "Alert!",
	)

	resp = {
		'title': request.json['title'],
		'status': True
	}

	print "Message sent!"

    return 201
#--------------------


if __name__ == '__main__':
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port, debug=True)

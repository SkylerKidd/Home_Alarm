from twilio.rest import TwilioRestClient
from flask import Flask, jsonify
import os

if 'ACCOUNT_SID' in os.environ:
	ACCOUNT_SID = os.environ['ACCOUNT_SID']
	AUTH_TOKEN = os.environ['AUTH_TOKEN']
	password = os.environ['password']
	toMess = os.environ["to"],
	fromMess = os.environ["from"],
else:
	try:
		config = {}
		execfile("settings.conf", config)
	except Exception:
		print "No local config file"
	ACCOUNT_SID = config["ACCOUNT_SID"]
	AUTH_TOKEN = config["AUTH_TOKEN"]
	password = config['password']
	toMess = config["to"],
	fromMess = config["from"],

client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

app = Flask(__name__)

#--------------------

@app.route('/api/v1.0/alert', methods=['POST'])
def create_task():
    if not request.json or not 'title' in request.json:
        abort(400)
	if request.json.password != password:
		abort(400)

	client.messages.create(
		to = toMess,
		from_ = fromMess,
		body = "Alert!",
	)

	resp = {
		'title': request.json['title'],
		'status': True
	}

    return jsonify({'resp': resp}), 201

#--------------------

print "Message sent!"

if __name__ == '__main__':
	port = int(os.environ.get("PORT", 5000))
    app.run(debug=True)

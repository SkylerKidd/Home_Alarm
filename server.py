from twilio.rest import TwilioRestClient
from flask import Flask, jsonify

config = {}
execfile("settings.conf", config)

ACCOUNT_SID = config["ACCOUNT_SID"]
AUTH_TOKEN = config["AUTH_TOKEN"]

client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

app = Flask(__name__)

#--------------------

@app.route('/api/v1.0/alert', methods=['POST'])
def create_task():
    if not request.json or not 'title' in request.json:
        abort(400)
	if request.json.password != config["password"]:
		abort(400)

	client.messages.create(
		to=config["to"],
		from_=config["from"],
		body="Alert!",
	)

	resp = {
		'title': request.json['title'],
		'status': True
	}

    return jsonify({'resp': resp}), 201

#--------------------

print "Message sent!"







if __name__ == '__main__':
    app.run(debug=True)

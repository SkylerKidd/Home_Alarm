from twilio.rest import TwilioRestClient
from flask import Flask, jsonify, request, abort
import os

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

app = Flask(__name__)

#--------------------

@app.route('/alert', methods=['POST'])
def send_alert():
	# TODO - Password checking
	posted_data = request.get_json()

	if posted_data['password'] != password:
		abort(400)
	client.messages.create(
		to = toNum,
		from_ = fromNum,
		body = "Alert!!!"
	)
	status = "Succesfully sent!"
	return jsonify({'resp':{'title': request.json['title'],'status': posted_data}})

#--------------------

if __name__ == '__main__':
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port, debug=True)

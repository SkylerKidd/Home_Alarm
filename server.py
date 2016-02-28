from flask import Flask, jsonify, request
import os


app = Flask(__name__)

#--------------------

@app.route('/api/v1.0/alert', methods=['POST'])
def alert_me():
	resp = 1
	return resp

	#--------------------


if __name__ == '__main__':
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port, debug=True)

from flask import Flask
from flask import json
import logging

app = Flask(__name__)

@app.route("/")
def hello():
	## log line
	app.logger.info('Main request successfull')
	return "Hello World!"
	
@app.route("/status")
def status():
	
	data = {"result":"OK - healthy"}
	response = app.response_class(
		response = json.dumps(data),
		status=200,
		mimetype='application/json'
	)
	## log line
	app.logger.info('Status request successfull')
	return response

@app.route("/metrics")
def metrics():

	data = {"status":"success","code":0,"data":{"UserCount":140,"UserCountActive":23}}
	response = app.response_class(
		response = json.dumps(data),
		status=200,
		mimetype='application/json'
	)
	## log line
	app.logger.info('Metrics request successfull')	
	return response
	
if __name__ == "__main__":

	## logging to file
	
	logname = 'app.log'

	logging.basicConfig(filename=logname,
								filemode='a',
								format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
								datefmt='%H:%M:%S',
								level=logging.DEBUG)

	logging.info("Running python app HELLO WORLD")

	app.run(host='0.0.0.0')

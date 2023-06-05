from flask import Flask, jsonify, request
from insurance_fraud.exception import InsuranceFraudException
from insurance_fraud.logger import logging
import os, sys

app = Flask(__name__)


@app.route('/', methods=['GET'])
def helloworld():
	if(request.method == 'GET'):
		try:
			raise Exception("We are testing custom Exception.")       
		except Exception as e:
			insurance_fraud = InsuranceFraudException(e, sys)
			logging.error(insurance_fraud.error_message)
   
		data = {"data": "Hello World"}
		return jsonify(data)


if __name__ == '__main__':
	app.run(debug=True)

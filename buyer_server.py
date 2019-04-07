from flask import Flask, jsonify, render_template
from flask import abort
from flask import make_response,request
import json
import os



app= Flask(__name__)
app.config.from_object(__name__)


app.secret_key = 'my key'


#-------------------------------------------------ANDROID-APP-POST-REQUESTS-------------------------------------------------------------------------

#save details of user into database
@app.route('/buyer', methods=['GET'])
def buyer():
	cmd = os.system('python buyer.py')
	return make_response(jsonify({'success': 'success'}), 200)

@app.route('/update', methods=['POST'])
def update():
	print('SUNNNNNNNNNYYYYYYYY',request.data)
	return make_response(jsonify({'success': 'success'}), 200)


if __name__ == '__main__':
	app.run('127.0.0.1',8083,debug=True)

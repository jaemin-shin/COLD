import requests
import json
'''
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

if __name__=='__main__':
	app.run(host='0.0.0.0')
'''
url = 'http://172.17.0.3:5000/' #IP address of other machine
while(True):
	print ('Client -> Control Plane, /upload (POST) : 1')
	rest_choice = input()
	if int(rest_choice) == 1:
		url = url + 'upload'
		file_info = '{"file_info": ["file", "file_piece1", "file_piece2"]}'
		headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
		response = requests.post(url, data=file_info, headers = headers)
		json_dict = response.json()
		print (json_dict.get('message'))
	

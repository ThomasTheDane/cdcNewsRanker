import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
	toSend = ""
	f = open((time.strftime("%d-%m-%Y")+'.txt'), 'r')
	for line in f:
		toSend += (line)
	return toSend

import os
from flask import Flask
import time	

app = Flask(__name__)

@app.route('/')
def hello():
	print "dickbutt"
	toSend = ""
	if(os.path.isfile((time.strftime("%d-%m-%Y")+'.txt'))):
		print "file found"
		f = open((time.strftime("%d-%m-%Y")+'.txt'), 'r')
		for line in f:
			toSend += (line)
		return toSend
	else:
		return "Report Not Found, check back later"


if __name__ == "__main__":
	# print hello();
    app.run()
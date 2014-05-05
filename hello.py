import os
from flask import Flask
import time	

app = Flask(__name__)

@app.route('/')
def hello():
	print "dickbutt"
	toSend = ""
	# if(os.path.isfile((time.strftime("%d-%m-%Y")+'.txt'))):
	print "file found"
	try:
		f = open((time.strftime("%d-%m-%Y")+'.html'), 'r')
		for line in f:
			toSend += (line)
	except:
		toSend = "File not found"
	return toSend
	# else:
	# 	return "Report Not Found, check back later"


if __name__ == "__main__":
	# print hello();
    app.run()
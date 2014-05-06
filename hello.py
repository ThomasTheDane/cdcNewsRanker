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
		toSend = "<h1>Showing report for " + time.strftime("%m-%d-%Y") + "</h1>"
		f = open((time.strftime("%d-%m-%Y")+'.html'), 'r')
	except:
		f = open("06-05-2014.html", 'r')
		toSend = "<h1>Showing report for 05/06/2014</h1>"
	for line in f:
		toSend += (line)
	return toSend

if __name__ == "__main__":
	# print hello();
    app.run()
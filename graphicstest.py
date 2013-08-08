import sys
sys.path.append('/Users/AnirudhVasudevan/Desktop/graphics3.py')
from graphics3 import *

import socket
 
import threading, signal

def timed_out(signum, frame):
	print("Times up!\n")
	sys.exit()
	
def main():
	print("Opening window\n")
	g = GraphWin("Window", 200, 200)
	g.setBackground("red")
	name = Entry(Point(100,50), 10).draw(g)
	filename = stringname.getText	
	f = open(filename, "w")
	print f

	(Text(Point(100, 25), "Please enter your name:").draw(g))
		
	Text(Point(100, 125), "Click anywhere to begin").draw(g)
	print("Waiting for Mouse\n")
	if g.getMouse():
		
		print("Got Mouse!.. setting timer for 10 seconds\n")
		#t = threading.Timer(10.0, timed_out)
		#t.start()
		signal.signal(signal.SIGALRM, timed_out)
		signal.alarm(10)
		print("timer started.\n")
	
		print("opening socket.\n")
		s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		
		ip = "127.0.0.1"
		print("connecting to " +ip+ "..")
		s.connect((ip,13854))
		print("success\n")
			
		#configString = ""
		configString = "{\"enableRawOutput\":false,\"format\":\"Json\"}"
		#configString = "{\"format\":\"Json\"}"
		print("sent config string\n")
		s.send(configString)
		
		while 1:
			

			buf = s.recv(10000)
			value = str(buf)	
			
			f.write(value)

	


	











main()



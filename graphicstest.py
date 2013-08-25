import sys

from graphics3 import *

import socket
import time
import threading, signal
import thread

def timed_out(signum, frame):
	print("Times up!\n")
	sys.exit()
	
def main():
	print("Opening window\n")
	g = GraphWin("Window", 2000, 2000)
	g.setBackground("red")
	#name = Entry(Point(100,50), 10).draw(g)
	#filename = eval(name.getText())	
	f = open("SuchiVRed "+ " " +time.asctime()+".txt" , "w")

	#(Text(Point(100, 25), "Please enter your name:").draw(g))
		
	#Text(Point(100, 125), "Click anywhere to begin").draw(g)
	print("Waiting for Mouse\n")
	if g.getMouse():
		
		print("Got Mouse!.. setting timer for 30 seconds\n")
		#t = threading.Timer(30.0, timed_out)
		#t.start()
		signal.signal(signal.SIGALRM, timed_out)
		a = signal.alarm(30)
		print("timer started.\n")
		#t = Timer(15.0, g.setBackground("red"))
		#t.start()
		
	#signal.signal(signal.SIGALRM, timed_out)
	#if signal.alarm(15):
		#g.setBackground("red")
			
			
	
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



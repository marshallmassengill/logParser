#!/usr/bin/python

from random import *
if __name__=="__main__":
	not_valid = [10,127,169,172,192]
			 
	first = randrange(1,256)
	while first in not_valid:
		first = randrange(1,256)
	
	ip = ".".join([str(first),str(randrange(1,256)),str(randrange(1,256)),str(randrange(1,256))])
	
	#print ip

	e = randrange(0,4)
	if e == 0:
		errorCode = "error"
	elif e == 1:
		errorCode = "readonly"
	elif e == 2:
		errorCode = "diffError"
	elif e == 3:
		errorCode = "connectionrefused"
	
	print str(ip) + ' ' + str(errorCode)

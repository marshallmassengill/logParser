#!/usr/bin/python
#Break out a count and type of error messages per IP without taking hours to process

#Import the collections library
from collections import *
#import re #I ended up not using regex

#Opening the file
with open('testLog.txt') as logfile:
	#Using collections to get a list and then stripping whitespace
	errorCounts = Counter(line.strip() for line in logfile)
	#Iterating through each item in the list
	for line, count in errorCounts.items():
		#making an assumption that there is only a single space per line ;-)
		ipAddr, errorCode = line.split(" ")
		#Printing things out all nice and pretty
		print 'Error "' + str(errorCode) +'" occurs '+ str(count) + ' time(s) for IP: ' + str(ipAddr)
		#Example output line: Error "connectionrefused" occurs 415 time(s) for IP: 11.81.121.143

#Regex that I ended up not needing:
#Finding IP addresses: r'[0-9]+.[0-9]+.[0-9]+.[0-9]+'
#Finding Error Codes: r' [A-Za-z]+'


# Grabs GT NextBus locations every 10 seconds for 8640 records
# Change the values to get different results.
# Stores results in buses.txt file in same directory.

import urllib2
import json
import time
from time import gmtime, strftime

def getBusLocations():
	request = urllib2.Request("http://m.gatech.edu/proxy/walkpath.cip.gatech.edu/bus_position.php", None)
	opener = urllib2.build_opener()
	while True:
		try:
			f = opener.open(request)
			break
		except Exception, e:
			print(e)
			print("\n======Error occured, sleeping for 10 seconds======")
			time.sleep(10)
	data = json.load(f)
	f.close()
	return data

def printCurrentLocations(f, currentTime, records):
	
	data = getBusLocations()
	f.write(json.dumps({'time': currentTime, 'record': records, 'data': data}) +  "\n")
	

def recordLocations():

	records = 0
	f = open('buses.txt','w')
	o = open('records.txt','w')
	f.write("[\n")
	while(records < 8640):
		currentTime = strftime("%H:%M:%S", gmtime())
		printCurrentLocations(f, currentTime, records)
		records = records + 1
		time.sleep(10)
		if (records % 6 == 0):
			o.write("Done " + str(records) + " records\n")	
	f.write("]\n")	
	f.close()	
	o.close()


recordLocations()

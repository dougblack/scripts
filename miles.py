# Command line milage log tool.

# Usage:
#	Add milage: python miles.py + [milage] [week]
#	Print week: python miles.py = [week]

import sys

def processInput():
	if (sys.argv[1] == "="):
		printWeekMiles(sys.argv[2])
	elif (sys.argv[1] == "+"):
		addMilage(sys.argv[2], sys.argv[3])
	else:
		print "Error: incorrect arguments"
		print "Format: miles.py [+ or = ] [params...]"


def addMilage(milage, week):
	f = open(".miles.txt", "a+")
	f.write(str(week) + "|" + str(milage) + "\n")
	f.close

def printWeekMiles(week):
	f = open(".miles.txt", "r")
	line = f.readline()
	print
	print"Milage for week: ",week
	total = 0
	while (line != ""):
		lineWeek = list(line.split("|"))
		milage = lineWeek[1].split("\n")[0]
		if str(week)==lineWeek[0]:
			print milage
			total += int(lineWeek[1].split("\n")[0])
		line = f.readline()
	print 
	print "Total: " + str(total)
	print
	f.close()
		
processInput()

# A really simple goal pace calculator.
import sys

def getInput():
	if (len(sys.argv) == 4):
		distance = int(sys.argv[1])
		goal = (sys.argv[2])	
		splits = (sys.argv[3])
		return (distance,goal,splits)
	else:
		print("Error: incorrect arguments")
		print("Format: pace.py [distance] [goal] [split]")


def printSplits(distance, goal,splits):
	splits = int(splits)
	(goalMinutes, goalExtraSeconds) = goal.split(":")
	goalSeconds = int(goalMinutes) *60 + int(goalExtraSeconds)
	timePerMeter = goalSeconds / distance
	timePerSplit = timePerMeter * splits
	print()
	print("=====",distance,"AT",goal,"=====")
	print()
	intervalPace = timePerSplit
	for x in range(splits, distance+splits, splits):
		if ((x%1600) == 0):
			print(x,"m:\t",formatToTime(intervalPace),"\t\t",x,"m: \t",formatToTime(intervalPace),"\t\t",x,"m: \t",formatToTime(intervalPace))
		elif ((x % 400) == 0):
			print(x,"m:\t",formatToTime(intervalPace),"\t\t",x,"m: \t",formatToTime(intervalPace))
		else:
			print(x,"m:\t", formatToTime(intervalPace))	
		intervalPace = intervalPace + timePerSplit

	print()
	print("Pace per",splits,"m: " , formatToTime(timePerSplit))
	print("Pace per",2*splits,"m: " , formatToTime(2*timePerSplit))
	print("Pace per",8*splits,"m: " , formatToTime(8*timePerSplit))
	print()

def formatToTime(time):
	minutes = int(time) // int(60)
	seconds = int(time) % int(60)
	secondsString = str(seconds)
	minutesString = str(minutes)
	if (len(secondsString) != 2):
		secondsString = "0"+secondsString 
	return (minutesString + ":" + secondsString)


try:
	(distance, goal,splits) = getInput()
	printSplits(distance,goal,splits)
except Exception:
	pass


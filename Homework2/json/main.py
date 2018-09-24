import json

# find and print cheapest Bar
def printCheapestBar(data):
	minCheck = data[0]["bars"][0]["check"]
	currentBar = {}
	for city in data:
		for bar in city["bars"]:
			if (bar["check"] < minCheck):
				minCheck = bar["check"]
				currentBar = bar
	print ("Cheapest Bar is \"" + currentBar["name"] + "\" (check: " + str(minCheck) + ")")


# find and print expensivest Bar
def printExpensivestBar(data):
	minCheck = data[0]["bars"][0]["check"]
	currentBar = {}
	for city in data:
		for bar in city["bars"]:
			if (bar["check"] > minCheck):
				minCheck = bar["check"]
				currentBar = bar
	print ("Expensivest Bar is \"" + currentBar["name"] + "\" (check: " + str(minCheck) + ")")


# find and print Bars in range
def printBarsInRange(data, min, max):
	print ("All bars between " + str(min) + " and " + str(max) + " are : ")
	for city in data:
		for bar in city["bars"]:
			if (bar["check"] >= min and bar["check"] <= max):
				print ("\t\"" + bar["name"] + "\" (check: " + str(bar["check"]) + ")")


fileName = "cities.json"
jsonFile = open(fileName)
jsonData = json.load(jsonFile)

print ("---------------------------------------------------------------")
printCheapestBar(jsonData)

print ("---------------------------------------------------------------")
printExpensivestBar(jsonData)

print ("---------------------------------------------------------------")
printBarsInRange(jsonData, 350, 400)

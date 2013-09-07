# timed greetings

import datetime

def main():
	name = raw_input("What's your name?\n>> ")
	greet(name)

def greet(name):
	greeting = getTimedGreeting()
	print greeting, name

def getTimedGreeting():
	now = datetime.datetime.now()
	hour = now.time().hour
	if hour < 12:
		greeting = "Good morning"
	elif hour < 18:
		greeting = "Good afternoon"
	else:
		greeting = "Good evening"
	return greeting

# start by executing the main function
if __name__ == '__main__':
	main()
# Bot class with methods for interaction

import datetime
import time

def main():
	chatBot = Bot("Monty")

	name = raw_input("What's your name?\n>> ")
	thisPerson = Person(name)
	
	chatBot.greet(thisPerson.name)
	chatBot.introduce()
	chatBot.perform()
	chatBot.sayBye(thisPerson.name)


class Person(object):
	"""Class Person with name"""
	def __init__(self, name):
		self.name = name

class Bot(object):
	"""Class Bot with name and some talking methods"""
	def __init__(self, name):
		self.name = name

	def introduce(self):
		print "My name is", self.name

	def greet(self, name):
		greeting = self.getTimedGreeting()
		print greeting, name

	def getTimedGreeting(self):
		now = datetime.datetime.now()
		hour = now.time().hour
		if hour < 12:
			greeting = "Good morning"
		elif hour < 18:
			greeting = "Good afternoon"
		else:
			greeting = "Good evening"
		return greeting

	def perform(self):
		interest = raw_input("Would you like to see a trick? [yes / no]\n>> ")
		if interest == "yes":
			self.doTrick()
		elif interest == "no":
			print "Well you sure are a lot of fun..."
			time.sleep(2)
			print "NOT"
			time.sleep(1)
		else:
			print "I dont understand..."
			self.perform()

	def doTrick(self):
		number = int(raw_input("Name a whole number\n>> "))
		numbers = range(1, number + 1)
		numbers.reverse()
		for i in numbers:
			print i
			time.sleep(1)
		print "Holy spam, I just counted down from", number, "!"
		time.sleep(1)

	def sayBye(self, name):
		print "\nBye bye", name
		

# start by executing the main function
if __name__ == '__main__':
	main()
# random greeting

import random

def main():
	name = raw_input("What's your name?\n>> ")
	greet(name)

def greet(name):
	greetings = ['hello', 'hi', 'howdy', 'hey', 'hiya', 'ciao', 'aloha']
	randomIndex = random.randint(0, len(greetings) - 1)
	greeting = greetings[randomIndex]
	print greeting, name

# start by executing the main function
if __name__ == '__main__':
	main()
# using a function to say hello

def main():
	name = raw_input("What's your name?\n>> ")
	greet(name)

def greet(name):
	print "hello, ", name

# start by executing the main function
if __name__ == '__main__':
	main()

# start by executing the main function
if __name__ == '__main__':
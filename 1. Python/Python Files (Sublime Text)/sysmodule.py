import sys

def printData():
	print(sys.argv)

def printSum():
	print(int(sys.argv[1]) + int(sys.argv[2]))

# printData()
# printSum()

# print(sys.version) # ==> Version of Python
# print(sys.path) # Interpreter will search for packages in all these paths
print(sys.maxsize)
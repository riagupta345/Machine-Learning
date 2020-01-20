
if __name__ == '__main__':
	# What to do when module is run directly
	print("M1 name is %s"%__name__)

else:
	# What to do when module is imported
	print("Inside M1's else block")

# When __name__ is __main__ ==> it means that module is currently running
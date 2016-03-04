error = True

while error == True:
	number = input("What number should I double? ")
	
	try:
		number = float(number)
		# print("double that is {}.".format(number * 2))
		# BUT try block is only for exception causes
	except ValueError:
		print("Sorry, that's not a number.")
		error = True
		# exit()

	else:
		print("Double that is {}.".format(number * 2))
		error = False
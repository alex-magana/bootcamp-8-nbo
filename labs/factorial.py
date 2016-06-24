def factorial(number):
	product = 1
	while number > 0:
		product *= number
		number -= 1
	return product
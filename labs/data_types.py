def data_type(n):
	if type(n) is str:
		return len(n)
	elif type(n) is None:
		return "no value"
	elif (n == True) or (n == False):
		return n
	elif type(n) is int:
		if n > 100:
			return 'greater than 100'
		elif n < 100:
			return 'less than 100'
		else:
			return 'equal to 100'
	elif type(n) is list:
		my_array = n
		third_element = my_array[3]
		if type(third_element) is None:
			return 'nil'
		else:
			return third_element


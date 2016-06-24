def reverse_string(string):
	new_string = string[::-1]
	if new_string == string:
		return True
	else:
		return new_string

print reverse_string("Little")
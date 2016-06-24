def string_length(parameter_val):
	length_list = []
	if type(parameter_val) is list:
		for str_idx in parameter_val:
			length_list.append(len(str_idx))
	elif type(parameter_val) is str:
		length_list.append(len(parameter_val))
	return length_list

print string_length(["Mercury", "Venus"])
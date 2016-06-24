def find_missing(list_a,list_b):
	if list_a == [] or list_b == []:
		return 0
	elif list_a != list_b: 
		return abs(sum(list_a) - sum(list_b))
	else:
	  if list_a == list_b:
	    return 0
	
print find_missing([1,2,3],[1,2,3,4])
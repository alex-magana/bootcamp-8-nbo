def returnPrime(n):
	listPrime = []
	if n <= 0:
		return "None"
	elif n == 1:
		listPrime.append(2)
	else:
		listPrime.append(2)
		curr_num = 3
		while len(listPrime) != n:
 			isPrime = True
			for num in listPrime:
				if curr_num % num == 0:
					isPrime = False
					break
			
			if isPrime:
				listPrime.append(curr_num)
				curr_num += 2
				
	return listPrime

print returnPrime(2)
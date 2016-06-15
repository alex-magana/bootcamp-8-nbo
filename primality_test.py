def returnPrime(n):
	if n <= 0:
		return "None"
	elif n == 1:
		listPrime = [2]
		return listPrime
	else:
		listPrime = [2]
		x = listPrime[len(listPrime) - 1] + 1
		if x % 2 == 0:
			x += 1
		count = 1
		while count < n:
			for num in listPrime:
				if x % num == 0:
					break
			else:
				listPrime.append(x)
				x += 2
				count += 1
				
		return listPrime

print returnPrime(3)
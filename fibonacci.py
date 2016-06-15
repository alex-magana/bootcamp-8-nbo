def buildFibonacci(position):
	fibonacci = [0, 1]
	length = position
	while len(fibonacci) < length:
		fibonacci.insert(len(fibonacci), (fibonacci[len(fibonacci) - 1] + fibonacci[len(fibonacci) - 2]))
	#return fibonacci[len(fibonacci) - 1]
	return fibonacci
	
print buildFibonacci(7)
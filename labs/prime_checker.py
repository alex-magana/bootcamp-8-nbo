class PrimeChecker(object):
	def __init__(self, num=''):
		self.number = num

	def is_prime(self):
		try:
			n = int(self.number)
			if n < 2:
				return False
			elif n == 2:
				return True
			else:
				for num in range(2, n):
					if n % num == 0:
						return False
						break
				else:
					return True	
		except ValueError:
			return False

prime = PrimeChecker('1000')
print prime.is_prime()




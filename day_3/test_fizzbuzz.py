import unittest
import fizzbuzz 
#OR
#from fizzbuss import fizz_buzz

class FizzBuzzTest(unittest.TestCase):
	""" Testing fizzbuzz
	"""

	def test_returns_fizz_when_divisible_by_three(self):
		""" Test returns fizz when input is 
		divisible by three 
		"""
		self.assertEqual(fizzbuzz.fizz_buzz(3), "fizz")

	def test_returns_fizz_when_divisible_by_five(self):
		""" Test returns fizz when input is 
		divisible by five 
		"""
		self.assertEqual(fizzbuzz.fizz_buzz(5), "buzz")

	def test_returns_fizz_when_divisible_by_three_and_five(self):
		""" Test returns fizz when input is 
		divisible by both three and five 
		"""
		self.assertEqual(fizzbuzz.fizz_buzz(15), "fizzbuzz")
from flask import Flask
from primality_test import returnPrime

app = Flask(__name__)

@app.route('/')
def hundred_primes():
	return str(returnPrime(4))


@app.route('/<int:n>', methods = ['GET'])
def get_first_n_primes(n):
	return str(returnPrime(n))

if __name__ == '__main__':
	app.run(debug=True)


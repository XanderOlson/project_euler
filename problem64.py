"""
Project Euler - Problem 64

Odd period square roots
"""
import math
import time

def main():
	result = 0
	n = 10000
	start = time.time()
	breaker = False
	for i in xrange(2, n):
		a0 = int(math.floor(i ** 0.5))
		
		if a0 ** 2 == i:
			continue

		"""
		http://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Continued_fraction_expansion
		"""
		period = 0
		d = 1
		m = 0
		a = a0
		# loop through to find period of continued fraction
		while a != 2 * a0:
			m = d * a - m
			d = (i - m * m) / d
			a = (a0 + m) / d
			period += 1

		if period % 2:
			result += 1

	print result

	
if __name__ == '__main__':
	main()
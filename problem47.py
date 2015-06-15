"""
Project Euler - Problem 47

Distinct Primes Factors
"""

import primes as p

def problem47(n):
	stepper = 0
	for i in xrange(1,n):
		check = len(p.prime_fact_distinct(i))
		if check == 4:
			stepper += 1
			if stepper == 4:
				return i - 3
		else:
			stepper = 0
	
	return None


if __name__ == '__main__':
	print problem47(200000)
"""
Project Euler - Problem 43

Sub-string Divisibility
"""

import itertools
import math


DIGITS = '0123456789'
PRIMES = [2,3,5,7,11,13,17]

def createpandigital():
	return [''.join(e) for e in itertools.permutations(DIGITS,10)]


def problem43():
	results = []
	panlist = createpandigital()
	for e in panlist:
		checker = True
		for i in range(0,7):
			if int(e[i+1:i+4]) % PRIMES[i] != 0:
				checker = False

		if checker:
			results.append(float(e))
	
	return sum(results)

if __name__ == '__main__':
	print problem43()
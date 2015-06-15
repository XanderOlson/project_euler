"""
Project Euler - Problem 72

Counting Fractions
"""

import primes as p
import time
from fractions import gcd

def euler_totient(n):
	pset = p.prime_fact_distinct(n)
	totient = n * 1.0
	for e in pset:
		if e != 1:
			totient *= (1 - 1.0/e)
	return totient

def problem72(n):
	primelist = p.primes2(n)
	primeset = set(primelist)
	total = 0
	for i in xrange(2,n+1):
		if i in primeset:
			t = i - 1
		else:
			t = int(euler_totient(i))
		total += t

	return int(total)

if __name__ == '__main__':
	start = time.time()
	print problem72(10**6)
	print time.time() - start
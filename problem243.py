"""
Project Euler - Problem 243

Resilience
"""


"""
NOTES:
Euler's Totient
"""

import primes as p
import time

def euler_totient(n):
	pset = p.prime_fact_distinct(n)
	totient = n * 1.0
	for e in pset:
		if e != 1:
			totient *= (1 - 1.0/e)
	return totient

def problem243(n):
	breaker = 15499./94744
	starter = 2*3*5*7*11*13*17*19*23
	for i in xrange(1,n):
		starter *= 2
		t = euler_totient(starter)
		denominator = starter - 1.0
		if t / denominator < breaker:
			return starter
	return starter, t/(starter-1), breaker

if __name__ == '__main__':
	start = time.time()
	print problem243(1000)
	print time.time() - start
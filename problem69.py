"""
Project Euler - Problem 69

Totient Maximum
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

def problem69(n):
	result = [0,0]
	for i in range(2,n,2):
		t = euler_totient(i)
		if t == 0:
			print i
		if i/t > result[0]:
			result[0] = i/t
			result[1] = [i]
	return result


if __name__ == '__main__':
	start = time.time()
	print problem69(1000000)
	print time.time() - start
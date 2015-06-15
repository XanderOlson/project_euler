"""
Project Euler - Problem 73

Counting Fractions in a range
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

def problem73approx(n):
	x = 0.
	for i in xrange(2,n):
		t = euler_totient(i)
		x += (t/2. - t/3.)
	return x

def problem73brute(n):
	result = 0
	for i in xrange(2,n):
		for j in xrange(1,i):
			if gcd(i,j) == 1:
				t = j*1./i
				if t < .5 and t>(1./3):
					result += 1
	return result

if __name__ == '__main__':
	n = 12001
	print problem73brute(n)
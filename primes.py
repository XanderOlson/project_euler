"""
Prime Numbers
"""
import numpy as np
import math

def primes2(n):
	# http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
	""" Input n>=6, Returns a list of primes, 2 <= p < n """
	correction = (n%6>1)
	n = {0:n,1:n-1,2:n+4,3:n+3,4:n+2,5:n+1}[n%6]
	sieve = [True] * (n/3)
	sieve[0] = False
	for i in xrange(int(n**0.5)/3+1):
		if sieve[i]:
			k=3*i+1|1
			sieve[((k*k)/3)::2*k]=[False]*((n/6-(k*k)/6-1)/k+1)
			sieve[(k*k+4*k-2*k*(i&1))/3::2*k]=[False]*((n/6-(k*k+4*k-2*k*(i&1))/6-1)/k+1)
	return [2,3] + [3*i+1|1 for i in xrange(1,n/3-correction) if sieve[i]]

def primesnp(n):
	# http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
	""" Input n>=6, Returns a array of primes, 2 <= p < n """
	sieve = np.ones(n/3 + (n%6==2), dtype=np.bool)
	sieve[0] = False
	for i in xrange(int(n**0.5)/3+1):
		if sieve[i]:
			k=3*i+1|1
			sieve[      ((k*k)/3)      ::2*k] = False
			sieve[(k*k+4*k-2*k*(i&1))/3::2*k] = False
	return np.r_[2,3,((3*np.nonzero(sieve)[0]+1)|1)]

def is_prime(n):
	"""Returns True if the number is prime"""
	if n == 2:
		return True
	if n%2 == 0 or n <= 1:
		return False
	sqr = int(math.sqrt(n)) + 1
	for divisor in range(3, sqr, 2):
		if n%divisor == 0:
			return False
	return True

def prime_fact_distinct(n):
	"""Returns a set of distinct prime factors"""
	i = 2
	distinct = set()
	while i*i <= n:
		while n%i == 0:
			n = n/i
			if i not in distinct:
				distinct.add(i)
		i += 1
	distinct.add(n)
	return distinct


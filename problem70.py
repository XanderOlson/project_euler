"""
Project Euler - Problem 70

Totient Permuation
"""

import primes as p
import itertools as it
import time

def euler_totient(n):
	pset = p.prime_fact_distinct(n)
	totient = n * 1.0
	for e in pset:
		if e != 1:
			totient *= (1 - 1.0/e)
	return totient

def problem70(n):
	primelist = p.primesnp(n)
	primeset = set(primelist)
	timer = time.time()
	min_tot = [n,0]
	for i in xrange(1,len(primelist)):
		x = primelist[i]
		for y in xrange(i,len(primelist)):
			a = x*primelist[y]
			if a < n and a> n/2:
				t = int(euler_totient(a))
				if (a* 1.0) / t < min_tot[0]:
					for e in it.permutations(str(a)):
						f = ''.join(e)
						if str(t) == f:
							min_tot[0] = (a*1.0)/t
							min_tot[1] = a
							break
			else:
				break
			
			if time.time() - timer > 600:
				return a,t,"OW", min_tot
	return min_tot

if __name__ == '__main__':
	print problem70(10**7)
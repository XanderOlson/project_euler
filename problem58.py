"""
Project Euler - Problem 58

Spiral Primes
"""
import time
import math
import primes as p

def spriral(n,primes):
	fraction = 1.0
	result = [0.0,0]
	total = 1
	prior = 1
	p_count = 0
	z = 0
	for i in xrange(3,n,2):
		total +=4
		for t in xrange(0,4):
			if t % 4 == 0:
				z +=2
			prior += z
			if prior in primes:
				p_count +=1
			elif prior > 100000000:
				if p.is_prime(prior):
					p_count +=1
					primes.add(prior)
		fraction = 1.*p_count/total

		if fraction < 0.1:
			result = [fraction,i]
			break

	result = [fraction,i]
	return result , prior, z , len(primes)
	
def problem58(n):
	primes = set(p.primes2(10000**2))
	return spriral(n, primes)

if __name__ == '__main__':
	print problem58(100000)
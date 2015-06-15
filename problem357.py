"""
Project Euler - Problem 357

Prime generating integers
"""

import primes as p
import time

def factors(n):
    factorlist = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            factorlist.append(i)
    return factorlist

def problem357(n):
	start = time.time()
	pset = set(p.primes2(n))
	quickset = set()
	results = set()
	for e in pset:
		quickset.add(e-1)

	counter = 0
	for j in quickset:
		if 2+(j/2) in pset:
			t = factors(j)
			breaker = True
			for k in t:
				if k in pset:
					breaker = False
					break
			if breaker:
				results.add(j)
		counter += 1
		if time.time() - start >240:
			return "TOOO LONG", len(pset) - counter

	timer = time.time() - start
	return sum(results), timer

if __name__ == '__main__':
	print problem357(100000001)
	# print realfactor(4)


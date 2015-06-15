"""
Project Euler - Problem 77

Prime Summations
"""

import primes as p

def problem76(n):
	prior_k = []
	sopf_table = []
	ident = set([1])
	for i in xrange(1,n):
		if i == 1:
			sopf = 0
		else:
			sopf = sum(p.prime_fact_distinct(i) - ident)
		sopf_table.append(sopf)
		x = 0
		for j in xrange(1,i):
			x += prior_k[i-j-1] * sopf_table[j-1]
		
		k_n = (sopf + x)*1. / i
		if k_n >= 5000:
			return k_n,i
		prior_k.append(k_n)
	
	return prior_k

if __name__ == '__main__':
	print problem76(100)



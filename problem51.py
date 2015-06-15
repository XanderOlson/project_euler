"""
Project Euler - Problem 51

Prime Digit Replacements
"""

import primes as p

def problem51(n):
	primeset = set(p.primes2(n*10))
	for i in xrange(1001,n,2):
		if i%5 != 0:
			x = list(str(i))
			for j in xrange(0,len(x)-1):
				if j > 0:
					for k in xrange(0,j):
						for l in xrange(0,k):
							x = list(str(i))
							counter = 0
							for m in xrange(0,10):
								x[j] = str(m)
								x[k] = str(m)
								x[l] = str(m)
								y = int(''.join(x))
								if x[0] != '0' and y in primeset:
									counter += 1
			if counter >=8:
				return i,x,j,k,counter
	return "HERE BE DRAGONS"

if __name__ == '__main__':
	print problem51(10000000)
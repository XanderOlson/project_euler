"""
Project Euler - Problem 71

Ordered Fractions
"""
import time
import math

def problem71(n):
	best = [0,0,0]
	for i in xrange(1,(n/7)+1):
		x = (3*i-1.) / (7 * i)

		if x > best[0]:
			best[0] = x
			best[1] = 3*i - 1.
			best[2] = 7*i
	return best

if __name__ == '__main__':
	start = time.time()
	print problem71(1000000)
	print time.time() - start
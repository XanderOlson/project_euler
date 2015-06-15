"""
Project Euler - Problem 74

Digit Factorial Chains
"""

import math
import time

FACT = [1,1,2,6,24,120,720,5040,40320,362880]

def problem74(n):

	# create breakers for loops
	checker = {}
	checker[145] = 1
	checker[169] = 3
	checker[871] = 2
	checker[872] = 2
	checker[45361] = 2
	checker[45362] = 2
	checker[363601] = 3
	checker[1454] = 3

	result = 0
	for i in xrange(2,n):
		x = 1
		t = i
		while True:
			words = str(t)
			t = 0
			for e in words:
				t += FACT[int(e)]
			if t in checker:
				x += checker[t]
				break
			if x >60:
				break
			x += 1			
				
		if x == 60:
			result += 1

	return result

if __name__ == '__main__':
	start = time.time()
	print problem74(10**6)
	print time.time() - start



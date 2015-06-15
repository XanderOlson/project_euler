"""
Project Euler - Problem 26

Reciprocal cycles
"""

import re

def steps(t):
	power = [10**len(str(t))]
	next = power[0]
	step = 0
	while True:
		step +=1
		next = next % t
		if next*10 in power or next == 0:
			return step
		else:
			next *= 10
			power.append(next)

		if step >1000:
			return 0


def problem26(n):
	result = [0,0]
	for i in xrange(1,n):
		t = steps(i)
		if t > result[0]:
			result = [t,i]
				
	return result

if __name__ == '__main__':
	print problem26(1001)
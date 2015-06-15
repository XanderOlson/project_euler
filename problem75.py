"""
Project Euler - Problem 75

Singular Integer Right Triangles
"""

import time
from fractions import gcd
import math

def problem75(n):
	squares = {}
	for i in xrange(1,n):
		squares[i**2] = i
	result = set()
	badset = set()
	for a in range(1,int(n/2)):
		for b in range(1,min(a,n/3)):
			c = a**2 + b**2
			if c in squares:
				x = a + b + squares[c]
			
				if (x > n) or (x in badset):
					break
				elif x in result:
					badset.add(x)
				else:
					result.add(x)
	
	return (len(result) - len(badset))

def problem75tester(n):
	start = time.time()
	result = {}
	count = 0
	for i in xrange(1,int(math.sqrt(n/2))):
		for j in xrange(1,i):
			if (i - j) % 2 == 1 and gcd(i,j) == 1:
				a = (i**2 - j**2)
				b = (2*i*j)
				c = (i**2 + j**2)
				x = a+b+c
				for k in xrange(0,n):
					t = k*x
					if t > n:
						break
					if t in result:
						result[t] +=1
					else:
						result[t] = 1
	for e in result:
		if result[e] == 1:
			count +=1
	return count





if __name__ == '__main__':
	start = time.time()
	print problem75tester(1500000)
	print time.time()-start

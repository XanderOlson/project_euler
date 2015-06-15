"""
Project Euler - Probelm 62

Cubic Permutations
"""

import itertools
import time

def problem62(x,n):
	cubelist = []
	start = time.time()
	for i in xrange(x,n):
		cubelist.append(i**3)

	for e in xrange(0,n-x):
		t = str(cubelist[e])
		counter = 0
		for f in cubelist[e:]:
			if t != str(f):
				if len(str(f)) > len(t):
					break
				elif len(str(f)) == len(t):
					if sorted(str(f)) == sorted(t):
						counter+=1
		if counter == 4:
			return t

		if time.time() - start >600:
			return "SHIIIIIIIIT"
	return time.time()-start

if __name__ == '__main__':
	print problem62(10**3,10**5)


"""
Project Euler - Problem 87

Prime Power Triples
"""

import primes as p
import time

def problem87(n):
	start = time.time()
	plist = p.primes2(n)
	square_set = set()
	cube_set = set()
	four_set = set()
	print time.time()-start, "prime creation time"
	#create sets
	for e in plist:
		if e <= 85:
			square_set.add(e**2)
			cube_set.add(e**3)
			four_set.add(e**4)
		elif e<= 369:
			square_set.add(e**2)
			cube_set.add(e**3)
		elif e<= 7072:
			square_set.add(e**2)
	results = set()
	for a in four_set:
		for b in cube_set:
			for c in square_set:
				d = a + b + c
				if d <= 50000000:
					results.add(d)

				if time.time() - start >30:
					return 'TOOOOO LOOOONG', counter

	return len(results)

if __name__ == '__main__':
	print problem87(7072) #7071 = Sqrt(50,000,000)
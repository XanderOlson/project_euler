"""
Project Euler - Problem 49

Prime Permutations
"""

import primes as p
import itertools

def create_permuation(n):
	return [''.join(e) for e in itertools.permutations(n,4)]

def problem49(n):
	primelist = p.primesnp(n)
	for e in primelist:
		if len(str(e)) == 4:
			hello = create_permuation(str(e))
			for t in hello:
				if e != int(t) and e != 1487:
					z = (int(t) - e) + int(t)
					if str(z) in hello and int(t) in primelist and z in primelist:
						return e, t, z
	return None

if __name__ == '__main__':
	print problem49(10000)
"""
Project Euler - Problem 50

Consecutive prime sums
"""

import primes as p

def problem50(n):
	plist = p.primes2(n)
	xlist = set(plist)
	tlist = plist
	
	current_max = [0,0]
	for e in plist:
		total = 0
		steps = 0
		for t in tlist:
			total += t
			steps += 1
			if total in xlist and steps > current_max[1]:
				current_max = [total,steps]
			if total > n or t > n / 20:
				break
		tlist = tlist[1:]
		xlist.remove(e)
		if e > n / 20:
			break
	return current_max

if __name__ == '__main__':
	print problem50(1000000)
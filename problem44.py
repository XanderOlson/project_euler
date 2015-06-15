"""
Project Euler - Problem 44

Pentagon Numbers
"""

def problem44(n):
	pents = set()
	for i in xrange(1,n):
		p = (i*(3*i-1)/2)
		pents.add(p)
		for n in pents:
			if p-n in pents and p-2*n in pents:
				return p-2*n
	return None

if __name__ == '__main__':
	print problem44(10000)
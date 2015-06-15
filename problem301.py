"""
Project Euler - Problem 301

Nim
"""

def nim(heaps, misere=False):
	"""
	Computes next move for Nim in a normal or misere (default) game, returns tuple (chosen_heap, nb_remove)
	"""
	X = reduce(lambda x,y: x^y, heaps)
	if X == 0: # Will win unless all non-empty heaps have size one
		if max(heaps) > 1:
			return 1
	else:
		return 0

def problem301(n):
	counter = 0
	for i in xrange(1,n+1):
		counter+= nim([i,2*i,3*i])
	return counter

if __name__ == '__main__':
	print problem301(2**30)
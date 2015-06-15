"""
Project Euler - Problem 78

Coin Partitions
"""
import time

def generate_partition(n):
	#PARTITIONS
	p = [1]*(n + 1)

	for i in xrange(1, n + 1):
		j, k, s = 1, 1, 0
		while j > 0:
			j = i - (3 * k * k + k) // 2
			if j >= 0:
				s -= (-1) ** k * p[j]
			j = i - (3 * k * k - k) // 2
			if j >= 0:
				s -= (-1) ** k * p[j]
			k += 1
		p[i] = s

	return p

def problem78(x,n):
	t = generate_partition(n)
	for i in xrange(x,n):
		if t[i] % 1000000 == 0:
			return i, t[i]

	return "DRAGONS"

if __name__ == '__main__':
	start = time.time()
	print problem78(10**4,10**5)
	print time.time() - start
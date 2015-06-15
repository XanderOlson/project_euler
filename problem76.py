"""
Project Euler - Problem 76

Counting Summations
"""


def problem76(n):
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

	return p[n] - 1

if __name__ == '__main__':
	print problem76(100)

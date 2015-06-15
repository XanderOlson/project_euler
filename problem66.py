"""
Project Euler - Problem 66

Diophantine Equation
"""

def problem66(n):
	result = 0
	pmax = 0

	for D in xrange(2, 1000):
		a0 = int(D ** 0.5)
		if a0 ** 2 == D:
			continue
		m = 0
		d = 1
		a = a0

		numer1 = 1
		numer = a

		denom1 = 0
		denom = 1

		while (numer ** 2 - D * (denom ** 2) != 1):
			m = d * a - m
			d = (D - m ** 2) / d
			a = (a0 + m) / d

			numer2 = numer1
			numer1 = numer
			denom2 = denom1
			denom1 = denom

			numer = a * numer1 + numer2
			denom = a * denom1 + denom2

		if numer > pmax:
			pmax = numer
			result = D

	return result

if __name__ == '__main__':
	print problem66(1000)
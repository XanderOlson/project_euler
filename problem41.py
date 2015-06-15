"""
Project Euler - Problem 41

Pandigital Prime
"""
import primes as p
import math
import itertools

DIGITS = [x for x in range(1,10)]

def is_prime(n):
    if n == 2:
        return True
    if n%2 == 0 or n <= 1:
        return False
    sqr = int(math.sqrt(n)) + 1
    for divisor in range(3, sqr, 2):
        if n%divisor == 0:
            return False
    return True

def createpandigital():
	results = []
	for i in [2,4,7]:
		for e in itertools.permutations(DIGITS[:i],i):
			num = ''
			for t in e:
				num = num + str(t)
			results.append(int(num))
	return results

def problem41():
	large = 0
	pandigital = createpandigital()

	for i in pandigital:
		if is_prime(i):
			large = i
	return large

if __name__ == '__main__':
	print problem41()
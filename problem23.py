"""
Project Euler - Problem 23

Non-abundant sums
"""
import math

def divisorGen(n):
	div = set()
	for i in xrange(1,int(math.sqrt(n) + 1)):
		if n % i == 0:
			div.add(i)
			if n / i != n:
				div.add(n/i)
	if sum(div) > n:
		return True
	return False

def abundance(n):
	results = set()
	for i in xrange(n):
		if divisorGen(i):
			results.add(i)
	return results

def problem23(n):
	abund = abundance(n)
	abundant_sums = set()
	for e in abund:
		for t in abund:
			if e+t > 28123:
				break
			if e+t not in abundant_sums:
				abundant_sums.add(e+t)
	
	non_sums = set()
	for i in xrange(28123):
		if i not in abundant_sums:
			non_sums.add(i)
	return sum(non_sums)

if __name__ == '__main__':
	print problem23(28113)
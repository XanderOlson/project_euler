"""
Project Euler - Problem 80

Square Root Digital Expansion
"""

from decimal import *
import math

SQUARES = set([1,4,9,16,25,36,49,64,81,100])

def problem80(n):
	getcontext().prec = 102
	totals = []
	for i in xrange(1,n):
		if i not in SQUARES:
			t = str(Decimal(i).sqrt())
			counter = 0
			total = 0
			for j in t[:101]:
				if j != '.':
					counter += 1
					total += int(j)
				if counter >= 100:
					break
			totals.append(total)
	return sum(totals)

if __name__ == '__main__':
	print problem80(100)
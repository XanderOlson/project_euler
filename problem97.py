"""
Project Euler - Problem 97

Large non-Mersenne Prime
"""

import time

def problem97(n):
	start = time.time()
	power_num = 2
	z = 1
	while z < n:
		power_num *= 2
		power_num = power_num % 10000000000
		z += 1
		if time.time() - start > 30:
			print "TOOOOO LOONG",n

	power_num *= 28433
	power_num += 1
	power_num = power_num % 10000000000

	return power_num

if __name__ == '__main__':
	print problem97(7830457)
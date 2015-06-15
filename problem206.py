"""
Project Euler - Problme 206

Concealed Square
"""

import itertools as it
import time

DIGITS = '1234567890'
#DIGITS2 = '1[0-9]0'

def problem206(x,n):
	start = time.time()
	while x<n :
		t = str(x**2)
		if t[::2] == DIGITS:
			return x,t
		if x % 100 == 30:
			x += 40
		else:
			x += 60
		if time.time() - start > 60:
			return "AWWWW SHIIIIIT"
	return 'DRAGONS'

if __name__ == '__main__':
	print problem206(1010101030,1389026623)
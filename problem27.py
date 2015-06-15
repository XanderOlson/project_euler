"""
Project Euler - Problem 27

Quadratic Primes
"""

import primes as p

def problem27(n):
	blist = p.primesnp(n)
	counter = [0,0,0]
	for a in range(-n + 1,n):
		for b in blist:
			stepper = 0
			t = 0
			while p.is_prime((t**2) + (a*t) + b):
				stepper += 1
				t += 1
			
			if stepper > counter[0]:
				counter = [stepper,a,b]
	
	return counter, counter[1]*counter[2]

if __name__ == '__main__':
	print problem27(1000)
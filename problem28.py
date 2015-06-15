"""
Project Euler - Problem 28

Number spiral diagonals
"""
import math

def spiral(n):
	total = 1
	prior = 1
	t = 0
	for i in range(0,int(n/2)*4):
		if i % 4 == 0:
			t +=2
		prior += t
		total += prior
	return total
	
def problem28(n):
	print spiral(n)

if __name__ == '__main__':
	problem28(1001)


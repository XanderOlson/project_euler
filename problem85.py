"""
Project Euler - Problem 85

Counting Rectangles
"""

import math

def count_rectangles(m,n):
	counter = 0
	for i in range(m,0,-1):
		for j in range(n,0,-1):
			z = (n-j+1) * (m-i+1)
			counter += z
	return counter

def find_closest_square(x,y):
	for k in xrange(x,y):
		z = count_rectangles(k,k)
		if z > 2000000:
			return k,z
	return k,z

def problem85(square,interval):
	cur_min= [1000000,0,0]
	starter = square - interval
	for x in xrange(0,interval):
		for y in xrange(0,(2*interval)-x):
			z = abs(2000000-count_rectangles(starter+x,starter+((2*interval)-y)))
			if z < cur_min[0]:
				cur_min[0] = z
				cur_min[1] = starter+x
				cur_min[2] = starter+((2*interval)-y)
	return cur_min[0], cur_min[1]*cur_min[2]

if __name__ == '__main__':
	starter,z = find_closest_square(10**1,10**2) 
	#returns 53 x 53
	#iterate around 53
	print problem85(starter,40)
	
	



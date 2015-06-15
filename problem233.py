"""
Project Euler - Problem 233

Lattice points on a circle
"""

import math

def schinzel(n):
	"""http://mathworld.wolfram.com/SchinzelCircle.html"""
	if n % 2:
		k = (n - 1) / 2
	else:
		k = n // 2

	

def lattice_points(n):
	center = n * 0.5
	# use pythagorean theorem to find radius
	# a ^ 2 + b ^ 2 = c ^ 2
	# since it is a square a = b
	radius = math.sqrt(center ** 2 + center ** 2)



def main():
	"""Problem 233"""


if __name__ == '__main__':
	main()
"""
Project Euler - Problem 86

Cuboid Routes
"""
import math 

def main():
	counter = 0
	length = 2
	maximum = 1000000
	root = 0.0
	while counter < maximum:
		length += 1
		for yz in range(3, 2 * length + 1):
			root = math.sqrt(yz ** 2 + length ** 2)
			if root == int(root):
				if yz <= length:
					counter += yz / 2
				else:
					counter += 1 + (length - (yz + 1) / 2)

	print length
	print counter, yz


if __name__ == '__main__':
	main()
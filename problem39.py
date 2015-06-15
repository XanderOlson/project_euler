"""
Project Euler - Problem 39

Integer Right Triangles
"""
import math

def psolutions(p):
	results = []
	for i in range(1,p):
		for j in range(1,p):
			if j not in results:
				if i + j + math.sqrt(i**2 + j**2) == p:
					results.append(i)

	return len(results)

def problem39():
	counter = 0
	maxi = 0
	for i in range(1,1001):
		t = psolutions(i)
		if t > counter:
			counter = t
			maxi = i

	return maxi, counter

if __name__ == '__main__':
	print problem39()
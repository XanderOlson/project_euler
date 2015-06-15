"""
Project Euler - Problem 63

Powerful Digit Counts
"""

def problem63(n):
	numberset = [1,2,3,4,5,6,7,8,9]
	counter = 0
	for i in xrange(4,10):
		for j in xrange(1,n):
			x = i**j
			if len(str(x)) == j and x not in numberset:
				numberset.append(x)
				counter+=1
			if len(str(x))< j:
				break
	return counter, len(numberset)

if __name__ == '__main__':
	print problem63(50)
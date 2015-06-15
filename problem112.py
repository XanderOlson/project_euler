"""
Project Euler - Problem 112

Bouncy Numbers
"""

def problem112(n):
	x = 0
	t = 0

	while x < n + 1:
		up,down = 1,1
		y = str(x)
		z = len(y)
		if z >= 3:
			for e in xrange(1,z):
				if y[e] >= y[e-1]:
					up += 1
				if y[e] <= y[e-1]:
					down +=1
			if up !=z and down != z:
				t += 1.
		x +=1
		

	return t/n

if __name__ == '__main__':
	print problem112(1587000)
"""
Project Euler - Problem 30

Digit Fifth Powers
"""

def power_sum(n,p):
	digits = str(n)
	t = 0
	for e in digits:
		t+= int(e)**p

	if t == n:
		print t
		return n
	else:
		return 0

def problem30():
	z = 0
	#6 digits maximum (7*(9**5)) < 9999999
	for i in range(10,1000000):
		z += power_sum(i,5)
	return z

if __name__ == "__main__":
	print problem30()
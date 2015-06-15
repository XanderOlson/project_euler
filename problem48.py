"""
Project Euler - Problem 48

Self Powers
"""

def problem48():
	result = 0
	modder = 10**10
	for i in range(1,1001):
		result += i**i % modder
		result = result % modder

	return result

if __name__ == '__main__':
	print problem48()
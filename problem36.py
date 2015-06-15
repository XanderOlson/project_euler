"""
Project Euler - Problem 36

Double-base palindromes
"""

def is_palindrome(n):
	if str(n) == str(n)[::-1]:
		return True
	return False

def problem36():
	total = 0
	for i in range(0,1000000):
		if is_palindrome(i) and is_palindrome(int(bin(i)[2:])):
			total += i
	return total

if __name__ == '__main__':
	print problem36()
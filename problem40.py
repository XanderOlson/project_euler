"""
Project Euler - Problem 40

Champernowne's Constant
"""

def champer(n):
	word = ''
	for i in range(0,n+1):
		word += str(i)
		if len(word) > 1000000:
			break
	return word

def problem40():
	irrational = champer(200000)
	result = 1
	for i in [1,10,100,1000,10000,100000,1000000]:
		result = result*int(irrational[i])

	return result
	
if __name__ == '__main__':
	print problem40()
"""
Project Euler - Problem 37

Truncatable Primes
"""
import primes

def truncatable(i,plist):
	word = str(i)
	for i in range(1,len(word)):
		if int(word[i:]) not in plist or int(word[:-i]) not in plist:
			return False
	return True

def problem37(n):
	primelist = primes.primes2(n)
	results = []
	for i in primelist:
		if truncatable(i,primelist) and  i not in [2,3,5,7]:
			results.append(i)
	return sum(results)

if __name__ == '__main__':
	print problem37(1000000)

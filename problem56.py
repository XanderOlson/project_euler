"""
Project Euler - Problem 56

Powerful digit sum
"""

def problem56(n):
	maxsum = [0,0,0]
	for i in range(2,n):
		if i%10 != 0:
			for t in range(2,100):
				summer = 0
				word = str(i**t)
				for e in word:
					summer += int(e)

				if summer > maxsum[0]:
					maxsum = [summer,i,t]

	return maxsum
	
if __name__ == '__main__':
	print problem56(100)
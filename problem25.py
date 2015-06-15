"""
Project Euler - Problem 25

1000-digit Fibonacci number
"""

def find_fib(n):
	a = 1
	b = 1
	for i in range(n):
		a, b = a + b, a
		if len(str(a)) == 1000:
			print i + 3, len(str(a))
			break
	print 'finished running'

def problem25():
	find_fib(10000)

if __name__ == '__main__':
	problem25()

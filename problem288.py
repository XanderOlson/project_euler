"""
Project Euler - Problem 288

Enormous Factorial
"""

def NFmod(p, q, e):
     m = p ** e
     s = 290797
     r = 0
     x = 0
     for n in xrange(q + 1):
         t = s % p
         s = s * s % 50515093
         r = (r + t * x) % m
         if n < e:
             x += p ** n
     return r % m

def problem288():
     return NFmod(61, 10 ** 7, 10)


if __name__ == '__main__':
	print problem288()
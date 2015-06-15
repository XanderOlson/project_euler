"""
Project Euler - Problem 33

Digit Cancelling Fractions
"""

def digit(numer,denom):
	for e in str(numer):
		if e in str(denom) and int(e) != 0:
			s = str(numer).replace(e,"",1)
			t = str(denom).replace(e,"",1)
			if int(t) != 0:
				try:
					if float(s) * 1.0 / float(t) == numer*1.0 / denom:
						return s,t
				except:
					print s,t,numer,denom
	return None

def problem33():
	num,dem = 1,1
	for i in range(10,100):
		for j in range(10,100):
			if digit(i,j) and i!=j and i<j:
				s,t = digit(i,j)
				num *= int(s)
				dem *= int(t)
	return num,dem

if __name__ == "__main__":
	print problem33()
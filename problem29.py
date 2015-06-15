"""
Project Euler - Problem 29

Distinct Powers
"""

def integer_combo(a,b):
	total = set()
	for i in range(2,a+1):
		new_set = set()
		for j in range(2,b+1):
			total = total.union(set([i**j]))
	return len(total)
	
def problem29():
	print integer_combo(100,100)

if __name__ == '__main__':
	problem29()
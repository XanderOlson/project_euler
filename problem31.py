"""
Project Euler - Problem 31

Coin Sums
"""
PENCE = [1,2,5,10,20,50,100,200]

def check_sum(numlist):
	money = sum([a*b for a,b in zip(numlist,PENCE)])
	if money > 200:
		return 2
	elif money == 200:
		return 1
	return 0

def problem31():
	money = 0
	summer = 8
	for i in range(0,2):
		for j in range(0,4):
			for k in range(0,10):
				for l in range(0,20):
					for m in range(0,40):
						for n in range(0,100):
							for o in range(0,200):
								numlist = [o,n,m,l,k,j,i,0]
								money = sum([a*b for a,b in zip(numlist,PENCE)])
								if money > 200:
									break
								elif money == 200:
									summer +=1
	return summer

if __name__ == '__main__':
	print problem31()


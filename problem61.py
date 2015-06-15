"""
Project Euler - Problem 61

Cyclical Figurate Numbers
"""

import math

def create_triangle(n):
	triag = []
	for i in xrange(n):
		t = i*(i+1)/2
		if len(str(t))==4:
			triag.append(t)
		elif len(str(t)) >= 4:
			break
	return triag

def create_square(n):
	squa = []
	for i in xrange(n):
		t = i**2
		if len(str(t))==4:
			squa.append(t)
		elif len(str(t)) >= 4:
			break
	return squa

def create_pent(n):
	pent = []
	for i in xrange(n):
		t = i*(3*i-1)/2
		if len(str(t))==4:
			pent.append(t)
		elif len(str(t)) >= 4:
			break
	return pent

def create_hexa(n):
	hexa = []
	for i in xrange(n):
		t = i*(2*i - 1)
		if len(str(t))==4:
			hexa.append(t)
		elif len(str(t)) >= 4:
			break
	return hexa

def create_hept(n):
	hept = []
	for i in xrange(n):
		t = i*(5*i - 3) / 2
		if len(str(t))==4:
			hept.append(t)
		elif len(str(t)) >= 4:
			break
	return hept

def create_oct(n):
	octa = []
	for i in xrange(n):
		t = i*(3*i-2)
		if len(str(t))==4:
			octa.append(t)
		elif len(str(t)) >= 4:
			break
	return octa

def cleaner(list1,n):
	t = 0
	for i in xrange(0,n):
		if t < len(list1):
			if str(list1[t])[-1] == '0' or str(list1[t])[-2] == '0':
				del list1[t]
				t-= 1
		else:
			break
		t +=1
	return set(list1)

def find_next(x,bigset):
	t = []
	word = str(x)[2:]
	for e in bigset:
		if str(e)[:2] == word:
			t.append(e)
	return t

def problem61(n):
	bigset = set()
	triag = cleaner(create_triangle(n),n)
	square = cleaner(create_square(n),n)
	pent = cleaner(create_pent(n),n)
	hexa = cleaner(create_hexa(n),n)
	hept = cleaner(create_hept(n),n)
	octa = cleaner(create_oct(n),n)
	biglist = [triag,square,pent,hexa,hept,octa]

	#create bigset
	bigset = triag | square | pent | hexa | hept | octa
	
	# create chain
	chains = {}
	for e in bigset:
		end = str(e)[2:]
		t = find_next(e,bigset)
		if end in chains:
			if t:
				chains[end] = set(chains[end]) | set(t)
		else:
			chains[end] = set(t)

	#1 chain
	chainer = []
	for b in bigset:
		for c in chains[str(b)[2:]]:
			for d in chains[str(c)[2:]]:
				for e in chains[str(d)[2:]]:
					for f in chains[str(e)[2:]]:
						for g in chains[str(f)[2:]]:
							if b in chains[str(g)[2:]]:
								if set([b,c,d,e,f,g]) not in chainer:
									spinner = set([b,c,d,e,f,g])
									chainer.append(spinner)

	# check lists
	result = []
	for x in chainer:
		tester = [0 for a in xrange(0,6)]
		if len(x) == 6:
			for y in x:
				for i in xrange(0,6):
					if y in biglist[i]:
						tester[i] += 1

		if sum(tester) >=6:
			count = 0
			for i in xrange(0,6):
				if tester[i] == 0:
					count +=1

			if count == 0:
				result.append([x,tester,sum(x)])


	return result

if __name__ == '__main__':
	print problem61(1000)


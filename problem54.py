"""
Project Euler - Problem 54

Poker Hands
"""

PATH = 'C:\Python27\Project_Euler\\text_files\p054_poker.txt'
CARDS = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
REFERENCE = ['Straight Flush','Four of a Kind','Full House','Flush','Straight','Three','2 Pair','1 Pair','High','High 2']


import csv

def winninghand(dict1,dict2):
	point1, point2 = [0 for x in range(0,13)],[0 for x in range(0,13)]

	#check straight
	point1[4] = return_points_straight(dict1)	
	point2[4] = return_points_straight(dict2)
	
	#check flush
	if len(dict1) == 1:
		point1[3] = 1
		if point1[4] > 0:
			point1[0] = point1[4]
	elif len(dict2) == 1:
		point2[3] = 1
		if point2[4] > 0:
			point2[0] = point2[4]
	
	#check number of cards
	point1[1],point1[5],point1[6],point1[7],point1[8],point1[9],point1[10],point1[11],point1[12] =  common_cards(dict1) 
	point2[1],point2[5],point2[6],point2[7],point2[8],point2[9],point2[10],point2[11],point2[12] =  common_cards(dict2) 

	#check full house
	if point1[5] and point1[7]:
		point1[2] = point1[5]
		point1[5] = 0

	if point2[5] and point2[7]:
		point2[2] = point2[5]
		point2[5] = 0

	for i in range(0,13):
		if point1[i] > point2[i]:
			return 1
		elif point2[i] > point1[i]:
			return 2


def common_cards(dict1):
	kind = [0 for s in range(0,9)]
	x = [0 for t in range(0,13)]
	for t in dict1:
		for i in range(0,13):
			if CARDS[i] in dict1[t]:
				x[i] += 1

	pairs = 0
	counter = 0
	for z in range(0,len(x)):
		if x[z] == 4:
			kind[0] = z + 1
		elif x[z] == 3:
			kind[1] = z + 1
		elif x[z] == 2:
			if pairs == 0:
				kind[3] = z + 1
				pairs = 1
			elif z+1 > kind[3]:
				kind[2] = z + 1
			else:
				kind[2] = kind[3]
				kind[3] = z+1
		elif x[z] == 1:
			counter += 1
			kind[9-counter] = z+1


	return kind[0],kind[1],kind[2],kind[3],kind[4],kind[5],kind[6],kind[7],kind[8]


def return_points_straight(dict1):
	point = 0
	start = 50
	counter = 0
	straight = set()
	for i in dict1:
		for t in dict1[i]:
			z = CARDS.index(t)			
			if z < start:
				start = z
		
	for i in dict1:
		for t in dict1[i]:
			z = CARDS.index(t)			
			straight = straight | set([z])
			counter = counter + (z - start)

	if counter == 10 and len(straight) == 5:
		point = start + 1

	return point

def update_dict(list1,dict1):
	for i in list1:
		key = i[1]
		if key in dict1:
			dict1[key].append(i[0])
		else:
			dict1[key] = [i[0]]
	return dict1

def problem54(n,m):
	with open(PATH, 'rb') as csvfile:
		reader = csv.reader(csvfile)
		win1,win2 = 0,0
		for row in reader:
			words = row[0].split()	
			player1 = words[0:5]
			player2 = words[5:10]
			play1,play2 = {},{}
			play1 = update_dict(player1,play1)
			play2 = update_dict(player2,play2)
			t = winninghand(play1,play2)
			if t == 1:
				win1 += 1
			elif t == 2:
				win2 += 1						
	return win1, win2


if __name__ == '__main__':
	print problem54(0,10)
"""
Project Euler - Problem 67

Maximum Path Sum II
"""

import csv
PATH = 'C:\Python27\Project_Euler\\text_files\p067_triangle.txt'

def problem67():
	weak_matrix = []
	strong_matrix = []
	with open(PATH, 'rb') as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			weak_matrix.append(row)

		for e in weak_matrix:
			strong_matrix.append(e[0].split())

		length = 100
		new_matrix = [[0 for x in xrange(length)] for y in xrange(length)]

		for i in xrange(length - 1,-1,-1):
			for j in xrange(len(strong_matrix[i])-1,-1,-1):
				temp = 0
				if i == 99:
					print "HELLO"
				if (i+1 < length):
					temp = max(new_matrix[i+1][j],new_matrix[i+1][j+1])
				# elif i + 1 < length:
				# 	temp = new_matrix[i+1][j]
				# elif j + 1 < length:
				# 	temp = new_matrix[i+1][j+1]
				else:
					temp = 0
				new_matrix[i][j] = int(strong_matrix[i][j]) + temp
				
	print new_matrix[99]
	return new_matrix[0][0]

if __name__ == '__main__':
	print problem67()
"""
Project Euler - Problem 81

Minimal Path Sum
"""

import csv
PATH = 'C:\Python27\Project_Euler\\text_files\p081_matrix.txt'

def problem81():
	weak_matrix = []
	with open(PATH, 'rb') as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			weak_matrix.append(row)

	length = 80
	new_matrix = [[0 for x in xrange(80)] for y in xrange(80)]
	for i in xrange(79,-1,-1):
		for j in xrange(79,-1,-1):
			temp = 0
			if (i+1 < length) & (j + 1 < length):
				temp = min(new_matrix[i+1][j],new_matrix[i][j+1])
			elif i + 1 < length:
				temp = new_matrix[i+1][j]
			elif j + 1 < length:
				temp = new_matrix[i][j+1]
			else:
				temp = 0
			new_matrix[i][j] = int(weak_matrix[i][j]) + temp


	return new_matrix[0][0]

if __name__ == '__main__':
	print problem81()
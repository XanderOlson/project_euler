"""
Project Euler - Problem 99

Largest Exponential
"""

import csv
import math
PATH = 'C:\Python27\Project_Euler\\text_files\p099_base_exp.txt'

def problem99():
	cur_max = [0,0,0,0]
	counter = 0
	with open(PATH, 'rb') as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			counter += 1
			x = int(row[0])
			y = int(row[1])
			z = math.log(x) * y
			if z > cur_max[0]:
				cur_max[0] = z
				cur_max[1] = x
				cur_max[2] = y
				cur_max[3] = counter
	return cur_max[3]

if __name__ == '__main__':
	print problem99()
			


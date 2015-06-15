"""
Project Euler - Problem 102

Triangle Containment
"""

import csv
import math
PATH = 'C:\Python27\Project_Euler\\text_files\p102_triangles.txt'

def problem102():
	counter = 0
	with open(PATH, 'rb') as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			truearea,checkarea = 0,0
			x1 = int(row[0])
			x2 = int(row[1])
			y1 = int(row[2])
			y2 = int(row[3])
			z1 = int(row[4])
			z2 = int(row[5])

			truearea = (0.5)*abs(((x1-z1)*(y2-x2)) - ((x1-y1)*(z2-x2)))

			for zero in xrange(0,3):
				if zero == 0:
					checkarea += (0.5)*abs(y1*z2 - z1*y2)
				elif zero == 1:
					checkarea += (0.5)*abs(x1*z2 - z1*x2)
				elif zero == 2:
					checkarea += (0.5)*abs(x1*y2 - y1*x2)
			if truearea==checkarea:
				counter+=1

	return counter

if __name__ == '__main__':
	print problem102()
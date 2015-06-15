"""
Project Euler - Problem 42

Coded triangle numbers
"""

PATH = 'C:\Python27\Project_Euler\\text_files\p042_words.txt'

import csv

def createtriangle(n):
	result = []
	for i in xrange(1,n+1):
		result.append((i*(i+1)/2))
	return result

def problem42(n):
	results = []
	triangles = createtriangle(n)
	with open(PATH, 'rb') as csvfile:
		reader = csv.reader(csvfile)
		words = reader.next()

	for e in words:
		number = 0
		for t in e:
			number += ord(t.lower()) - 96

		if number in triangles:
			results.append(number)

	return len(results)

if __name__ == '__main__':
	print problem42(1000)
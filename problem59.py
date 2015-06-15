"""
Project Euler - Problem 59

XOR Decryption
"""

import csv


PATH = 'C:\Python27\Project_Euler\\text_files\p059_cipher.txt'

def problem59(n,m):
	with open(PATH, 'rb') as csvfile:
		reader = csv.reader(csvfile)
		cipher = reader.next()

	for i in range(n,m):
		for j in range(97,123):
			for k in range(97,123):
				result = []
				for e in range(0,len(cipher),3):
					result.append(chr(int(cipher[e]) ^ i))
					if e + 1 < len(cipher):
						result.append(chr(int(cipher[e+1]) ^ j))
					if e + 2 <  len(cipher):
						result.append(chr(int(cipher[e+2]) ^ k))
				text = ''.join(result).lower()
				if text.find('the')>0 and text.find('be')>0 and text.find('that')>0 and text.find('have')>0:
					return text[0:15], sum([ord(e) for e in result])




if __name__ == '__main__':
	print problem59(97,123)
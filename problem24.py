"""
Project Euler - Problem 24

Lexicographic permutations
"""
import itertools

INPUTS = [x for x in range(0,10)]

def nth_permutation(n):
	return next(itertools.islice(itertools.permutations(INPUTS),n-1,None),None)

print nth_permutation(1000000)
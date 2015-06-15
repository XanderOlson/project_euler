"""
Project Euler - Problem 121

Disc game prize fund
"""

def main():
	"""Problem 121"""
	rounds = 15
	possible_outcomes = [0] * (rounds + 1)
	possible_outcomes[rounds] = 1
	possible_outcomes[rounds-1] = 1

	for i in range(2, rounds+1):
		for j in range(rounds):
			possible_outcomes[j] = possible_outcomes[j + 1]

		possible_outcomes[rounds] = 0

		for k in range(rounds, 0, -1):
			possible_outcomes[k] += possible_outcomes[k-1] * i


	positive = sum(possible_outcomes[:8])


	total = 1
	for tot in range(2, rounds + 2):
		total *= tot


	print positive, total, total / positive


	
if __name__ == '__main__':
	main()
"""
Project Euler - Problem 95

Amicable Chains
"""
import primes

def generate_factors(limit):
	sum_of_factors_list = [0] * (limit + 1)
	for i in xrange(1, limit // 2 + 1):
		for j in xrange(2*i, limit + 1, i):
			sum_of_factors_list[j] += i
	return sum_of_factors_list


if __name__ == '__main__':
	limit = 1000000
	result = 0
	chain_length = 0

	prime_list = primes.primes2(limit)
	print "Primes generated..."
	sum_of_factors_list = generate_factors(limit)
	print "Factor sums generated..."

	numbers_bool = [False] * (limit + 1)

	for i in xrange(2, limit + 1):
		if numbers_bool[i]:
			continue
		chain = []

		new_number = i
		broken = False

		while (new_number not in chain):
			chain.append(new_number)
			new_number = sum_of_factors_list[new_number]

			if (new_number > limit) or numbers_bool[new_number]:
				broken = True
				break

		if not broken:
			smallest = max(chain)
			first = chain.index(new_number)

			if len(chain) - first > chain_length:
				for j in range(first, len(chain)):
					if chain[j] < smallest:
						smallest = chain[j]

				chain_length = len(chain) - first
				result = smallest

		for j in range(len(chain)):
			numbers_bool[chain[j]] = True

	print result
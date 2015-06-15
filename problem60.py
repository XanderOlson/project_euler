"""
Project Euler - Problem 60

Prime Pair Sets
"""

import primes as p

def problem60(n):
	startsum = [100000000,[]]
	primes = p.primesnp(n)
	pairs = {}
	t = len(primes)
	primeset = set(p.primes2(n))
	for i in xrange(1,t-1):
		for j in xrange(i+1, t-2):
			word = int(str(primes[i]) + str(primes[j]))
			word2 = int(str(primes[j]) + str(primes[i]))
			if (word in primeset and word2 in primeset):
				if primes[i] in pairs:
					pairs[primes[i]].append(primes[j])
				else:
					pairs[primes[i]] = [primes[j]]
			else:
				if p.is_prime(word) and p.is_prime(word2):
					primeset.add(word)
					primeset.add(word2)
					if primes[i] in pairs:
						pairs[primes[i]].append(primes[j])
					else:
						pairs[primes[i]] = [primes[j]]
	
	print "starting second phase"
	for a in pairs:
		for b in pairs[a]:
			if b in pairs:
				for c in pairs[b]:
					if c in pairs and c in pairs[a]:
						if a + b + c < startsum[0]:
							for d in pairs[c]:
								if d in pairs and d in pairs[a] and d in pairs[b]:
									if a + b + c + d < startsum[0]:
										for e in pairs[d]:
											if e in pairs and e in pairs[a] and e in pairs[b] and e in pairs[c]:
												if a + b + c + d + e < startsum[0]:
													startsum[0] = a + b + c + d + e
													startsum[1] = [a,b,c,d,e]
									else:
										break
						else:
							break

	return startsum


if __name__ == '__main__':
	print problem60(10000)
"""
Project Euler - Problem 57

Square Root Convergents
"""

import math
import itertools

def convergs_gen(qgen, pgen=itertools.repeat(1)):
    """Compute successive convergents for an arbitrary continued fraction.

       q1 + p2/(q2 + p3/(q3 + p4/(q4 + . . .
    """
    Np, Dp, N, D = 0, 1, 1, 0
    for q, p in itertools.izip(qgen, pgen):
        Np, Dp, N, D = N, D, p*Np + q*N, p*Dp + q*D
        yield N, D # Numerator, Denominator


def problem57(n):
    prior_n = 3
    prior_d = 2
    result = 0
    for i in xrange(n):
        new_n = prior_n + 2 * prior_d
        new_d = new_n - prior_d
        prior_n = new_n
        prior_d = new_d
        if len(str(new_n)) > len(str(new_d)):
            result += 1

    return result
		

if __name__ == '__main__':
	print problem57(999)

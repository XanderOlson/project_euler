"""
Project Euler - Problem 91

Right triangles with integer coordinates
"""
import fractions

def main():
	size = 50
	result = 3 * size ** 2
	for x in range(1, size + 1):
		for y in range(1, size + 1):
			factor = int(fractions.gcd(x, y))
			result += min(y * factor / x, (size - x) * factor / y) * 2

	print result


if __name__ == '__main__':
	main()
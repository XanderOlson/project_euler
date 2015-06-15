"""
Project Euler - Problem 94

Almost equilateral triangles
"""

def main():
	x = 2
	y = 1
	upper_limit = 1000000000 # 1 billion
	result = 0

	while True:
		#case 1: b = a + 1
		a_times_3 = 2 * x - 1
		area_times_3 = y * (x - 2)
		if a_times_3 > upper_limit:
			break
		
		if (a_times_3 > 0) & (area_times_3 > 0) & (a_times_3 % 3 == 0) & (area_times_3 % 3 == 0):
			a = a_times_3 / 3
			area = area_times_3 / 3

			result += 3 * a + 1

		#case 2 b = a - 1
		a_times_3 = 2 * x + 1
		area_times_3 = y * (x + 2)

		if (a_times_3 > 0) & (area_times_3 > 0) & (a_times_3 % 3 == 0) & (area_times_3 % 3 == 0):
			a = a_times_3 / 3
			area = area_times_3 / 3

			result += 3 * a - 1

		next_x = 2 * x + y * 3
		next_y = y * 2 + x

		x = next_x
		y = next_y

	print result

if __name__ == '__main__':
	main()
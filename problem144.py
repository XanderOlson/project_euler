"""
Project Euler - Problem 144

Investigating multiple reflections of a laser beam
"""
import math
import time

def main():
	"""Problem 144"""
	result = 0

	xA, yA = 0.0, 10.1
	xO, yO = 1.4, -9.6

	print "starting the loop..."
	# start time
	start = time.time()

	while (xO > 0.01 or xO < -0.01 or yO < 0):
		#calculate the slope of A
		slope_a = (yO - yA) / (xO - xA)

		#calculate the slope of the ellipse tangent
		slope_o = -4 * xO / yO

		#calculate the slope of B
		tan_a = (slope_a - slope_o) / (1 + slope_a * slope_o)
		slope_b = (slope_o - tan_a) / (1 + tan_a * slope_o)

		#calculate intercept of line B
		intercept_b = yO - slope_b * xO

		# solve the quadratic equation for finding
		# the intersection of B and the ellipse
		# ax^2 + bx + c = 0
		a = 4 + slope_b * slope_b
		b = 2 * slope_b * intercept_b
		c = intercept_b * intercept_b - 100

		ans1 = (-b + math.sqrt(b * b - 4 * a * c)) / (2 * a)
		ans2 = (-b - math.sqrt(b * b - 4 * a * c)) / (2 * a)

		xA = xO
		yA = yO

		# take the solution furthest from xO
		if abs(ans1 - xO) > abs(ans2 - xO):
			xO = ans1
		else:
			xO = ans2

		yO = slope_b * xO + intercept_b

		result += 1

		# While loop breaker to catch infinite loops
		if time.time() - start > 60:
			print "ran out of time", result
			break

	print result


if __name__ == '__main__':
	main()


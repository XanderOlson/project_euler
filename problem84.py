"""
Project Euler - Problem 84

Monopoly odds
"""
import random

chance_position = 0
community_chest_position = 0

def chance(current_position):
	global chance_position
	chance = [0, 10, 11, 24, 39, 5]
	chance_position += 1
	chance_position = chance_position % 16
	if chance_position < 6:
		return chance[chance_position]
	elif chance_position in [6 , 7]:
		if current_position == 7:
			return 15
		elif current_position == 22:
			return 25
		elif current_position == 36:
			return 5
	elif chance_position == 8:
		if current_position == 22:
			return 28
		else:
			return 12
	elif chance_position == 9:
		current_position -= 3
		return current_position
	else:
		return None

def community_chest():
	global community_chest_position
	community_chest = [0,10]
	community_chest_position += 1
	community_chest_position = community_chest_position % 16
	if community_chest_position < 2:
		return community_chest[community_chest_position]
	return None


def simulation(n):
	board_locations = [0 for x in range(40)]
	samples = n

	doubles = 0
	current_position = 0
	for i in xrange(samples):
		dice1 = random.randint(1,4)
		dice2 = random.randint(1,4)

		if dice1 == dice2:
			doubles += 1
		else:
			doubles = 0

		if doubles > 2:
			current_position = 10 # GO TO JAIL
		else:
			current_position = (current_position + dice1 + dice2) % 40

			if current_position in [7, 22, 36]:
				x = chance(current_position)
				if x:
					current_position = x
			if current_position in [2, 17, 33]:
				y = community_chest()
				if y:
					current_position = y
			# GO TO JAIL
			if current_position == 30:
				current_position = 10

		board_locations[current_position] = board_locations[current_position] + 1

	total_moves = sum(board_locations)
	for x in range(len(board_locations)):
		board_locations[x] = board_locations[x] * 1.0 / total_moves

	print board_locations
	sorted_board = sorted(board_locations)
	return board_locations.index(sorted_board[-1]), \
			board_locations.index(sorted_board[-2]), \
			board_locations.index(sorted_board[-3])


def main():
	print simulation(1000000)


if __name__ == '__main__':
	main()

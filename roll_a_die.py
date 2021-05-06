import random

Four_corner_die = [1,2,3,4]
six_corner_die = [1,2,3,4,5,6]
eight_corner_die = [1,2,3,4,5,6,7,8]
ten_corner_die = [1,2,3,4,5,6,7,8,9,10]
twelve_corner_die = [1,2,3,4,5,6,7,8,9,10,11,12]
twenty_corner_die = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,10]

def roll_a_die_get(die_face):
	global Four_corner_die
	global six_corner_die
	global eight_corner_die
	global ten_corner_die
	global twelve_corner_die
	global twenty_corner_die

	if die_face == '4':
		return random.choice(Four_corner_die)
	elif die_face == '6':
		return random.choice(six_corner_die)
	elif die_face == '8':
		return random.choice(eight_corner_die)
	elif die_face == '12':
		return random.choice(twelve_corner_die)
	elif die_face == '20':
		return random.choice(twenty_corner_die)
	else:
		if die_face%2 == 0:
			return random.randint(1,die_face)
		else:
			return "this is not a vaild die"

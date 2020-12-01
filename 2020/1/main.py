# A really tacky rushed solution. :(
# I started it a bit late.

fdone = sdone = False

with open("input", 'r') as file:
	lines = [int(x) for x in file]
	for x in lines:
		for y in lines:
			if sum([x,y]) == 2020 and not fdone:
				print(f"1: {x*y}")
				fdone = True
			for z in lines:
				if sum([x,y,z]) == 2020 and not sdone:
					print(f"2: {x*y*z}")
					sdone = True

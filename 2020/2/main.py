# code bad :(
numberfound = 0
part2found = 0

with open("input") as file:
	lines = [x for x in file]
	for line in lines:
		passpattern = line.split(':')
		password = passpattern[1][1:]
		requirements = passpattern[0].split(' ')
		passrange = list(map(int, requirements[0].split('-')))
		passchar = requirements[1]
		charcount = password.count(passchar)
		if charcount >= passrange[0] and charcount <= passrange[1]:
			numberfound += 1
		if (password[passrange[0]-1] == passchar) != (password[passrange[1]-1] == passchar):
			part2found += 1
	print(f"Part One: {numberfound}")
	print(f"Part Two: {part2found}")
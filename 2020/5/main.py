# This one is incredibly late, had an assignment due.
# Will have pylint set up probably tomorrow so the code won't look so dreadful after that.

idlist = []

with open("input") as file:
	lines = [x.strip('\n') for x in file]
	for line in lines:
		binstr = ""
		for char in line:
			if char == "F" or char == "L":
				binstr += '0'
			else:
				binstr += '1'
		idlist.append(int(binstr, 2))
	answer = sorted(idlist)[-1]
	part2ans = ""
	for n in range(1, answer+1):
		if n not in idlist:
			if n+1 in idlist and n-1 in idlist:
				part2ans = n

print(f"Part 1: {answer}")
print(f"Part 2: {part2ans}")

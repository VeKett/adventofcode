# This code is so bad, runs horribly
# As long as I get the answer, I'm not terribly bothered

with open("input", 'r') as file:
	lines = [*map(int, file.readlines())]

for index, number in enumerate(lines):
	if index > 24:
		found = False
		before = [lines[index-1-x] for x in range(0,25)] # I suck with lists
		for n in before:
			if number - n in before:
				found = True
		if not found:
			errorNumber = number
			print(f"Part 1: {errorNumber}")
			break

for i, n in enumerate(lines): # this seems terribly inefficient, probably is. :)
	for x in range(i, len(lines)-1):
		potentialAnswer = lines[i:x]
		if sum(potentialAnswer) == errorNumber and potentialAnswer != [errorNumber]:
			sortedAnswer = sorted(potentialAnswer)
			print(f"Part 2: {sortedAnswer[0] + sortedAnswer[-1]}")

from copy import deepcopy

with open("input") as file:
	lines = file.readlines()

def testLines(lines, part2):
	accumulatorVal = 0
	ranLines = []
	index = 0
	endex = len(lines)
	while True:
		if part2 and index in ranLines:
			return None
		if index not in ranLines and index != endex:
			ranLines.append(index)
			line = lines[index]
			l1, l2 = line.split()
			if l1 == "acc":
				accumulatorVal += int(l2)
			if l1 == "jmp":
				index += int(l2)
			else:
				index += 1
		else:
			break
	return accumulatorVal

for i, v in enumerate(lines):
	lines2 = deepcopy(lines)
	if v.startswith('jmp'):
		lines2[i] = v.replace('jmp', 'nop')
	elif v.startswith('nop'):
		lines2[i] = v.replace('nop', 'jmp')
	result = testLines(lines2, True)
	if result:
		break

print(f"Part 1: {testLines(lines, False)}")
print(f"Part 2: {result}")
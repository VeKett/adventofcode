threeval = 1
oneval = 0

with open("input", 'r') as file:
	lines = sorted([0] + [*map(int, file.readlines())])

for x in range(1, len(lines)):
	calculate = lines[x] - lines[x-1]
	if calculate == 3:
		threeval += 1
	elif calculate == 1:
		oneval += 1

y = [1] + [0] * (len(lines)-1)
for index, value in enumerate(lines):
	for n in range(index-3, index):
		if value - lines[n] <= 3:
			y[index] += y[n]

print(f"Part 1: {oneval*threeval}")
print(f"Part 2: {y[-1]}")

from functools import reduce # I had originally planned to use math.prod() but don't have Python 3.8 currently
import operator

slopes = [[1,1], [3,1], [5,1], [7,1], [1,2]]
completetreelist = []
currentslope = 1
with open("input") as file:
	lines = [x.rstrip() for x in file.readlines()]
	width = len(lines[0])
	for slope in slopes:
		trees = 0
		x = y = 0

		while y < len(lines):
			if lines[y][x % width] == "#":
				trees += 1
			x += slope[0]
			y += slope[1]
		print(f"Slope {currentslope}: {trees}")
		completetreelist.append(trees)
		currentslope += 1
	print(f"Product of slopes: {reduce(operator.mul, completetreelist, 1)}")
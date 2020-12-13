with open("input") as file:
	lines = file.read().splitlines()
	lines[0] = int(lines[0])

ids = list(map(int, [i for i in lines[1].split(',') if i.isdigit()]))

def partone():
	currentTime = lines[0]
	while True:
		for id in ids:
			if currentTime % id == 0:
				return (currentTime - lines[0]) * id
		currentTime += 1

def parttwo():
	n, step = 0, 1
	for k,v in enumerate(lines[1].split(',')):
		if v == "x": continue
		v = (int(v))
		r = (v - k) % v
		while n % v - r != 0: n += step
		step *= v
	return n
print(f"Part 1: {partone()}")
print(f"Part 2: {parttwo()}")
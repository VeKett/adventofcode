# This was a pain in my ass
# Still not linted but looks slightly better than usual

setify = lambda x: set(x.replace('\n', ''))

file = open("input").read()
items = file.split('\n\n')

def partOne(item):
	return len(setify(item))

def partTwo(item):
	questions = setify(item)
	answers = item.split()
	return sum(all(question in answer for answer in answers) for question in questions)

print(f"Part 1: {sum(partOne(item) for item in items)}")
print(f"Part 2: {sum(partTwo(item) for item in items)}")

import turtle

t = turtle.Turtle()

t.speed(0)
t._tracer(0,0)

print(f"Start: {str(t.pos())}")

with open("input", 'r') as file:
	lines = file.read().split('\n')[:-1]


for i in lines:
	ins = i[0]
	value = int(i[1:])
	if ins == "F":
		t.forward(value)
	elif ins == "L":
		t.left(value)
	elif ins == "R":
		t.right(value)
	else:
		tempangle = t.heading()
		if ins == "N":
			t.setheading(90)
		elif ins == "E":
			t.setheading(0)
		elif ins == "S":
			t.setheading(270)
		elif ins == "W":
			t.setheading(180)
		t.forward(value)
		t.setheading(tempangle)
t._update()

endtuple = t.pos()
endvalue = int(abs(endtuple[0]) + abs(endtuple[1]))

print(f"End: {endvalue}")
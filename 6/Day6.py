f = open("Day6.Input")

#Part 1
lights = []
for i in range(1000):
	lights.append([ 0 ] * 1000)

for line in f:
	commmands = line.split(" ")

	if commmands[0] == "turn":
		if commmands[1] == "on":
			point_a = commmands[2].split(",")
			point_b = commmands[4].split(",")
			for i in range(int(point_a[0]), int(point_b[0]) + 1):
				for j in range(int(point_a[1]), int(point_b[1]) + 1):
					lights[i][j] = 1

		if commmands[1] == "off":
			point_a = commmands[2].split(",")
			point_b = commmands[4].split(",")
			for i in range(int(point_a[0]), int(point_b[0]) + 1):
				for j in range(int(point_a[1]), int(point_b[1]) + 1):
					lights[i][j] = 0

	if commmands[0] == "toggle":
		point_a = commmands[1].split(",")
		point_b = commmands[3].split(",")
		for i in range(int(point_a[0]), int(point_b[0]) + 1):
			for j in range(int(point_a[1]), int(point_b[1]) + 1):
				lights[i][j] = (lights[i][j] + 1) % 2

total = 0
for row in lights:
	total += sum(row)
print(total)

#Part 2
lights = []
for i in range(1000):
	lights.append([ 0 ] * 1000)
f.seek(0)

for line in f:
	commmands = line.split(" ")

	if commmands[0] == "turn":
		if commmands[1] == "on":
			point_a = commmands[2].split(",")
			point_b = commmands[4].split(",")
			for i in range(int(point_a[0]), int(point_b[0]) + 1):
				for j in range(int(point_a[1]), int(point_b[1]) + 1):
					lights[i][j] += 1

		if commmands[1] == "off":
			point_a = commmands[2].split(",")
			point_b = commmands[4].split(",")
			for i in range(int(point_a[0]), int(point_b[0]) + 1):
				for j in range(int(point_a[1]), int(point_b[1]) + 1):
					lights[i][j] = max(lights[i][j] - 1, 0)


	if commmands[0] == "toggle":
		point_a = commmands[1].split(",")
		point_b = commmands[3].split(",")
		for i in range(int(point_a[0]), int(point_b[0]) + 1):
			for j in range(int(point_a[1]), int(point_b[1]) + 1):
				lights[i][j] += 2

total = 0
for row in lights:
	total += sum(row)
print(total)
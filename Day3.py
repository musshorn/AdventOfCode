f = open("Day3.Input","r")

#Problem 1
visited = {}
current = [0, 0]

for line in f:
	for char in line:
		if char == '^':
			current[1] += 1
		elif char == 'v':
			current[1] -= 1
		elif char == '<':
			current[0] -= 1
		elif char == '>':
			current[0] += 1
		visited[str(current[0]) + 'x' + str(current[1])] = 1
print(len(visited.keys()))

#Problem 2
visited = {'0x0' : 1}
turn = 0 # 0 = real santa, 1 = robo santa
current = [[0, 0], [0, 0]]
for char in line:
	if char == '^':
		current[turn][1] += 1
	elif char == 'v':
		current[turn][1] -= 1
	elif char == '<':
		current[turn][0] -= 1
	elif char == '>':
		current[turn][0] += 1
	visited[str(current[turn][0]) + 'x' + str(current[turn][1])] = 1
	turn = (turn + 1) % 2
print(len(visited.keys()))

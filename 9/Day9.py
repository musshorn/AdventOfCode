import itertools
f = open("Day9.Input")

routes = {}
for line in f:
	tokens = line.split(" ")
	
	if tokens[0] not in routes.keys():
		routes[tokens[0]] = {}
	
	if tokens[2] not in routes.keys():
		routes[tokens[2]] = {}
	
	routes[tokens[0]][tokens[2]] = int(tokens[4])
	routes[tokens[2]][tokens[0]] = int(tokens[4])

best = -1
worst = 0
for order in itertools.permutations(routes.keys()):
	distance = 0
	try:
		for i in range(len(order) - 1):
			distance += routes[order[i]][order[i + 1]]
		if best == -1 or distance < best:
			best = distance
		if distance > worst:
			worst = distance
	except:
		continue
print(best)
print(worst)
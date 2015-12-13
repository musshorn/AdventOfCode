import itertools

def Part1():
	f = open("Day13.Input", "r")

	relationships = {}
	for line in f:
		tokens = line.split(" ")
		if tokens[0] not in relationships.keys():
			relationships[tokens[0]] = {}
		
		if tokens[2] == "gain":
			relationships[tokens[0]][tokens[-1][:-2]] = int(tokens[3])
		else:
			relationships[tokens[0]][tokens[-1][:-2]] = -int(tokens[3])
	f.close()
	return relationships

def Part2():
	f = open("Day13.Input", "r")
	relationships = {}
	for line in f:
		tokens = line.split(" ")
		if tokens[0] not in relationships.keys():
			relationships[tokens[0]] = {"Me" : 0}
		
		if tokens[2] == "gain":
			relationships[tokens[0]][tokens[-1][:-2]] = int(tokens[3])
		else:
			relationships[tokens[0]][tokens[-1][:-2]] = -int(tokens[3])

	#Add myself
	relationships["Me"] = {}
	for person in relationships.keys():
		relationships["Me"][person] = 0
	
	f.close()
	return relationships

def FindBest(relationships):
	best = 0
	for order in itertools.permutations(relationships.keys()):
		happiness = 0

		#First Person
		happiness += relationships[order[0]][order[-1]]
		happiness += relationships[order[0]][order[1]]

		#Middle People
		for i in range(1, len(order) - 1):
			happiness += relationships[order[i]][order[i - 1]]
			happiness += relationships[order[i]][order[i + 1]]

		#Last Person
		happiness += relationships[order[-1]][order[0]]
		happiness += relationships[order[-1]][order[-2]]

		if happiness > best:
			best = happiness

	return best

print(FindBest(Part1()))
print(FindBest(Part2()))
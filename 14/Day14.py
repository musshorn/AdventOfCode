class Reindeer():
	def __init__(self, name, speed, duration, rest):
		self.speed = speed
		self.duration = duration
		self.rest = rest
		self.name = name

		self.distance = 0
		self.flyingTime = 0
		self.resting = False
		self.score = 0
	
	def __repr__(self):
		return "%s has travelled %d" % (self.name, self.distance)

	def Tick(self):
		if not self.resting:
			self.flyingTime += 1
			self.distance += self.speed

			if self.flyingTime == self.duration:
				self.resting = True
				self.flyingTime = 0
		else:
			self.flyingTime += 1
			if self.flyingTime == self.rest:
				self.resting = False
				self.flyingTime = 0
	
	def GetDistance(self):
		return self.distance

	def AddPoint(self):
		self.score += 1

	def GetScore(self):
		return self.score

def Part1():
	f = open("Day14.Input", "r")
	helpers = []
	for line in f:
		tokens = line.split(" ")
		helpers.append(Reindeer(tokens[0], int(tokens[3]), int(tokens[6]), int(tokens[13])))

	for i in range(2503):
		for h in helpers:
			h.Tick()

	best = 0
	for h in helpers:
		if h.GetDistance() > best:
			best = h.GetDistance()
	return best

def Part2():
	f = open("Day14.Input", "r")
	helpers = []
	for line in f:
		tokens = line.split(" ")
		helpers.append(Reindeer(tokens[0], int(tokens[3]), int(tokens[6]), int(tokens[13])))

	for i in range(2503):
		
		bestDistance = 0
		bestIndex = 0
		for j in range(len(helpers)):
			helpers[j].Tick()
		
			if helpers[j].GetDistance() > bestDistance:
				bestDistance = helpers[j].GetDistance()

		for h in helpers:
			if h.GetDistance() == bestDistance:
				h.AddPoint()

	best = 0
	for h in helpers:
		if h.GetScore() > best:
			best = h.GetScore()

	return best

print(Part1())
print(Part2())

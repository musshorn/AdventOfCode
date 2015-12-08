import numpy as np

f = open("Day7.Input")

class Memory():
	def __init__(self):
		self.memory = {}

	def Get(self, key):
		try:
			return np.uint16(key)
		except:		
			if key in self.memory.keys():
				return self.memory[key]
			else:
				return None

	def Set(self, key, value):
		if key.strip() not in self.memory.keys():
			self.memory[key.strip()] = np.uint16(value)

	def __repr__(self):
		out = ""
		for key in self.memory.keys():
			out += "%s %d\n" % (key, self.memory[key])
		return out

m = Memory()
ops = []
for line in f:
	ops.append(line)

#Part 1
index = 0
while m.Get("a") == None:
	commands = ops[index].split(" ")
	operator = commands[1]

	if commands[0] == "NOT":
		operator = "NOT"

	if operator == "->" and m.Get(commands[0]) != None:
		m.Set(commands[2], m.Get(commands[0]))

	elif operator == "AND" and m.Get(commands[0]) != None and m.Get(commands[2]) != None:
		m.Set(commands[4], m.Get(commands[0]) & m.Get(commands[2]))

	elif operator == "OR"  and m.Get(commands[0]) != None and m.Get(commands[2]) != None:
		m.Set(commands[4], m.Get(commands[0]) | m.Get(commands[2]))

	elif operator == "LSHIFT" and m.Get(commands[0]) != None and m.Get(commands[2]) != None:
		m.Set(commands[4], m.Get(commands[0]) << int(commands[2]))

	elif operator == "RSHIFT" and m.Get(commands[0]) != None and m.Get(commands[2]) != None:
		m.Set(commands[4], m.Get(commands[0]) >> int(commands[2]))

	elif operator == "NOT"  and m.Get(commands[1]) != None:
		m.Set(commands[3], ~m.Get(commands[1]))
	index = (index + 1) % len(ops)

print(m.Get('a'))

#Part 2
a = m.Get("a")
m = Memory()
m.Set("b", a)
index = 0
print(m)
while m.Get("a") == None:
	commands = ops[index].split(" ")
	operator = commands[1]

	if commands[0] == "NOT":
		operator = "NOT"

	if operator == "->" and m.Get(commands[0]) != None:
		m.Set(commands[2], m.Get(commands[0]))

	elif operator == "AND" and m.Get(commands[0]) != None and m.Get(commands[2]) != None:
		m.Set(commands[4], m.Get(commands[0]) & m.Get(commands[2]))

	elif operator == "OR"  and m.Get(commands[0]) != None and m.Get(commands[2]) != None:
		m.Set(commands[4], m.Get(commands[0]) | m.Get(commands[2]))

	elif operator == "LSHIFT" and m.Get(commands[0]) != None and m.Get(commands[2]) != None:
		m.Set(commands[4], m.Get(commands[0]) << int(commands[2]))

	elif operator == "RSHIFT" and m.Get(commands[0]) != None and m.Get(commands[2]) != None:
		m.Set(commands[4], m.Get(commands[0]) >> int(commands[2]))

	elif operator == "NOT"  and m.Get(commands[1]) != None:
		m.Set(commands[3], ~m.Get(commands[1]))
	index = (index + 1) % len(ops)

print(m.Get('a'))
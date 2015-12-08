import ast
import re
f = open("Day8.Input")

#Part 1
total = 0
for line in f:
	total += len(line.strip()) - len(ast.literal_eval(line.strip()))
print(total)

#Part 2
f.seek(0)
total = 0
for line in f:
	total += 2 + line.count("\\") + line.count('"')
print(total)

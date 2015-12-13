import json

f = open("Day12.Input")
data = json.loads(f.read())

def RecursiveSearch(submap):
	submapTotal = 0
	if type(submap) is list:
		for i in submap:
			submapTotal += RecursiveSearch(i)
	
	elif type(submap) is dict:
		for key in submap.keys():
			submapTotal += RecursiveSearch(submap[key])

	elif type(submap) is int:
		submapTotal += submap
	return submapTotal

def RecursiveSearchPart2(submap):
	submapTotal = 0
	if type(submap) is list:
		for i in submap:
			submapTotal += RecursiveSearchPart2(i)
	
	elif type(submap) is dict:
		for key in submap.keys():
			if submap[key] == "red":
				return 0
		for key in submap.keys():
			submapTotal += RecursiveSearchPart2(submap[key])

	elif type(submap) is int:
		submapTotal += submap
	return submapTotal

print(RecursiveSearch(data))
print(RecursiveSearchPart2(data))

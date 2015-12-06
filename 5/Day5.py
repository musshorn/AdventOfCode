f = open("Day5.Input", "r")

#Part 1
vowels = ['a', 'e', 'i', 'o', 'u']
bad_strings = ['ab', 'cd', 'pq', 'xy']

nice_strings = 0

for line in f:
	acceptable = True

	for bad in bad_strings:
		if bad in line:
			acceptable = False
			break

	if acceptable:
		has_doubles = False
		for i in range(len(line) - 1):
			if line[i] == line[i + 1]:
				has_doubles = True
				break
		
		vowel_count = 0
		for v in vowels:
			vowel_count += line.count(v)

		if has_doubles and vowel_count > 2:
			nice_strings += 1
print(nice_strings)

#Part 2
nice_strings = 0
f.seek(0)

for line in f:
	has_pair = False
	has_double = False

	for i in range(len(line) - 1):
		pair = line[i:i + 2]

		if pair in line[i + 2:]:
			has_pair = True
	
	for i in range(len(line) - 2):
		if line[i] == line[i + 2]:
			has_double = True
	
	if has_pair and has_double:
		nice_strings += 1
print(nice_strings)

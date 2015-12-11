def iterations(key, num):
	for x in range(num):
		out = ""
		i = 0
		while i < len(key):
			count = 0
			char = key[i]
			j = i
			while j < len(key):
				if char == key[j]:
					count += 1
				else:
					break
				j += 1
			i = j
			out += str(count) + char
		key = out
	return key

# Could be sped up with a lookup table
print(len(iterations("1113122113", 40)))
print(len(iterations("1113122113", 50)))
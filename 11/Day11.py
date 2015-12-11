# Range is 97 - 122

def HasStraight(key):
	for i in range(len(key) - 3):
		if ord(key[i + 1]) - ord(key[i]) == 1 and ord(key[i + 2]) - ord(key[i + 1]) == 1:
			return True
	return False

def HasGoodLetters(key):
	if "i" not in key and "o" not in key and "l" not in key:
		return True
	return False

def HasPairs(key):
	count = 0
	i = 0
	while i < len(key) - 1:
		if key[i] == key[i + 1]:
			count += 1
			i += 1 # skip a char

		if count == 2:
			return True

		i += 1
	return False

def NextPass(pwd):
	while not (HasGoodLetters(pwd) and HasStraight(pwd) and HasPairs(pwd)):
		pwd[-1] = chr(ord(pwd[-1]) + 1)
		for i in range(len(pwd) - 1, 0, -1):
			if ord(pwd[i]) == 123:
				pwd[i] = 'a'
				pwd[i - 1] = chr(ord(pwd[i - 1]) + 1)
	return pwd

pwd = list('cqjxjnds')
pwd1 = NextPass(pwd)
print(''.join(pwd1))

#Move to the next bad password and test again
pwd1[-1] = chr(ord(pwd1[-1]) + 1)
for i in range(len(pwd1) - 1, 0, -1):
	if ord(pwd1[i]) == 123:
		pwd1[i] = 'a'
		pwd1[i - 1] = chr(ord(pwd1[i - 1]) + 1)

pwd2 = NextPass(pwd1)
print(''.join(pwd2))

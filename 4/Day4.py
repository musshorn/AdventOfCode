import hashlib

#Part 1 and 2. Change "zeroes" to be the number of leading0

secret = 'bgvyzdsv'
i = 0
zeroes = 6

while True:
	check = secret + str(i)
	hexdigest = hashlib.md5(check.encode('utf-8')).hexdigest()

	i += 1
	try:
		if int(hexdigest[0:zeroes]) == 0:
			print(i - 1, hexdigest)
			break
	except:
		continue

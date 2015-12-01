f = open("Day1.Input", "r")
l = f.readline()

#Part 1
print((len(l.split("(")) - 1) - (len(l.split(")")) - 1))

#Part 2
level = 0
pos = 0
for char in l:
    pos += 1
    if char == "(":
        level += 1
    else:
        level -= 1
    if level == -1:
         print(pos)
         break
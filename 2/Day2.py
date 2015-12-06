f = open("Day2.Input", "r")

# Part 1
paper = 0
for line in f:
    l, w, h = map(int, line.split("x"))
    paper += 2 * (l * w + w * h + h * l) + min(l * w, w * h, h * l)
print(paper)

#Part 2
f.seek(0)
ribbon = 0
for line in f:
    l, w, h = map(int, line.split("x"))
    ribbon += 2 * min(l + w, h + w, h + l) +  l * h * w
print(ribbon)
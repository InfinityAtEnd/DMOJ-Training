# See the problem request at the link down below
# https://dmoj.ca/problem/p287ex4

# my solution:
T = int(input())
lines = [input() for x in range(T)]
blanks = []

for line in lines:
	ind = 0
	keep_looking = True
	i = 0
	while keep_looking and (i < len(line)):
		if ord(line[i]) == 32:
			ind = i + 1
			keep_looking = False
		else:
			i += 1
	blanks.append(ind)

for bl in blanks:
	print(bl)

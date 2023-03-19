# See the problem request at the link down below
# https://dmoj.ca/problem/ecoo15r1p1

# my solution:
import math

cases = {}
box_contents = []
box_times = []
smarties = {'orange': 0, 'blue': 0, 'green': 0, 'yellow': 0, 'pink': 0, 'violet': 0, 'brown': 0, 'red': 0}
for i in range(10):
	box_contents = []
	while (col := input()) != 'end of box':
		box_contents.append(col.lower())
	cases[i] = box_contents

for k, v in cases.items():
	seconds = 0
	for c in smarties.keys():
		n = v.count(c)
		if c != 'red':
			seconds = seconds + (math.ceil(n / 7) * 13)
		else:
			seconds = seconds + (n * 16)
	box_times.append(seconds)

for time in box_times:
	print(time)

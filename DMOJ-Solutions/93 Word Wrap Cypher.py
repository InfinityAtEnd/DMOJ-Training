# See the problem request at the link down below
# https://dmoj.ca/problem/wordwrap

# my solution:
output = []
for data in range(5):
	out = ''
	w = int(input())
	encoded = input()
	rows = int(len(encoded) / w)
	text = ['' for x in range(rows)]
	line = 0
	for ch in encoded:
		text[line] = text[line] + ch
		if line == rows - 1:
			line = 0
		else:
			line += 1
	for l in text:
		out = out + l.lstrip() + ' '
	output.append(out)

for o in output:
	print(o)

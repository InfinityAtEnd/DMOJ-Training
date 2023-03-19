# See the problem request at the link down below
# https://dmoj.ca/problem/ccc21j3

# my solution:
from sys import stdin

codes = []
output = []
for line in stdin:
	if line == '':
		break
	else:
		codes.append(line)

previous_step = ''
for code in codes[:-1]:
	step = ''
	steps = code[2:-1]
	firsts_sum = int(code[0]) + int(code[1])
	if firsts_sum == 0:
		step = previous_step
	elif firsts_sum % 2 == 0:
		step = 'right'
		previous_step = step
	else:
		step = 'left'
		previous_step = step
	output.append([step, steps])

for out in output:
	print(f'{out[0]} {out[1]}')

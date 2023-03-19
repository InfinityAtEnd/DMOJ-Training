# See the problem request at the link down below
# https://dmoj.ca/problem/dmopc20c2p2

# my solution:
N, M = [int(x) for x in input().split()]
scarf = [int(x) for x in input().split()]
start = {}
end = {}

for i in range(N):
	color = scarf[i]
	if color not in start:
		start[color] = i
		end[color] = i
	else:
		end[color] = i

longest_scarf = 0

for i in range(M):
	relative = input().split()
	first = int(relative[0])
	last = int(relative[1])
	if first in start and last in end:
		length = end[last] - start[first] + 1
		if length > longest_scarf:
			longest_scarf = length

print(longest_scarf)

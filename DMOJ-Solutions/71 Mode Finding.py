# See the problem request at the link down below
# https://dmoj.ca/problem/dmopc19c3p1

# my solution:
N = int(input())
list_of_numbers = [int(x) for x in input().split()]
counted = {}
for nr in list_of_numbers:
	if nr in counted:
		counted[nr] += 1
	else:
		counted[nr] = 1

max_val = max(counted.values())
modes = []
for k, v in counted.items():
	if v == max_val:
		modes.append(k)

modes.sort()
for m in modes:
	print(m, end=' ')

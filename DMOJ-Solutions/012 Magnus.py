# See the problem request at the link down below
# https://dmoj.ca/problem/coci18c3p1

# my solution:
N = input()
H = 0
H_count = 0

for i in N:
	if i == 'H' and H == 0:
		H += 1
	elif i == 'O' and H == 1:
		H += 1
	elif i == 'N' and H == 2:
		H += 1
	elif i == 'I' and H == 3:
		H = 0
		H_count += 1

print(H_count)

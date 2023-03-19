# See the problem request at the link down below
# https://dmoj.ca/problem/coci20c2p1

# my solution:
nr_days = int(input())
change = input()
matrix = []
net = 100
for _ in range(net + 100):
	matrix.append('')

for i in range(nr_days):
	for j in range(len(matrix)):
		matrix[j] = matrix[j] + '.'
	if change[i] == '+':
		matrix[net] = matrix[net][:-1] + '/'
		net += 1
	elif change[i] == '-':
		matrix[net - 1] = matrix[net - 1][:-1] + '\\'
		net -= 1
	elif change[i] == '=':
		matrix[net] = matrix[net][:-1] + '_'

for line in matrix[::-1]:
	if '/' in line or '\\' in line or '_' in line:
		print(line)

# See the problem request at the link down below
# https://dmoj.ca/problem/ecoo17r3p1

# my solution:
baker_prizes = []
for set in range(10):
	baker_prizes.append(0)
	baker_brie = [int(i) for i in input().split(' ')]
	matrix = []  # baker_brie[1] lines and baker_brie[0] columns
	for i in range(baker_brie[1]):
		matrix.append([int(j) for j in input().split(' ')])

	for i in matrix:
		if sum(i) % 13 == 0:
			baker_prizes[set] += sum(i) // 13

	for i in range(baker_brie[0]):
		goods = 0
		for j in matrix:
			goods += j[i]
		if goods % 13 == 0:
			baker_prizes[set] += goods // 13

for prize in baker_prizes:
	print(prize)

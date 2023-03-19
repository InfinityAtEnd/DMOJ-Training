# See the problem request at the link down below
# https://dmoj.ca/problem/coci19c5p1

# my solution:
N, M = input().split(' ')
N = int(N)
M = int(M)
picture = []
for _ in range(N):
	picture.append(input())
pic = picture.copy()
rectangle_list = []
nr_rectangle = 0
for i in range(N):
	for c in range(len(pic[i])):
		if pic[i][c] == '*':
			if i == 0 and c == 0:
				nr_rectangle += 1
			elif i == 0 and pic[i][c - 1] != '*':
				nr_rectangle += 1
			elif c == 0 and pic[i - 1][c] != '*':
				nr_rectangle += 1
			elif pic[i - 1][c] != '*' and pic[i][c - 1] != '*':
				nr_rectangle += 1

print(nr_rectangle)

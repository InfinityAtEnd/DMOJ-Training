# See the problem request at the link down below
# https://dmoj.ca/problem/year2015p3

# my solution:
N = int(input())  # number of layers
ms = 2 * N - 1  # matrix size
matrix = []
for i in range(ms):
	matrix.append([])
	for j in range(ms):
		if i == (int(ms / 2)) and j == (int(ms / 2)):
			matrix[i].append('a')
		else:
			matrix[i].append('.')


def wrap_level(mat):  # level are counted a 1 from the center to the margins
	for lev in range(1, int((len(mat) - 1) / 2 + 1)):
		level = int(lev)
		letter = chr(97 + level)
		i_ind = int(len(mat) / 2)
		j_ind = int(len(mat) / 2)
		for i in range(i_ind - level, i_ind + level + 1):
			for j in range(j_ind - level, j_ind + level + 1):
				if i == (i_ind - level) or j == (j_ind - level) or i == (i_ind + level) or j == (j_ind + level):
					mat[i][j] = letter
	return mat


matrix = wrap_level(matrix)

for line in matrix:
	print(''.join(line))

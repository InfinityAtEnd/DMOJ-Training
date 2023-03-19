# See the problem request at the link down below
# https://dmoj.ca/problem/coci13c2p2

# my solution:
R, S = input().split()
R = int(R)
S = int(S)
seats = [input() for x in range(R)]


def check_links(benches, char):  # char will be '.' or 'o' ...'o' will give us a matrix with total hand shakes(must / 2)
	people_shakes = []
	if len(benches) == 1:
		bench_line = []
		for j in range(len(benches[0])):
			shakes = 0
			if benches[0][j] == char:
				if j == 0:
					if benches[0][j + 1] == 'o':
						shakes += 1
				elif j == len(benches[0]) - 1:
					if benches[0][j - 1] == 'o':
						shakes += 1
				else:
					if benches[0][j - 1] == 'o':
						shakes += 1
					if benches[0][j + 1] == 'o':
						shakes += 1
			bench_line.append(shakes)
		people_shakes.append(bench_line)
	else:
		for i in range(len(benches)):  # '.' - give us a matrix with nr of hand shakes Mirko could do
			bench_line = []
			for j in range(len(benches[i])):
				shakes = 0
				if benches[i][j] == char:
					if i == 0:
						if j == 0:  # top-left corner
							if benches[i + 1][j] == 'o':
								shakes += 1
							if benches[i][j + 1] == 'o':
								shakes += 1
							if benches[i + 1][j + 1] == 'o':
								shakes += 1
						elif j == len(benches[i]) - 1:  # top-right corner
							if benches[i + 1][j] == 'o':
								shakes += 1
							if benches[i][j - 1] == 'o':
								shakes += 1
							if benches[i + 1][j - 1] == 'o':
								shakes += 1
						else:  # top-edge line
							if benches[i][j + 1] == 'o':
								shakes += 1
							if benches[i + 1][j + 1] == 'o':
								shakes += 1
							if benches[i + 1][j] == 'o':
								shakes += 1
							if benches[i + 1][j - 1] == 'o':
								shakes += 1
							if benches[i][j - 1] == 'o':
								shakes += 1
					elif i == len(benches) - 1:
						if j == 0:  # bottom-left corner
							if benches[i][j + 1] == 'o':
								shakes += 1
							if benches[i - 1][j] == 'o':
								shakes += 1
							if benches[i - 1][j + 1] == 'o':
								shakes += 1
						elif j == len(benches[i]) - 1:  # bottom-right corner
							if benches[i - 1][j] == 'o':
								shakes += 1
							if benches[i][j - 1] == 'o':
								shakes += 1
							if benches[i - 1][j - 1] == 'o':
								shakes += 1
						else:  # bottom-edge line
							if benches[i][j - 1] == 'o':
								shakes += 1
							if benches[i - 1][j - 1] == 'o':
								shakes += 1
							if benches[i - 1][j] == 'o':
								shakes += 1
							if benches[i - 1][j + 1] == 'o':
								shakes += 1
							if benches[i][j + 1] == 'o':
								shakes += 1
					else:
						if j == 0:  # left-edge line
							if benches[i - 1][j] == 'o':
								shakes += 1
							if benches[i - 1][j + 1] == 'o':
								shakes += 1
							if benches[i][j + 1] == 'o':
								shakes += 1
							if benches[i + 1][j + 1] == 'o':
								shakes += 1
							if benches[i + 1][j] == 'o':
								shakes += 1
						elif j == len(benches[i]) - 1:  # right-edge line
							if benches[i - 1][j] == 'o':
								shakes += 1
							if benches[i - 1][j - 1] == 'o':
								shakes += 1
							if benches[i][j - 1] == 'o':
								shakes += 1
							if benches[i + 1][j - 1] == 'o':
								shakes += 1
							if benches[i + 1][j] == 'o':
								shakes += 1
						else:  # center spots with all 8 neighbours
							if benches[i - 1][j - 1] == 'o':
								shakes += 1
							if benches[i - 1][j] == 'o':
								shakes += 1
							if benches[i - 1][j + 1] == 'o':
								shakes += 1
							if benches[i][j - 1] == 'o':
								shakes += 1
							if benches[i][j + 1] == 'o':
								shakes += 1
							if benches[i + 1][j - 1] == 'o':
								shakes += 1
							if benches[i + 1][j] == 'o':
								shakes += 1
							if benches[i + 1][j + 1] == 'o':
								shakes += 1
				bench_line.append(shakes)
			people_shakes.append(bench_line)
	return people_shakes


def mirko_shakes(benches):
	max_per_bench = []
	for bench in benches:
		max_per_bench.append(max(bench))
	return max(max_per_bench)


def total_shakes(benches):
	total_per_bench = []
	for bench in benches:
		total_per_bench.append(sum(bench))
	res = sum(total_per_bench)
	return res / 2


nr_of_shakes = check_links(seats, 'o')
nr_of_possible_shakes = check_links(seats, '.')
hand_shakes_of_people = total_shakes(nr_of_shakes)
mirko_nr_of_shakes = mirko_shakes(nr_of_possible_shakes)
output = hand_shakes_of_people + mirko_nr_of_shakes
print(int(output))

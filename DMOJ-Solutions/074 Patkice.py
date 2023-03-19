# See the problem request at the link down below
# https://dmoj.ca/problem/coci20c1p1

# my solution:
r, s = [int(x) for x in input().split()]
ocean_map = []
directions = {}
home_i = 0
home_j = 0
for i in range(r):
	ocean_map.append(input())
for i in range(len(ocean_map)):
	if 'o' in ocean_map[i]:
		home_i = i
		home_j = ocean_map[i].find('o')  # map the starting island


def update_position(map, position):  # updates the indexing position of the ducks on the ocean map
	i = position[0]
	j = position[1]
	if map[i][j] == '^':
		return i - 1, j
	elif map[i][j] == '>':
		return i, j + 1
	elif map[i][j] == 'v':
		return i + 1, j
	else:
		return i, j - 1


def check_direction(map, position):  # keeps looking all the way... return length is path clear or False if not
	length = 1
	i = position[0]
	j = position[1]
	last_position = position
	while map[i][j] in '<>v^':
		last_position = update_position(map, last_position)
		length += 1
		i = last_position[0]
		j = last_position[1]
	if map[i][j] == 'o' or map[i][j] == '.':
		return False
	else:
		return length


def print_solution(directions):
	val = []
	list_values = directions.values()
	for value in list_values:
		if value:
			val.append(value)
	if not val:
		print(':(')
	else:
		paths = []
		for k, v in directions.items():
			if v == min(val):
				paths.append(k)
		print(':)')
		paths = sorted(paths)
		print(paths[0])


directions['N'] = check_direction(ocean_map, (home_i - 1, home_j))
directions['E'] = check_direction(ocean_map, (home_i, home_j + 1))
directions['W'] = check_direction(ocean_map, (home_i, home_j - 1))
directions['S'] = check_direction(ocean_map, (home_i + 1, home_j))
print_solution(directions)

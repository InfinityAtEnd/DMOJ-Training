# See the problem request at the link down below
# https://dmoj.ca/problem/ccc18j3

# my solution:
distances = input().split()
starting = [int(x) for x in distances]
all_distances = []


def distances_of(lst, city):
	distances_to_cities = []
	for k in range(len(lst) + 1):
		if k < city:
			distances_to_cities.append(sum(lst[k:city]))
		elif k == city:
			distances_to_cities.append(0)
		else:
			distances_to_cities.append(sum(lst[city:k]))
	return distances_to_cities


for i in range(len(starting) + 1):
	all_distances.append(distances_of(starting, i))

for j in all_distances:
	for i in j:
		print(i, end=' ')
	print()

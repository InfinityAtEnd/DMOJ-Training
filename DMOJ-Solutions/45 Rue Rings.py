# See the problem request at the link down below
# https://dmoj.ca/problem/ecoo18r1p2

# my solution:
dataset_lowest = []
route_list = []
for d in range(10):
	routes = []
	nr_of_routes = int(input())
	for nr in range(nr_of_routes):
		routes.append(input().split())
	working_routes = []
	for r in routes:
		working_routes.append([int(x) for x in r])

	lowest_in_routes = []
	lowest = 0
	lst = 0
	for route in working_routes:
		lst = min(route[2:])
		lowest_in_routes.append(lst)

	lowest = min(lowest_in_routes)

	dataset_lowest.append(lowest)
	l_of_r = []
	for routes in working_routes:
		if lowest in routes[2:]:
			l_of_r.append(routes[0])
	l_of_r.sort()
	route_list.append(l_of_r[:])
	l_of_r.clear()

for i in range(len(dataset_lowest)):
	print(f'{dataset_lowest[i]} {{', end='')
	print(','.join(map(str, route_list[i])), end='')
	print(f'}}')

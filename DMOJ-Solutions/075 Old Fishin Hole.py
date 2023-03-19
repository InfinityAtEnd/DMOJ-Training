# See the problem request at the link down below
# https://dmoj.ca/problem/ccc09j2

# my solution:
trout_p = int(input())
pike_p = int(input())
pickerel_p = int(input())
total_p = int(input())
ways = []


def fish_order(trout_p, pike_p, pickerel_p):
	fish_points = {}
	fish_points['trout'] = trout_p
	fish_points['pike'] = pike_p
	fish_points['pickerel'] = pickerel_p
	sorted_fish_points = dict(sorted(fish_points.items(), key=lambda x: x[1]))
	return sorted_fish_points


order = fish_order(trout_p, pike_p, pickerel_p)
a, b, c = order.values()
max_a = total_p // a
max_b = total_p // b
max_c = total_p // c
for i in range(max_a + 1):
	if max_b > 0:
		for j in range(max_b + 1):
			if max_c > 0:
				for k in range(max_c + 1):
					points_scored = i * a + j * b + k * c
					if points_scored <= total_p and (i + j + k > 0):
						ways.append((i, j, k))
			else:
				points_scored = i * a + j * b
				if points_scored <= total_p and (i + j > 0):
					ways.append((i, j, 0))
	else:
		points_scored = i * a
		if points_scored <= total_p and i > 0:
			ways.append((i, 0, 0))

fishes = list(order.keys())
trout = 0
pike = 0
pick = 0
for i in range(len(fishes)):
	if fishes[i] == 'trout':
		trout = i
	elif fishes[i] == 'pike':
		pike = i
	else:
		pick = i
for way in ways:
	print(f'{way[trout]} Brown Trout, {way[pike]} Northern Pike, {way[pick]} Yellow Pickerel')
print(f'Number of ways to catch fish: {len(ways)}')

# See the problem request at the link down below
# https://dmoj.ca/problem/coci10c1p2

# my solution:
N = int(input())
desks = []
for i in range(N):
	desk = input().split()
	desks.append([int(desk[0]), int(desk[1])])
grades = [0, 0, 0, 0, 0, 0]
max_chains = [0, 0, 0, 0, 0, 0]
previous = [0, 0]
for desk in desks:
	if desk[0] != desk[1]:
		if desk[0] in previous:
			grades[desk[0]] += 1
		else:
			if grades[desk[0]] > max_chains[desk[0]]:
				max_chains[desk[0]] = grades[desk[0]]
				grades[desk[0]] = 1
			else:
				grades[desk[0]] = 1
		if desk[1] in previous:
			grades[desk[1]] += 1
		else:
			if grades[desk[1]] > max_chains[desk[1]]:
				max_chains[desk[1]] = grades[desk[1]]
				grades[desk[1]] = 1
			else:
				grades[desk[1]] = 1
	else:
		if desk[0] in previous:
			grades[desk[0]] += 1
		else:
			if grades[desk[0]] > max_chains[desk[0]]:
				max_chains[desk[0]] = grades[desk[0]]
				grades[desk[0]] = 1
			else:
				grades[desk[0]] = 1
	if (previous[0] not in desk) and (previous[1] not in desk):
		previous = desk
	for val in previous:
		if val not in desk:
			previous.remove(val)
	if desk[0] not in previous:
		previous.append(desk[0])
	if desk[1] not in previous:
		previous.append(desk[1])
	if len(previous) < 2:
		previous.append(previous[0])

for i in range(1, len(grades)):
	if grades[i] > max_chains[i]:
		max_chains[i] = grades[i]

max_chain = max(max_chains)
chain_lowest_grade = 0
for grade in range(1, len(max_chains)):
	if max_chains[grade] == max_chain:
		chain_lowest_grade = grade
		break

print(f'{max_chain} {chain_lowest_grade}')

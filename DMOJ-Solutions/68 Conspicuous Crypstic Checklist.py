# See the problem request at the link down below
# https://dmoj.ca/problem/dmopc19c5p1

# my solution:
N, M = [int(nr) for nr in input().split()]


def can_be_completed(backpack, quest):
	can_be = True
	for q in quest:
		if q not in backpack:
			can_be = False
			break
	return can_be


backpack = set()
for i in range(N):
	backpack.add(input())

tasks_completed = 0

for i in range(M):
	items = int(input())
	quest = [input() for x in range(items)]
	if can_be_completed(backpack, quest):
		tasks_completed += 1

print(tasks_completed)

# See the problem request at the link down below
# https://dmoj.ca/problem/ecoo18r1p1

# my solution:
play_time = []
for i in range(10):
	willow, days = input().split()
	boxes_home = 0
	days_left_to_play = int(willow)
	has_box = False
	mandy_day = [input() for _ in range(int(days))]
	for day in mandy_day:
		if day == 'B':
			boxes_home += 1

		if has_box:
			if days_left_to_play == 1:
				has_box = False
				days_left_to_play = int(willow)
			else:
				days_left_to_play -= 1
		else:
			if boxes_home > 0:
				has_box = True
				boxes_home -= 1
				days_left_to_play -= 1

	if has_box:
		response = days_left_to_play + boxes_home * int(willow)
	else:
		response = boxes_home * int(willow)
	play_time.append(response)

for i in play_time:
	print(i)

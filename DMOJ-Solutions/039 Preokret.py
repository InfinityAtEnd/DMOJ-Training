# See the problem request at the link down below
# https://dmoj.ca/problem/coci18c2p1

# my solution:
half_time_mark = 2 * 12 * 60
half_time_score = 0
team_A_score = 0
team_B_score = 0
turnarounds = 0
time_table = {}
goals_A = int(input())
for i in range(goals_A):
	scored_at = int(input())
	time_table[scored_at] = 'A'
goals_B = int(input())
for i in range(goals_B):
	scored_at = int(input())
	time_table[scored_at] = 'B'

time_table2 = dict(sorted(time_table.items()))
first_point = list(time_table2.keys())
if time_table2[first_point[0]] == 'A':
	leader = 'A'
else:
	leader = 'B'

for k, v in time_table2.items():
	if k <= half_time_mark:
		if v == 'A':
			team_A_score += 1
			half_time_score += 1
		elif v == 'B':
			team_B_score += 1
			half_time_score += 1
		else:
			team_A_score += 1
			team_B_score += 1
			half_time_score += 2
	else:
		if v == 'A':
			team_A_score += 1
		elif v == 'B':
			team_B_score += 1
		else:
			team_A_score += 1
			team_B_score += 1

	if team_A_score < team_B_score and leader == 'A':
		turnarounds += 1
		leader = 'B'
	elif team_A_score > team_B_score and leader == 'B':
		turnarounds += 1
		leader = 'A'

print(half_time_score)
print(turnarounds)

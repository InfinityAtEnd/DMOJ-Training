# See the problem request at the link down below
# https://dmoj.ca/problem/wc16c2j1

# my solution:
N = int(input())
warriors = {}
for i in range(N):
	name, wins, los = input().split()
	if int(los) == 0:
		wins = int(wins)
		if wins not in warriors:
			warriors[wins] = [name]
		else:
			warriors[wins].append(name)

if len(warriors) == 0:
	mate = 'None'
else:
	max_wins = max(warriors.keys())
	mate = warriors[max_wins][0]

print(mate)

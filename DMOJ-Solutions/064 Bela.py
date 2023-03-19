# See the problem request at the link down below
# https://dmoj.ca/problem/coci15c6p1

# my solution:
points_table = {
	'A': [11, 11],
	'K': [4, 4],
	'Q': [3, 3],
	'J': [20, 2],
	'T': [10, 10],
	'9': [14, 0],
	'8': [0, 0],
	'7': [0, 0]
}
n, suit = input().split()
cards = [input() for x in range(int(n)*4)]
total_score = 0
for card in cards:
	if card[1] == suit:
		total_score += points_table[card[0]][0]
	else:
		total_score += points_table[card[0]][1]
print(total_score)

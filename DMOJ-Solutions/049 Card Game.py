# See the problem request at the link down below
# https://dmoj.ca/problem/ccc99s1

# my solution:
nr_cards = 52
high_cards = ['jack', 'queen', 'king', 'ace']
deck = []
for nr in range(nr_cards):
	deck.append(input())

A_score = 0
B_score = 0
current_player = 'A'
temp_score = 0


def find_high(lst):  # I check if the next 1, 2, 3 or 4 cards are high cards.... return true if ok to move on
	if 'jack' in lst:
		return False
	if 'queen' in lst:
		return False
	if 'king' in lst:
		return False
	if 'ace' in lst:
		return False
	return True


for i in range(nr_cards):
	if deck[i] == 'jack' and i < nr_cards - 1 and find_high(deck[i + 1:i + 2]):
		temp_score = 1
	elif deck[i] == 'queen' and i < nr_cards - 2 and find_high(deck[i + 1:i + 3]):
		temp_score = 2
	elif deck[i] == 'king' and i < nr_cards - 3 and find_high(deck[i + 1:i + 4]):
		temp_score = 3
	elif deck[i] == 'ace' and i < nr_cards - 4 and find_high(deck[i + 1:i + 5]):
		temp_score = 4
	if temp_score > 0:
		print(f'Player {current_player} scores {temp_score} point(s).')
	if current_player == 'A':
		A_score += temp_score
		temp_score = 0
		current_player = 'B'
	else:
		B_score += temp_score
		temp_score = 0
		current_player = 'A'

print(f'Player A: {A_score} point(s).')
print(f'Player B: {B_score} point(s).')

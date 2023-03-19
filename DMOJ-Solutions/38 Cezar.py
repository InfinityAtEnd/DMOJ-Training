# See the problem request at the link down below
# https://dmoj.ca/problem/coci17c1p1

# my solution:
deck_of_cards = [4, 4, 4, 4, 4, 4, 4, 4, 16, 4]

nr_of_cards_drawn = int(input())
cards_drawn = [int(input()) for card in range(nr_of_cards_drawn)]

splitting_card = 21 - sum(cards_drawn)

for card in cards_drawn:
	deck_of_cards[card - 2] -= 1

bigger = sum(deck_of_cards[splitting_card - 1:])
lower = sum(deck_of_cards) - bigger

if splitting_card <= 0:
	print('DOSTA')
else:
	if bigger >= lower:
		print('DOSTA')
	else:
		print('VUCI')

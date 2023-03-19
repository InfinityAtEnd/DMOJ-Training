# See the problem request at the link down below
# https://dmoj.ca/problem/acmtryouts1a

# my solution:
n = int(input())
opponent_plays = [input() for x in range(n)]
user_plays = []
for play in opponent_plays:
    if play == 'Rock':
        user_plays.append('Paper')
    elif play == 'Paper':
        user_plays.append('Scissors')
    elif play == 'Scissors':
        user_plays.append('Rock')
    elif play == 'Fox':
        user_plays.append('Foxen')
    else:
        break

for play in user_plays:
    print(play)

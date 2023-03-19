# See the problem request at the link down below
# https://dmoj.ca/problem/coci06c5p1

# my solution:
moves = input()
ball = 1
for move in moves:
    if move == 'A':
        if ball == 1:
            ball = 2
        elif ball == 2:
            ball = 1
    elif move == 'B':
        if ball == 2:
            ball = 3
        elif ball == 3:
            ball = 2
    else:
        if ball == 1:
            ball = 3
        elif ball == 3:
            ball = 1

print(ball)

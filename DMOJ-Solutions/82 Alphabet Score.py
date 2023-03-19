# See the problem request at the link down below
# https://dmoj.ca/problem/alphabetscore

# my solution:
S = input()
score = 0

for c in S:
    score += ord(c) - 96

print(str(score))

# See the problem request at the link down below
# https://dmoj.ca/problem/ccc18j2

# my solution:
parking_spaces = int(input())
yesterday = input()
today = input()
occupied = 0
for i in range(parking_spaces):
    if yesterday[i] == today[i] and (yesterday[i] == 'C' or today[i] == 'C'):
        occupied += 1
print(occupied)

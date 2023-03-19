# See the problem request at the link down below
# https://dmoj.ca/problem/dmpg19b3

# my solution:
message = input()
K = int(input())
ms = 'S' * K
if ms in message:
    print('Spamming')
else:
    print('All good')

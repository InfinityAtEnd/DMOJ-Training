# See the problem request at the link down below
# https://dmoj.ca/problem/ccc19j1

# my solution:
a3 = int(input())
a2 = int(input())
a1 = int(input())
b3 = int(input())
b2 = int(input())
b1 = int(input())
at = a3 * 3 + a2 * 2 + a1
bt = b3 * 3 + b2 * 2 + b1
if at == bt:
    print('T')
elif at > bt:
    print('A')
else:
    print('B')

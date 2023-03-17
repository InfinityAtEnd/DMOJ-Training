# See the problem request at the link down below
# https://dmoj.ca/problem/wc18c3j1

# my solution:
P = int(input())
B = int(input())
D = int(input())
bottlecaps = int(P/B)  # I used int() to round the result
leftovers = P - B * bottlecaps
print(bottlecaps * D + leftovers)

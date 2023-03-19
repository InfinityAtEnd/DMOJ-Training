# See the problem request at the link down below
# https://dmoj.ca/problem/dwite09c3p1

# my solution:
dataset = {}
for data in range(5):
    question = input()
    order = int(input())
    dataset[order] = question

keys = sorted(dataset)
for key in keys:
    print(dataset[key])

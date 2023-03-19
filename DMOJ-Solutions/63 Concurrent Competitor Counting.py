# See the problem request at the link down below
# https://dmoj.ca/problem/dmopc19c5p0

# my solution:
n, c = input().split()
names = []
scores = []
for i in range(int(n)):
    name, score = input().split()
    names.append(name)
    scores.append(int(score))
for i in range(int(n)):
    if scores[i] > int(c):
        print(f'{names[i]} will advance')
    else:
        print(f'{names[i]} will not advance')

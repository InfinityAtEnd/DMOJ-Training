# See the problem request at the link down below
# https://dmoj.ca/problem/wc97p4

# my solution:
N = int(input())
results = []
for i in range(N):
    line = input()
    finding = 'OK.'
    for ch in line:
        if line.count(ch) > 1:
            finding = 'Nope.'
    results.append(finding)

for rez in results:
    print(rez)

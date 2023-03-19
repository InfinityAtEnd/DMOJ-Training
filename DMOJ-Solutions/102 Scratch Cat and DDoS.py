# See the problem request at the link down below
# https://dmoj.ca/problem/mald1p1

# my solution:
N = int(input())
websites = [input() for n in range(N)]
hacked = set()
for i in range(N):
    if 'yubo' in websites[i]:
        if i == 0:
            if N > 2:
                hacked.add(websites[i])
                hacked.add(websites[i+1])
            else:
                hacked.add(websites[i])
        elif i == (N-1):
            hacked.add(websites[i-1])
            hacked.add(websites[i])
        else:
            hacked.add(websites[i-1])
            hacked.add(websites[i])
            hacked.add(websites[i+1])
hacked = sorted(hacked)
if len(hacked) > 0:
    for h in hacked:
        print(h)
else:
    print()

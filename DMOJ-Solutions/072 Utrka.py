# See the problem request at the link down below
# https://dmoj.ca/problem/coci14c2p2

# my solution:
N = int(input())
contestants = [input() for _ in range(N)]
finishers = [input() for _ in range(N - 1)]
counter = {}
for memb in contestants:
	if memb in counter:
		counter[memb] += 1
	else:
		counter[memb] = 1
for memb in finishers:
	if memb in counter:
		counter[memb] += 1
	else:
		counter[memb] = 1
for k, v in counter.items():
	if v % 2 == 1:
		print(k)
		break

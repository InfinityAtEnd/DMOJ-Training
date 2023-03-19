# See the problem request at the link down below
# https://dmoj.ca/problem/wc18c2j3

# my solution:
N = int(input())
n_names = [input() for _ in range(N)]
M = int(input())
m_names = [input() for _ in range(M)]

out = 0
for name in n_names:
	if name in m_names:
		out += 1

print(out)

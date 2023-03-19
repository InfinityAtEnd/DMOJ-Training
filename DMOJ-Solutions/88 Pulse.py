# See the problem request at the link down below
# https://dmoj.ca/problem/pulse

# my solution:
line = input().split()
N = int(line[0])
S = int(line[1])
T = int(line[2])
waves = []
for i in range(N):
	w = input()
	waves.append(int(w))

made_it_back = 0
for wave in waves:
	if S <= wave * 2 <= T:
		made_it_back += 1

print(made_it_back)

# See the problem request at the link down below
# https://dmoj.ca/problem/ccc11s1

# my solution:
N = int(input())
lines = []
t_letters = 0
s_letters = 0

for i in range(N):
	lines.append(input())

for i in lines:
	t_letters = t_letters + i.count('t') + i.count('T')
	s_letters = s_letters + i.count('s') + i.count('S')

if t_letters > s_letters:
	print('English')
else:
	print('French')

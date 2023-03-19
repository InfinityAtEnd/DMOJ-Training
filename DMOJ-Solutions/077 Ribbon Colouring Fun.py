# See the problem request at the link down below
# https://dmoj.ca/problem/dmopc17c4p1

# my solution:
N, Q = [int(x) for x in input().split()]
strokes = []
for i in range(Q):
	st = input().split()
	strokes.append([int(st[0]), int(st[1])])
strokes.sort()

rightest = 0
blues = 0

for stroke in strokes:
	if stroke[0] <= rightest:
		if stroke[1] > rightest:
			blues += stroke[1] - rightest
			rightest = stroke[1]
	else:
		blues += stroke[1] - stroke[0]
		rightest = stroke[1]

purples_left = N - blues
print(f'{purples_left} {blues}')

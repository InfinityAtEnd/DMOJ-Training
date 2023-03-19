# See the problem request at the link down below
# https://dmoj.ca/problem/ccc00s2

# my solution:
n = int(input())
streams = [int(input()) for i in range(n)]
flowing = True

while flowing:
	event = int(input())
	if event == 99:
		splits = int(input())
		percent = int(input())
		streams.insert(splits, round(streams[splits - 1] * (1 - percent / 100)))
		streams[splits - 1] *= percent / 100
	elif event == 88:
		joins = int(input())
		riv = streams.pop(joins - 1)
		streams[joins - 1] += riv
	elif event == 77:
		flowing = False

for stream in streams:
	print(f'{round(stream)} ', end='')

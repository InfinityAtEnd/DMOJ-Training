# See the problem request at the link down below
# https://dmoj.ca/problem/ccc08j2

# my solution:
play_list = 'ABCDE'
button = 0

while button != 4:
	button = int(input())
	press = int(input())
	for i in range(press):
		if button == 1:
			play_list = play_list[1:] + play_list[0]
		elif button == 2:
			play_list = play_list[-1] + play_list[:-1]
		elif button == 3:
			play_list = play_list[1] + play_list[0] + play_list[2:]

final_playlist = ''
for s in play_list:
	final_playlist = final_playlist + s + ' '

print(final_playlist[:-1])

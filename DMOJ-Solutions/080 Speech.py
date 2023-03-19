# See the problem request at the link down below
# https://dmoj.ca/problem/gfssoc1s2

# my solution:
N = int(input())
key_words = {}
for i in range(N):
	line = input().split()
	key_words[line[1]] = line[0]
mess = input()
dot = mess.count('.')

if dot > 0:
	message = mess[:-1].split()
	has_dot = '.'
else:
	message = mess.split()
	has_dot = ' '

new_message = []
for word in message:
	if word in key_words.keys():
		new_message.append(key_words[word])
	else:
		new_message.append(word)

if dot > 0:
	new_message[-1] += has_dot
for m in new_message:
	print(m, end=' ')

# See the problem request at the link down below
# https://dmoj.ca/problem/coci06c2p2

# my solution:
nr1, nr2, nr3 = input().split()
order = input()
numbers = []
numbers.append(int(nr1))
numbers.append(int(nr2))
numbers.append(int(nr3))
numbers.sort()
for letter in order:
	if letter == 'A':
		print(numbers[0], end=' ')
	elif letter == 'B':
		print(numbers[1], end=' ')
	else:
		print(numbers[2], end=' ')

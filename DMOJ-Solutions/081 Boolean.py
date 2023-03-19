# See the problem request at the link down below
# https://dmoj.ca/problem/boolean

# my solution:
string = input().split()
if string[-1] == 'False':
	start = False
else:
	start = True
nots = len(string[:-1])
if nots % 2 == 0:
	print(start)
else:
	print(not start)

# See the problem request at the link down below
# https://dmoj.ca/problem/test2017p3

# my solution:
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
N = input()
count = int(N)
i = 1
while count > days[i - 1]:
	count = count - days[i - 1]
	i += 1

print(f'{i:02d}/{count:02d}')

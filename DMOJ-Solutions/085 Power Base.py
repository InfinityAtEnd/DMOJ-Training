# See the problem request at the link down below
# https://dmoj.ca/problem/p124ex5

# my solution:
N = int(input())
results = []
for i in range(N):
	lin = input().split()
	x = float(lin[0])
	p = int(lin[1])
	results.append(x ** p)

for rez in results:
	print(f'{rez:.2f}')

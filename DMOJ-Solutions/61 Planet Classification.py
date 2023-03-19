# See the problem request at the link down below
# https://dmoj.ca/problem/globexcup19s1

# my solution:
n, k = input().split()
N = int(n)  # plates passed
K = int(k)  # planet types
visits = []
visited = {}
for i in range(N):
	visits.append(input())

for visit in visits:
	if visit not in visited:
		print(0)
		visited[visit] = 1
	else:
		print(visited[visit])
		visited[visit] += 1

print(len(visited))

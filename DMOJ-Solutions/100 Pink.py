# See the problem request at the link down below
# https://dmoj.ca/problem/valentines19j2

# my solution:
N = int(input())
pinks = 0
for l in range(N):
	R, G, B = input().split()
	if (240 <= int(R) <= 255) and (int(G) <= 200) and (95 <= int(B) <= 220):
		pinks += 1

print(pinks)

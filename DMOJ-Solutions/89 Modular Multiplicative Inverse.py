# See the problem request at the link down below
# https://dmoj.ca/problem/modinv

# my solution:
line = input().split()
N = int(line[0])
M = int(line[1])
a, b = 0, 1


def gcde(N, M):  # Extended Euclid Algorithm
	global a, b
	if N == 0:
		a = 0
		b = 1
		return M
	gcd = gcde(M % N, N)
	a1 = a
	b1 = b
	a = b1 - (M // N) * a1
	b = a1
	return gcd


def modinv(N, M):
	g = gcde(N, M)
	if g != 1:
		print('No INVERSE')
	else:
		result = (a % M + M) % M
		print(result)


modinv(N, M)

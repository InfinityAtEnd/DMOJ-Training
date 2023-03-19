# See the problem request at the link down below
# https://dmoj.ca/problem/coci10c3p1

# my solution:
def val(A, B, C, D):
	return int(A) / int(C) + int(B) / int(D)


def max_rotations(A, B, C, D):
	va0 = val(A, B, C, D)
	va1 = val(C, A, D, B)
	va2 = val(D, C, B, A)
	va3 = val(B, D, A, C)
	ma = max(va0, va1, va2, va3)
	if ma == va0:
		return 0
	elif ma == va1:
		return 1
	elif ma == va2:
		return 2
	else:
		return 3


A, B = input().split()
C, D = input().split()

print(max_rotations(A, B, C, D))

# See the problem request at the link down below
# https://dmoj.ca/problem/ccc07j1

# my solution:
A = int(input())
B = int(input())
C = int(input())
if A > B:
	if A > C:
		if B > C:
			print(B)
		else:
			print(C)
	else:
		print(A)
else:
	if B > C:
		if A > C:
			print(A)
		else:
			print(C)
	else:
		print(B)

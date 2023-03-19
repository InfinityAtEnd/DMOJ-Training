# See the problem request at the link down below
# https://dmoj.ca/problem/coci13c3p1

# my solution:
K = int(input())

letters_A = 1
letters_B = 0

for i in range(K):
	new_A = letters_B
	new_B = letters_B + letters_A
	letters_A = new_A
	letters_B = new_B

print(f'{letters_A} {letters_B}')

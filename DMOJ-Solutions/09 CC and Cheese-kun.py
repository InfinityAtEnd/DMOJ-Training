# See the problem request at the link down below
# https://dmoj.ca/problem/dmopc16c1p0

# my solution:
W = int(input())  # width of the pizza
C = int(input())  # percentage of pizza covered in extra cheese

if W == 3 and C >= 95:
	M = 'absolutely'
elif W == 1 and C <= 50:
	M = 'fairly'
else:
	M = 'very'

print(f'C.C. is {M} satisfied with her pizza.')

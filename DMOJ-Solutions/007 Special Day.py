# See the problem request at the link down below
# https://dmoj.ca/problem/ccc15j1

# my solution:
month = int(input())
day = int(input())

if month < 2:
	print('Before')
elif month > 2:
	print('After')
else:
	if day < 18:
		print('Before')
	elif day > 18:
		print('After')
	else:
		print('Special')


# a second solution that I made:
month = int(input())
day = int(input())

if month < 2 or (month == 2 and day < 18):
	print('Before')
elif month > 2 or (month == 2 and day > 18):
	print('After')
else:
	print('Special')

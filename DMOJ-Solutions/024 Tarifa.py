# See the problem request at the link down below
# https://dmoj.ca/problem/coci16c1p1

# my solution:
monthly_data = int(input())
N = int(input())
data_spent = []
data_left = monthly_data
for i in range(N):
	data_spent.append(int(input()))

for data in data_spent:
	data_left = data_left + monthly_data
	if data < data_left:
		data_left = data_left - data
	else:
		data_left = 0

print(data_left)

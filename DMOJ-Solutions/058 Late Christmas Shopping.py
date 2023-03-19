# See the problem request at the link down below
# https://dmoj.ca/problem/year2016p1

# my solution:
shopping_bags = int(input())
bags = [input().split() for x in range(shopping_bags)]
output = 'NO'
for i in range(len(bags)):
	for j in range(1, len(bags[i])):
		for bag in bags[i + 1:]:
			if bags[i][j] in bag[1:]:
				output = 'YES'
				break

print(output)

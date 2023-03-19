# See the problem request at the link down below
# https://dmoj.ca/problem/ccc13s1

# my solution:
start_year = int(input())


def distinct_year(year):
	numbers = [int(nr) for nr in str(year)]
	for nr in numbers:
		if numbers.count(nr) > 1:
			return False
	return True


next_year = start_year
found = False

while not found:
	next_year += 1
	if distinct_year(next_year):
		found = True
		break
	else:
		found = False

print(next_year)

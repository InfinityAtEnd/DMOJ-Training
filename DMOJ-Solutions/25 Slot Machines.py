# See the problem request at the link down below
# https://dmoj.ca/problem/ccc00s1

# my solution:
quarters = int(input())
machine1_roll = int(input())
machine2_roll = int(input())
machine3_roll = int(input())
played = 0

while quarters:
	quarters -= 1
	played += 1
	if (played % 3) == 1:
		machine1_roll += 1
		if (machine1_roll % 35) == 0:
			quarters += 30
	elif (played % 3) == 2:
		machine2_roll += 1
		if (machine2_roll % 100) == 0:
			quarters += 60
	elif (played % 3) == 0:
		machine3_roll += 1
		if (machine3_roll % 10) == 0:
			quarters += 9

print(f'Martha plays {played} times before going broke.')

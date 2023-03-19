# See the problem request at the link down below
# https://dmoj.ca/problem/ecoo19r1p1

# my solution:
laundry_days = []
for i in range(1):
	dataset = input().split()
	clean_tshirt = int(dataset[0])
	d_days = int(dataset[2])
	d_w_e = [int(i) for i in input().split()]
	d_w_e.sort()
	total_shirt = clean_tshirt
	laundry_days.append(0)
	current_day = i

	for day in range(1, d_days + 1):
		if clean_tshirt == 0:
			laundry_days[current_day] += 1
			clean_tshirt = total_shirt
		if day in d_w_e:
			gained_tshirt = d_w_e.count(day)
			total_shirt += gained_tshirt
			clean_tshirt += gained_tshirt
		clean_tshirt -= 1

for times in laundry_days:
	print(times)

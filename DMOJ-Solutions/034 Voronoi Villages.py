# See the problem request at the link down below
# https://dmoj.ca/problem/ccc18s1

# my solution:
nr_villages = int(input())
villages_locations = [int(input()) for i in range(nr_villages)]
villages_sizes = []
villages_locations.sort()
for i in range(1, len(villages_locations)-1):
    villages_sizes.append((villages_locations[i+1] - villages_locations[i-1]) / 2)
villages_sizes.sort()
print(round(villages_sizes[0], 1))

# See the problem request at the link down below
# https://dmoj.ca/problem/coci18c4p1

# my solution:
wand_owner = input()
nr_of_duels = int(input())
wand_owners = {}
wand_owners[wand_owner] = True
duels_order = []
for i in range(nr_of_duels):
    Z1, Z2 = input().split() # Z1 is the new owner of the wand
    duels_order.append((Z1, Z2))
for i in duels_order:
    if i[1] == wand_owner:
        wand_owner = i[0]
        wand_owners[wand_owner] = True

print(wand_owner.capitalize())
print(len(wand_owners))

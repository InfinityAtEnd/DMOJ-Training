# See the problem request at the link down below
# https://dmoj.ca/problem/ecoo19r2p1

# my solution:
def clean(adr):
	plus_index = adr.find('+')  # remove everything from + to @
	if plus_index != -1:
		at_index = adr.find('@')
		adr = adr[:plus_index] + adr[at_index:]
	at_index = adr.find('@')  # update the @ index
	address_name = ''
	for k in range(at_index):  # removes all the dots up to @
		if adr[k] != '.':
			address_name += adr[k]
	almost_final_address = address_name + adr[at_index:]
	final_address = almost_final_address.lower()  # change all upper case letters
	return final_address


for data in range(10):
	N = int(input())
	addresses = set()
	for i in range(N):
		address = input()
		address = clean(address)
		addresses.add(address)
	print(len(addresses))

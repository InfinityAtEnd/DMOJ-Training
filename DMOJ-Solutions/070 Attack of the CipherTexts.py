# See the problem request at the link down below
# https://dmoj.ca/problem/ccc06s2

# my solution:
mes = input()
cyp = input()
code = input()
cipher = {}
for i in range(len(mes)):
	cipher[cyp[i]] = mes[i]
output = ''
for c in code:
	output += cipher.get(c, '.')

print(output)

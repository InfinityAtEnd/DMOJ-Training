# See the problem request at the link down below
# https://dmoj.ca/problem/dt16l1p2

# my solution:
nu = abs(int(input()))
num = str(nu)
number = len(num)
fax_number = 'false'
fibonacci_number = 0
aux = 0
bux = 1
while True:
	fibonacci_number = aux + bux
	aux = bux
	bux = fibonacci_number
	if number == fibonacci_number:
		fax_number = 'true'
		break
	elif number < fibonacci_number:
		break

print(fax_number)

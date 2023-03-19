# See the problem request at the link down below
# https://dmoj.ca/problem/coci08c3p2

# my solution:
luka_code = input()
true_code = ''
vowels = 'aeiou'
i = 0
while i < len(luka_code):
	true_code = true_code + luka_code[i]
	if luka_code[i] in vowels:
		i += 3
	else:
		i += 1

print(true_code)

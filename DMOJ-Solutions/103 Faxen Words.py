# See the problem request at the link down below
# https://dmoj.ca/problem/dt16l1p3

# my solution:
word = input()
vowels = 'aeiouAEIOU'
noun = False
verb = False
adjective = False

if word[0].isupper():
	if word[0] in vowels:
		verb = True
	else:
		noun = True
else:
	adjective = True

if noun:
	print('noun')
	if word[3] in vowels:
		print('fancy noun')
if verb:
	print('verb')
	if word[4] in 'xyzq':
		print('boring verb')
if adjective:
	print('adjective')
	if word[2] not in vowels:
		print('odd adjective')

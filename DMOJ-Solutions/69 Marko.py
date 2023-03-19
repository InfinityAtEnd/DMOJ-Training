# See the problem request at the link down below
# https://dmoj.ca/problem/coci15c2p1

# my solution:
keypad = {
	'1': '',
	'2': 'abc',
	'3': 'def',
	'4': 'ghi',
	'5': 'jkl',
	'6': 'mno',
	'7': 'pqrs',
	'8': 'tuv',
	'9': 'wxyz'
}
N = int(input())
words = [input() for n in range(N)]
digits = input()
output = 0


def word_is_typed(word, digits):
	word_is = True
	if len(word) != len(digits):
		word_is = False
	else:
		for i in range(len(word)):
			if word[i] not in keypad[digits[i]]:
				word_is = False
				break
	return word_is


for word in words:
	if word_is_typed(word, digits):
		output += 1

print(output)

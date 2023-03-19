# See the problem request at the link down below
# https://dmoj.ca/problem/coci17c2p2

# my solution:
K, N = [int(x) for x in input().split()]
words = {}
next_word = {}
for i in range(K):
	word = input()
	if word[0] not in words:
		words[word[0]] = [word]
	else:
		words[word[0]] += [word]

for k, v in words.items():
	words[k] = sorted(v)
	next_word[k] = 0

letters = [input() for x in range(N)]
output_words = []

for letter in letters:
	words_to_choose = words[letter]
	current_index = next_word[letter]
	next_word_to_print = words_to_choose[current_index]
	output_words.append(next_word_to_print)
	if next_word[letter] == len(words[letter]) - 1:
		next_word[letter] = 0
	else:
		next_word[letter] += 1

for word in output_words:
	print(word)

# See the problem request at the link down below
# https://dmoj.ca/problem/cco99p2

# my solution:
N = int(input())
output_words = []
output_k = []


def invert_dictionary(dictionary):
	inverted = {}
	for key in dictionary:
		num = dictionary[key]
		if num in inverted:
			inverted[num].append(key)
		else:
			inverted[num] = [key]
	return inverted


def suffixed(number):
	s = str(number)
	if s[-1] == '1' and s[-2:] != '11':
		return s + 'st'
	elif s[-1] == '2' and s[-2:] != '12':
		return s + 'nd'
	elif s[-1] == '3' and s[-2:] != '13':
		return s + 'rd'
	else:
		return s + 'th'


def occurrence_words(sorted_words, k):
	nums = list(sorted_words.keys())
	nums.sort(reverse=True)
	total = 0
	i = 0
	done = False
	while i < len(nums) and not done:
		num = nums[i]
		if total + len(sorted_words[num]) >= k:
			done = True
		else:
			total += len(sorted_words[num])
			i += 1
	if total == k - 1 and i < len(nums):
		return sorted_words[nums[i]]
	else:
		return []


for data in range(N):
	m, k = [int(x) for x in input().split()]
	words = {}
	output_k.append(k)
	for i in range(m):
		word = input()
		if word in words:
			words[word] += 1
		else:
			words[word] = 1
	sorted_words = invert_dictionary(words)
	chosen_words = occurrence_words(sorted_words, k)
	output_words.append(chosen_words)

for i in range(N):
	print(f'{suffixed(output_k[i])} most common word(s):')
	for word in output_words[i]:
		print(word)
	print()

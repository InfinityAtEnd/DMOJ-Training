# See the problem request at the link down below
# https://dmoj.ca/problem/ccc02j2

# my solution:
stops = False
vowels = 'aeiouy'
user_words = []
word_insert = ''
while not stops:
    word = input()
    if word == 'quit!':
        stops = True
    elif len(word) > 4 and 'or' in word:
        if word[-3] in vowels and word[-2:] == 'or':
            user_words.append(word)
        elif word[-3] not in vowels and word[-2:] == 'or':
            word_insert = word[:-1] + 'u' + word[-1]
            user_words.append(word_insert)
        else:
            user_words.append(word)
    else:
        user_words.append(word)

for w in user_words:
    print(w)

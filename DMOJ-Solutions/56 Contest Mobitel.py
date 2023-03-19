# See the problem request at the link down below
# https://dmoj.ca/problem/coci14c2p1

# my solution:
phone = ['0', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
marko = input().split()
word = input()
marko_phone = []
combination = '.'
for nr in marko:
    marko_phone.append(phone[int(nr)])

for l in word:
    for i in range(len(marko_phone)):
        if l in marko_phone[i]:
            for j in range(len(marko_phone[i])):
                if l == marko_phone[i][j]:
                    if combination[-1] == str(i+1):
                        combination += '#'
                        combination += str(i+1)*(j+1)
                    else:
                        combination += str(i+1)*(j+1)

print(combination[1:])

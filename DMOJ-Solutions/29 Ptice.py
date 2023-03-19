# See the problem request at the link down below
# https://dmoj.ca/problem/coci08c1p2

# my solution:
adrian_choice = 'ABC'
bruno_choice = 'BABC'
goran_choice = 'CCAABB'
n = int(input())
correct_answer = input()
ad = ''
br = ''
go = ''
while len(ad) < n:
    ad = ad + adrian_choice
while len(br) < n:
    br = br + bruno_choice
while len(go) < n:
    go = go + goran_choice

max_c_answers = 0
answers = [0, 0, 0]

for i in range(n):
    if correct_answer[i] == ad[i]:
        answers[0] += 1
    if correct_answer[i] == br[i]:
        answers[1] += 1
    if correct_answer[i] == go[i]:
        answers[2] += 1

if answers[0] >= answers[1]:
    if answers[0] >= answers[2]:
        max_c_answers = answers[0]
    else:
        max_c_answers = answers[2]
else:
    if answers[1] >= answers[2]:
        max_c_answers = answers[1]
    else:
        max_c_answers = answers[2]

print(max_c_answers)
if answers[0] == max_c_answers:
    print('Adrian')
if answers[1] == max_c_answers:
    print('Bruno')
if answers[2] == max_c_answers:
    print('Goran')

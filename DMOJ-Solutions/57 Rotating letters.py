# See the problem request at the link down below
# https://dmoj.ca/problem/ccc13j2

# my solution:
rot_let = 'IOSHZXN'
word = input()
output = 'YES'
for w in word:
    if w not in rot_let:
        output = 'NO'
        break

print(output)

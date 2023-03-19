# See the problem request at the link down below
# https://dmoj.ca/problem/wc17c3j3

# my solution:
password = input()
validation = 'Invalid'
lowers = 0
uppers = 0
digits = 0

if 8 <= len(password) <= 12:
    for i in password:
        if i.islower():
            lowers += 1
        elif i.isupper():
            uppers += 1
        elif 0 <= int(i) <= 9:
            digits += 1
        else:
            break

if lowers >= 3 and uppers >= 2 and digits >= 1:
    validation = 'Valid'

print(validation)

# See the problem request at the link down below
# https://dmoj.ca/problem/ucc21p1

# my solution:
coins = ['4', '6', '25']
scanning = input()
counterfeiter = 0
for i in range(len(scanning)):
    if i == (len(scanning) - 1):
        if scanning[i] == '2':
            counterfeiter += 1
    else:
        if scanning[i] == '2' and scanning[i+1] != '5':
            counterfeiter += 1
print(counterfeiter)

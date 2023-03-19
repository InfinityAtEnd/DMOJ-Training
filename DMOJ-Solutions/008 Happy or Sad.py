# See the problem request at the link down below
# https://dmoj.ca/problem/ccc15j2

# my solution:
line = input()
sad = line.count(':-(')
happy = line.count(':-)')
if sad == happy and sad != 0 and happy != 0:
    print('unsure')
elif sad > happy:
    print('sad')
elif sad < happy:
    print('happy')
else:
    print('none')

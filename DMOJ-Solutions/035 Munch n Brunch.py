# See the problem request at the link down below
# https://dmoj.ca/problem/ecoo17r1p1

# my solution:
strips = [[input() for i in range(3)] for j in range(10)]
funding = []
for event in strips:
    students = event[1].split(' ')
    attendants = []
    attendants.append(int(int(event[2]) * float(students[0])))
    attendants.append(int(int(event[2]) * float(students[1])))
    attendants.append(int(int(event[2]) * float(students[2])))
    attendants.append(int(int(event[2]) * float(students[3])))
    lefts = int(event[2]) - sum(attendants)
    most = max(attendants)
    most_index = attendants.index(most)
    attendants[most_index] += lefts
    money_raised = (attendants[0] * 12) + (attendants[1] * 10) + (attendants[2] * 7) + (attendants[3] * 5)
    if money_raised/2 >= int(event[0]):
        funding.append('NO')
    else:
        funding.append('YES')

for output in funding:
    print(output)

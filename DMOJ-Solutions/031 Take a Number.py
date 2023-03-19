# See the problem request at the link down below
# https://dmoj.ca/problem/ecoo13r1p1

# my solution:
next_number = int(input())
students_late = 0
students_in_line = 0
close_status = []
while (activity := input()) != 'EOF':
    if activity == 'TAKE':
        if next_number == 999:
            next_number = 1
        else:
            next_number += 1
        students_late += 1
        students_in_line += 1
    elif activity == 'SERVE':
        students_in_line -= 1
    elif activity == 'CLOSE':
        close_status.append((students_late, students_in_line, next_number))
        students_in_line = 0
        students_late = 0

for i in close_status:
    print(f'{i[0]} {i[1]} {i[2]}')

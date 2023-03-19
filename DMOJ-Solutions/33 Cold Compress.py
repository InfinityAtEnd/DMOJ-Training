# See the problem request at the link down below
# https://dmoj.ca/problem/ccc19j3

# my solution:
num = int(input())
lines = [input() for i in range(num)]
output = {}
for i, string in enumerate(lines):
    counted_list = [string[0], 1]
    for j in range(1, len(string)):
        if string[j] != counted_list[-2]:
            counted_list.append(string[j])
            counted_list.append(1)
        else:
            counted_list[-1] += 1
    output[i] = counted_list

for line in output.values():
    for i in range(0, len(line), 2):
        print(f'{line[i+1]} {line[i]} ', end='')
    print()

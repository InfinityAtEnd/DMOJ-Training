# See the problem request at the link down below
# https://dmoj.ca/problem/dmopc14c7p2

# my solution:
nr_of_readings = int(input())
readings_str = input().split()
readings = [int(x) for x in readings_str]
min_value = min(readings)
min_index = readings.index(min_value)
max_value = max(readings)
max_index = readings.index(max_value)
tide_level = max_value - min_value
output = True

if min_index < max_index:
    for level in readings[min_index+1:max_index+1]:
        if level < min_value:
            output = False
            break
        else:
            min_value = level
else:
    output = False

if output:
    print(tide_level)
else:
    print('unknown')

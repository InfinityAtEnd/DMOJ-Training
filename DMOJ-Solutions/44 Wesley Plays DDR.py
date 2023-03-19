# See the problem request at the link down below
# https://dmoj.ca/problem/wac3p3

# my solution:
wesley_moves = input()
nr_of_combos = int(input())
unsorted_combo_list = {}
combo_list = {}
for_sorting_combo_list = []
move_used = [0 for m in wesley_moves]

for i in range(nr_of_combos):
    c, p = input().split()
    unsorted_combo_list[c] = int(p)
    for_sorting_combo_list.append(c)

for_sorting_combo_list.sort(key=len, reverse=True)
for key in for_sorting_combo_list:
    combo_list[key] = unsorted_combo_list[key]

score = 0
current_move = 0
longest_combo = ''
combo_found = False
while current_move < len(wesley_moves):
    for c, p in combo_list.items():
        max_move = current_move + len(c)
        if wesley_moves[current_move:max_move] == c and 1 not in move_used[current_move:max_move] and len(c) > len(longest_combo):
            for i in range(current_move, max_move):
                move_used[i] = 1
            score += p
            current_move += len(c)
            combo_found = True
            break
        else:
            longest_combo = ''
    if combo_found:
        combo_found = False
    else:
        current_move += 1

score += len(wesley_moves)
print(score)

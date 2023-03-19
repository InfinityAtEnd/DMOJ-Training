# See the problem request at the link down below
# https://dmoj.ca/problem/ccc07j3

# my solution:
boxes = [100, 500, 1_000, 5_000, 10_000, 25_000, 50_000, 100_000, 500_000, 1_000_000]
boxes_chosen = int(input())
banker_info = [int(input()) for i in range(boxes_chosen + 1)]
banker_offer = banker_info.pop(-1)
banker_info.sort(reverse=True)

for i in range(len(banker_info)):
	boxes.remove(boxes[banker_info[i] - 1])

if (sum(boxes) / len(boxes)) <= banker_offer:
	print('deal')
else:
	print('no deal')

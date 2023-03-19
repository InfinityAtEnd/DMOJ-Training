# See the problem request at the link down below
# https://dmoj.ca/problem/nccc6s1

# my solution:
N = int(input())
marks = [int(input()) for x in range(N)]
average_mark = sum(marks) / len(marks)
print(f'{average_mark:.1f}')

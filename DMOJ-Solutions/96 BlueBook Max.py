# See the problem request at the link down below
# https://dmoj.ca/problem/p171ex6a

# my solution:
import sys

input = sys.stdin.readline

T = int(input())
numbers = [float(input()) for x in range(T)]
result = max(numbers)
print(f'{result:0.4f}')

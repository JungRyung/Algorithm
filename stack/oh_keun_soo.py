'''
TITLE   : 오큰수
URL     : https://www.acmicpc.net/problem/17298
DATE    : 21.10.09
'''
import sys
from collections import deque

n = int(sys.stdin.readline())
nums = deque(map(int, sys.stdin.readline().split()))

s = []
ans = []
for _ in range(n):
    curr = nums.popleft()
    depth = 0
    ohkeunsoo = -1
    while nums:
        next = nums.popleft()
        if next > curr:
            ohkeunsoo = next
            nums.appendleft(next)
            break
        else:
            s.append(next)
            depth += 1
    for __ in range(depth):
        nums.appendleft(s.pop())
    print(ohkeunsoo,end=' ')
print()
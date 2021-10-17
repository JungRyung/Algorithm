'''
TITLE   : 최솟값 찾기
URL     : https://www.acmicpc.net/problem/11003
DATE    : 21.10.17
'''
import sys
from collections import deque

n, l = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
dq = deque()
ans = []
for i in range(n):
    while dq and dq[-1][1] > nums[i]:
        dq.pop()
    while dq and i - dq[0][0] >= l:
        dq.popleft()

    dq.append((i, nums[i]))
    ans.append(dq[0][1])
print(*ans)
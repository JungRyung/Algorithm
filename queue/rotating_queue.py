'''
TITLE   : 회전하는 큐
URL     : https://www.acmicpc.net/problem/1021
DATE    : 21.11.01
'''
import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
deq = [i for i in range(1,n+1)]
deq = deque(deq)
cnt = 0

for num in nums:
    while True:
        if deq[0] == num:
            deq.popleft()
            break
        if deq.index(num) <= len(deq) - deq.index(num):
            deq.append(deq.popleft())
            cnt += 1
        else:
            deq.appendleft(deq.pop())
            cnt += 1
print(cnt)
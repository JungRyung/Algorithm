'''
TITLE   : 숨바꼭질 2
URL     : https://www.acmicpc.net/problem/12851
DATE    : 21.08.06
'''
import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
q = deque()
q.append(n)
visit = [-1] * 100001
visit[n] = 0
cnt = 0
while q:
    curr = q.popleft()
    if curr == k:
        cnt += 1
    for next in [curr-1, curr+1, curr*2]:
        if 0<=next<=100000 and (visit[next] == -1 or visit[next] >= visit[curr]+1):
            q.append(next)
            visit[next] = visit[curr]+1
print(visit[k])
print(cnt)
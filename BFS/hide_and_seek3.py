'''
TITLE   : 숨바꼭질 3
URL     : https://www.acmicpc.net/problem/13549
DATE    : 21.10.08
'''
import sys
from collections import deque

def bfs(start):
    q = deque()
    q.append(start)
    visit[start] = True
    time[start] = 0
    while q:
        curr = q.popleft()
        if curr * 2 <=100000 and visit[curr*2] == False:
            q.appendleft(curr * 2)
            visit[curr * 2] = True
            time[curr * 2] = time[curr]
        if curr + 1 <=100000 and visit[curr+1] == False:
            q.append(curr + 1)
            visit[curr + 1] = True
            time[curr + 1] = time[curr] + 1
        if curr - 1 >= 0 and visit[curr-1] == False:
            q.append(curr - 1)
            visit[curr - 1] = True
            time[curr - 1] = time[curr] + 1

visit = [False] * 100001
time = [0] * 100001

n, k = map(int, sys.stdin.readline().split())

bfs(n)

print(time[k])
'''
TITLE   : 엘리베이터
URL     : https://www.acmicpc.net/problem/5014
DATE    : 21.08.26
'''
import sys
from collections import deque

f, s, g, u, d = map(int, sys.stdin.readline().split())


def bfs():
    visit = [False]*1000001
    q = deque()
    visit[s] = True
    q.append((s,0))
    while q:
        curr, t = q.popleft()
        if curr == g:
            return t
        next = curr + u
        if 1<=next<=f and not visit[next]:
            visit[next] = True
            q.append((next, t+1))
        next = curr - d
        if 1<=next<=f and not visit[next]:
            visit[next] = True
            q.append((next, t+1))
    return "use the stairs"

print(bfs())
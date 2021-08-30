'''
TITLE   : 촌수계산
URL     : https://www.acmicpc.net/problem/2644
DATE    : 21.08.30
'''
import sys
from collections import deque

n = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
a, b = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())
for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

def bfs(start, end):
    visit = [False] * (n+1)
    q = deque()
    visit[start] = True
    q.append((start, 0))
    while q:
        curr, t = q.popleft()
        if curr == end:
            return t
        for next in graph[curr]:
            if not visit[next]:
                visit[next] = True
                q.append((next, t+1))
    return -1

print(bfs(a,b))
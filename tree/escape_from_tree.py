'''
TITLE   : 나무 탈출
URL     : https://www.acmicpc.net/problem/15900
DATE    : 21.07.21
'''
import sys

n = int(sys.stdin.readline())

graph = [[] for _ in range(n+1)]
level = [0] * (n+1)
visit = [False] * (n+1)

for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

# DFS
s = []
s.append(1)
total_step = 0
while s:
    curr = s.pop()
    visit[curr] = True
    if curr != 1 and len(graph[curr]) == 1:
        total_step += level[curr]
        continue
    for next in graph[curr]:
        if not visit[next]:
            level[next] = level[curr] + 1
            s.append(next)
if total_step%2:
    print("Yes")
else:
    print("No")

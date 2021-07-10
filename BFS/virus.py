'''
Title   : 바이러스
URL     : https://www.acmicpc.net/problem/2606
Date    : 21.07.10
'''
import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

visit = [False] * (n+1)
visit[1] = True
q = [1]
cnt = 0
while q:
    tmp = q.pop(0)
    for next in graph[tmp]:
        if not visit[next]:
            q.append(next)
            visit[next] = True
            cnt += 1
print(cnt)
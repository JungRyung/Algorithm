'''
TITLE   : 이분 그래프
URL     : https://www.acmicpc.net/problem/1707
DATE    : 21.08.01
'''
import sys

def bfs(start):
    q = []
    mark[start] = 1
    q.append(start)
    while q:
        curr = q.pop(0)
        for next in graph[curr]:
            if mark[curr] == mark[next]:
                return False
            if mark[next] == 0:
                mark[next] = -mark[curr]
                q.append(next)
    return True
for _ in range(int(sys.stdin.readline())):
    v, e = map(int, sys.stdin.readline().split())
    graph = [[] for i in range(v+1)]
    for i in range(e):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    mark = [0] * (v+1)

    bipartite = True
    for i in range(1,v+1):
        if mark[i] == 0 and not bfs(i):
            bipartite = False
            break
    
    if bipartite:
        print("YES")
    else:
        print("NO")
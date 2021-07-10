'''
Title   : BFS와 DFS
URL     : https://www.acmicpc.net/problem/1260
'''
import sys

def dfs(graph, start):
    global n
    visit = [False] * (n+1)
    s = []
    visit[start] = True
    s.append(start)
    print(start, end=' ')
    while s:
        tmp = s[-1]
        searched = False
        for next in graph[tmp]:
            if not visit[next]:
                s.append(next)
                visit[next] = True
                searched = True
                print(next, end=' ')
                break
        if not searched:
            s.pop()
    print()

def bfs(graph, start):
    global n
    visit = [False] * (n+1)
    q = []
    visit[start] = True
    q.append(start)
    while q:
        tmp = q.pop(0)
        print(tmp, end=' ')
        for next in graph[tmp]:
            if not visit[next]:
                q.append(next)
                visit[next] = True
    print()

n, m, v = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(n):
    graph[i].sort()

dfs(graph,v)
bfs(graph,v)
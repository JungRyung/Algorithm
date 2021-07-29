'''
TITLE   : 중량 제한
URL     : https://www.acmicpc.net/problem/1939
DATE    : 21.07.29
'''
import sys
import heapq
INF = 10e9+1

n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((c,b))
    graph[b].append((c,a))
v1, v2 = map(int, sys.stdin.readline().split())

weight = [0] * (n+1)
weight[v1] = INF
q = []
heapq.heappush(q,(INF,v1))
while q:
    w, curr = heapq.heappop(q)
    if weight[curr] > w:
        continue
    for next in graph[curr]:
        nw, nnode = next
        cost = min(w,nw)
        if cost > weight[nnode]:
            weight[nnode] = cost
            heapq.heappush(q,(cost,nnode))

print(weight[v2])
        
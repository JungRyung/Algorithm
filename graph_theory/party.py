'''
TITLE   : 파티
URL     : https://www.acmicpc.net/problem/1238
DATE    : 21.07.11
'''
import sys
import heapq
INF = 1e9
n, m, x = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
distance = [[INF]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a, b, t = map(int, sys.stdin.readline().split())
    graph[a].append((b,t))

def dijstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start][start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[start][now] < dist:
            continue
        for next in graph[now]:
            cost = distance[start][now] + next[1]
            if cost < distance[start][next[0]]:
                distance[start][next[0]]= cost
                heapq.heappush(q,(cost,next[0]))

for i in range(1,n+1):
    dijstra(i)
    
max_dist = 0
for i in range(1,n+1):
    if i != x:
        max_dist = max(max_dist, distance[i][x] + distance[x][i])
print(max_dist)
'''
TITLE   : 특정한 최단 경로
URL     : https://www.acmicpc.net/problem/1504
DATE    : 21.09.09
'''
import sys
import heapq
INF = 10e9

n, e = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
v1, v2 = map(int, sys.stdin.readline().split())

# 1에서 출발하는 다익스트라
dist = [INF] * (n+1)
q = []
dist[1] = 0
heapq.heappush(q,(0,1))
while q:
    distance, curr = heapq.heappop(q)
    if dist[curr] < distance:
        continue
    for next_node in graph[curr]:
        next, next_dist = next_node
        cost = distance + next_dist
        if dist[next] > cost:
            dist[next] = cost
            heapq.heappush(q,(cost,next))

# v1에서 출발하는 다익스트라
dist1 = [INF] * (n+1)
q = []
dist1[v1] = 0
heapq.heappush(q,(0,v1))
while q:
    distance, curr = heapq.heappop(q)
    if dist1[curr] < distance:
        continue
    for next_node in graph[curr]:
        next, next_dist = next_node
        cost = distance + next_dist
        if dist1[next] > cost:
            dist1[next] = cost
            heapq.heappush(q,(cost,next))

# v2에서 출발하는 다익스트라
dist2 = [INF] * (n+1)
q = []
dist2[v2] = 0
heapq.heappush(q,(0,v2))
while q:
    distance, curr = heapq.heappop(q)
    if dist2[curr] < distance:
        continue
    for next_node in graph[curr]:
        next, next_dist = next_node
        cost = distance + next_dist
        if dist2[next] > cost:
            dist2[next] = cost
            heapq.heappush(q,(cost,next))
min_dist = min(dist[v1]+ dist1[v2] + dist2[n], dist[v2] + dist2[v1] + dist1[n])
if min_dist >= INF:
    print(-1)
else:
    print(min_dist)
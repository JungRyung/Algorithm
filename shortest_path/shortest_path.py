'''
TITLE   : 최단경로
URL     : https://www.acmicpc.net/problem/1753
DATE    : 21.09.07
'''
import sys
import heapq
INF = 10e9

v, e = map(int, sys.stdin.readline().split())
start = int(sys.stdin.readline())

graph = [[] for _ in range(v+1)]
for _ in range(e):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((v,w))
    
distance = [INF] * (v+1)
distance[start] = 0
q = []
heapq.heappush(q, (0,start))

while q:
    dist, curr = heapq.heappop(q)
    if distance[curr] < dist:
        continue
    for next in graph[curr]:
        next_node, w = next
        cost = dist + w
        if distance[next_node] > cost:
            distance[next_node] = cost
            heapq.heappush(q,(cost,next_node))
for i in range(1,v+1):
    print(distance[i])
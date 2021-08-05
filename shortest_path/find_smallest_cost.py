'''
TITLE   : 최소 비용 구하기
URL     : https://www.acmicpc.net/problem/1916
DATE    : 21.08.05
'''
import sys
import heapq
INF = 10e9

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    start, dest, cost = map(int, sys.stdin.readline().split())
    graph[start].append((dest, cost))
dist = [INF] * (n+1)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0,start))
    dist[start] = 0
    while q:
        curr_dist, curr = heapq.heappop(q)
        if dist[curr] < curr_dist:
            continue
        for next in graph[curr]:
            next_node, next_dist = next
            cost = curr_dist + next_dist
            if cost < dist[next_node]:
                dist[next_node] = cost
                heapq.heappush(q, (cost, next_node))

start, end = map(int, sys.stdin.readline().split())

dijkstra(start)
print(dist[end])
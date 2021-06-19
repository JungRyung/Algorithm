import sys
import heapq

INF = int(1e9)

n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append((b,1))
    graph[b].append((a,1))

distance = [INF] * (n+1)
q = []

distance[1] = 0
heapq.heappush(q,(0,1))

while q:
    dist, current = heapq.heappop(q)
    if distance[current] < dist:
        continue
    for next, nextDist in graph[current]:
        cost = dist + nextDist
        if cost < distance[next]:
            distance[next] = cost
            heapq.heappush(q,(cost,next))

max_dist = 0
max_cnt = 0
for i in range(1,n+1):
    if distance[i] > max_dist and distance[i]!=INF:
        max_dist = distance[i]
        max_cnt = 1
        barn_num = i
    elif distance[i] == max_dist:
        max_cnt += 1

print(barn_num,' ',max_dist,' ',max_cnt)
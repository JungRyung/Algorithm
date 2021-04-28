import heapq
INF = int(1e9)

n, m, c = map(int, input().split())

start = c
distance = [INF] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0,start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        # 현재노드와 인접한 노드들을 검색
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost, i[0]))

# 다익스트라 알고리즘 수행
dijkstra(start)

# 도달할 수 있는 노드의 개수와 가장 먼 거리
cnt = 0
max_time = 0
for i in range(2,n+1):
    if distance[i] != INF:
        cnt += 1
        if distance[i] > max_time:
            max_time = distance[i]

print(cnt,max_time)    
        
import heapq
INF = int(1e9)

n, m, c = map(int, input().split())

distance = [INF] * (n+1)
graph = [[] for _ in range(1+n)]

for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((z, y))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0,start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop()
        if distance[now] < dist:
            continue
        # 현재노드와 인접한 노드들을 검색
        for i in graph[now]:
            cost = dist + i[1]
            
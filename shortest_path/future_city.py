INF = int(1e9)
n, m = map(int, input().split())

# 플로이드 워셜 알고리즘으로 풀이

graph = [[INF]*(n+1) for _ in range(n+1)]

# 자기자신을 향할 때는 0으로 초기화
for i in range(1, n+1):
    graph[i][i] = 0

# 그래프 정보 받아오기
for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

x, k = map(int, input().split())

# 플로이드 워셜 알고리즘 수행
for v in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][v] + graph[v][b])

distance = graph[1][k] + graph[k][x]

if distance >= INF:
    print("-1")
else:
    print(distance)
# 플로이드 워셜 알고리즘으로 수행
INF = int(1e9)

n, m, c = map(int, input().split())

# 그래프의 정보를 가질 리스트 초기화
graph = [[INF]*(n+1) for _ in range(n+1)]
# 대각선 요소 초기화
for i in range(1, n+1):
    graph[i][i] = 0

# 그래프의 정보를 입력
for i in range(m):
    x, y, z = map(int, input().split())
    graph[x][y] = z

# 플로이드 워셜 알고리즘 수행
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

cnt = 0
max_time = INF
for i in range(1, n+1):
    if graph[c][i] != INF:
        cnt += 1
    if graph[c][i] < max_time:
        max_time = graph[c][i]

print(cnt, max_time)
    
    
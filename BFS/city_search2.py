from collections import deque

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
visit = [-1]*(n+1)
results = []
# 그래프를 인접리스트로 표현
for _ in range(m):
    start, destination = map(int, input().split())
    graph[start].append(destination)

q = deque()
q.append(x)
visit[x] = 0
flag = False
while q:
    tmp = q.popleft()
    if visit[tmp] == k:
        results.append(tmp)
        flag = True
    for destination in graph[tmp]:
        if visit[destination] == -1:
            q.append(destination)
            visit[destination] = visit[tmp]+1

if flag == False:
    print(-1)
else:
    results.sort()
    for result in results:
        print(result)
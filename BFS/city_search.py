import sys
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
visit = [-1]*(n+1)
results = []
# 그래프를 인접리스트로 표현
for _ in range(m):
    start, destination = map(int, sys.stdin.readline().split())
    graph[start].append(destination)

queue = []
queue.append(x)
visit[x] = 0
flag = False
while queue:
    tmp = queue.pop(0)
    if visit[tmp] == k:
        results.append(tmp)
        flag = True
    for destination in graph[tmp]:
        if visit[destination] == -1:
            queue.append(destination)
            visit[destination] = visit[tmp]+1

if flag == False:
    print(-1)
else:
    results.sort()
    for result in results:
        print(result)
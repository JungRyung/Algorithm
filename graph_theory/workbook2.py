##### 문제집 #####
import sys
import heapq

n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    indegree[b] += 1

# 위상 정렬 알고리즘 시작
q = []
result = []
for i in range(1,n+1):
    if indegree[i] == 0:
        heapq.heappush(q,i)

while q:
    current = heapq.heappop(q)
    result.append(current)
    for nextNode in graph[current]:
        indegree[nextNode] -= 1
        if indegree[nextNode] == 0:
            heapq.heappush(q,nextNode)

for i in result:
    print(i,end=' ')
print()
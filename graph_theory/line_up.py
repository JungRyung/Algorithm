##### 줄 세우기 #####
import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[b].append(a)
    indegree[a] += 1

# 위상 정렬 알고리즘 시작
q = deque()
result = []
for i in range(1,n+1):
    if indegree[i] == 0:
        q.append(i)

while q:
    current = q.popleft()
    result.append(current)
    for nextNode in graph[current]:
        indegree[nextNode] -= 1
        if indegree[nextNode] == 0:
            q.append(nextNode)

for i in result[::-1]:
    print(i,end=' ')
print()    
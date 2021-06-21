##### 문제집 #####
import sys
import heapq

n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[b].append(a)
    indegree[a] += 1

# 위상 정렬 알고리즘 시작
q = []  # 최대힙으로 사용
result = []
for i in range(n,0,-1):
    if indegree[i] == 0:
        heapq.heappush(q,-i)    # 최대힙으로 사용할 수 있게 -를 붙이고 삽입

while q:
    current = -heapq.heappop(q)  # 꺼낼 때 -를 다시 붙여서 복구
    result.append(current)
    for nextNode in graph[current][::-1]:
        indegree[nextNode] -= 1
        if indegree[nextNode] == 0:
            heapq.heappush(q,-nextNode)

for i in result[::-1]:
    print(i,end=' ')
print()
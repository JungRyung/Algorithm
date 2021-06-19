##### 최종 순위 #####
# 위상 정렬 알고리즘
import sys
from collections import deque

def print_graph(graph,n):
    for i in range(1,n+1):
        for j in range(1,n+1):
            print(graph[i][j],end='\t')
        print()
    

t = int(sys.stdin.readline())
answer = []
for _ in range(t):
    # 노드의 개수 입력
    n = int(sys.stdin.readline())
    indegree = [0] * (n+1)
    graph = [[False]*(n+1) for _ in range(n+1)]
    # 작년 순위 입력
    rank = list(map(int, sys.stdin.readline().split()))
    # 그래프 초기화
    for i in range(n):
        for j in range(i+1,n):
            graph[rank[j]][rank[i]] = True
            indegree[rank[i]] += 1
        
    # 변경된 순위 정보 입력
    m = int(sys.stdin.readline())
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        # 간선 방향 반대로
        if graph[a][b]:
            graph[a][b] = False
            graph[b][a] = True
            indegree[a] += 1
            indegree[b] -= 1
        else:
            graph[a][b] = True
            graph[b][a] = False
            indegree[a] -= 1
            indegree[b] += 1
    
    # 위상정렬 알고리즘
    result = []
    q = deque()
    for i in range(1,n+1):
        if indegree[i] == 0:
            q.append(i)

    only = True
    cycle = False

    for i in range(n):
        if len(q) == 0:
            cycle = True
            break
        if len(q) >= 2:
            only = False
            break
        current = q.popleft()
        result.append(current)
        for j in range(1, n+1):
            if graph[current][j]:
                indegree[j] -= 1
                if indegree[j] == 0:
                    q.append(j)
    if cycle:
        print("IMPOSSIBLE")
    elif not only:
        print("?")
    else:
        for i in result[::-1]:
            print(i, end=' ')
        print()
        
        
    
    

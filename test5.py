from collections import deque

def dfs(graph):
    s = []
    visited = []

    s.append(0,0)
    searched = False
    while s:
        now, wolf_cnt = s[0]
        for next in graph[now]:
            if next not in visited and 
    

def solution(info, edges):
    answer = 0

    # 트리 구성
    visit = [False] * len(info)
    graph = [[] for _ in range(len(info))]
    for edge in edges:
        parent, child = edge
        graph[parent].append(child)

    max_sheep = 1
    q = deque()
    q.append(0,0)
    visit[0] = True
    while q:
        curr, wolf_cnt = q.popleft()
        if not visit and info[curr] == 0:
            max_sheep += 1
        visit[curr] = True
        for next in graph[curr]:
            if not visit[next] and info[next] == 0:
                q.appendleft(next)
            elif not visit[next] and info[next] == 1:
                q.append(next)
    answer = cnt
    return answer

info = [0,0,1,1,1,0,1,0,1,0,1,1]
edges = [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]

result =solution(info, edges)
print(result)
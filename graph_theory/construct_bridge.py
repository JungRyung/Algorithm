##### 다리 만들기 #####
# URL : https://www.acmicpc.net/problem/17472
import sys
from typing import Deque

INF = 1e9

def print_2D_list(arr):
    row = len(arr)
    col = len(arr[0])
    for i in range(row):
        for j in range(col):
            if arr[i][j] == INF:
                print('INF',end='\t')
            else:
                print(arr[i][j],end='\t')
        print()

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

dx = [-1,0,1,0]
dy = [0,-1,0,1]

n, m = map(int, sys.stdin.readline().split())
sea_map = [[] for _ in range(n)]
for i in range(n):
    sea_map[i] = list(map(int, sys.stdin.readline().split()))

visit = [[False]*m for _ in range(n)]

islands = [[0]*m for _ in range(n)]
island_cnt = 1
for i in range(n):
    for j in range(m):
        # 조건을 만족하면 BFS 실시
        q = []
        if sea_map[i][j] == 1 and visit[i][j] == False:
            q.append((i,j))
            visit[i][j] = True
            islands[i][j] = island_cnt
            while q:
                x,y = q.pop(0)
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0<=nx<n and 0<=ny<m:
                        if sea_map[nx][ny] == 1 and visit[nx][ny] == False:
                            q.append((nx,ny))
                            visit[nx][ny] = True
                            islands[nx][ny] = island_cnt
            island_cnt += 1
print_2D_list(islands)

graph = [[INF]*(island_cnt) for _ in range(island_cnt)]

# 각 셀에서 놓을 수 있는 다리를 검색
for i in range(n):
    for j in range(m):
        if islands[i][j] != 0:
            current = islands[i][j]
            # 사방으로 검색
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                # 바다가 보이면 그 방향으로 계속 탐색
                if 0<=nx<n and 0<=ny<m and islands[nx][ny] == 0:
                    dist = 1
                    nx = nx + dx[k]
                    ny = ny + dy[k]
                    find_next = False
                    while 0<=nx<n and 0<=ny<m and islands[nx][ny] == 0:
                        dist += 1
                        nx = nx + dx[k]
                        ny = ny + dy[k]
                    if 0<=nx<n and 0<=ny<m and islands[nx][ny] != 0 and islands[nx][ny] != current:
                        find_next = True
                        next = islands[nx][ny]
                    if find_next == True and dist>=2:
                        graph[current][next] = min(graph[current][next],dist)
                        graph[next][current] = min(graph[next][current],dist)
print_2D_list(graph)

# 모든 섬이 연결되어 있는지 확인
parent = [0] * (island_cnt)
edges = []
for i in range(island_cnt):
    parent[i] = i
for i in range(2,island_cnt):
    for j in range(1,i):
        if graph[i][j]!=INF:
            # print(parent)
            union_parent(parent,i,j)
            edges.append((graph[i][j],i,j))
edges.sort()
for i in range(island_cnt):
    find_parent(parent,i)
            
print(parent)
tmp = parent[1]
all_connected = True
for i in range(1,island_cnt):
    if tmp != parent[i]:
        all_connected = False
# print(all_connected)

# 연결되어있으면 kruscal 알고리즘 진행
if all_connected:
    answer = 0
    # parent 리스트 다시 초기화
    for i in range(island_cnt):
        parent[i] = i
    for edge in edges:
        cost, a, b = edge
        if find_parent(parent,a) != find_parent(parent,b):
            union_parent(parent,a,b)
            answer += cost
    print(answer)
# 연결되어있지 않으면 -1 출력
else:
    print(-1)
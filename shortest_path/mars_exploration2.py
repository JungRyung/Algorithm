import sys
import heapq
from typing import Deque

INF = int(1e9)
t = int(sys.stdin.readline())

answer = []
for _ in range(t):
    n = int(sys.stdin.readline())
    dx = [-1,0,1,0]
    dy = [0,-1,0,1]
    mars_map = [[] for _ in range(n)]
    for i in range(n):
        mars_map[i] = list(map(int, sys.stdin.readline().split()))
    # 최단 거리 테이블을 모두 무한으로 초기화
    distance = [[INF]*n for _ in range(n)]
    
    x, y = 0, 0
    q = [(mars_map[x][y],x,y)]
    distance[x][y] = mars_map[x][y]
    while q:
        dist, x, y = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[x][y] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            #맵의 범위를 벗어나는 경우 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            cost = dist + mars_map[nx][ny]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[nx][ny]:
                distance[nx][ny] = cost
                heapq.heappush(q, (cost,nx,ny))
    answer.append(distance[n-1][n-1])
print(answer)
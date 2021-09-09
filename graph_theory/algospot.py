'''
TITLE   : 알고스팟
URL     : https://www.acmicpc.net/problem/1261
DATE    : 21.09.09
'''
import sys
from collections import deque
INF = 10e9

dx = [-1,0,1,0]
dy = [0,-1,0,1]

m, n = map(int, sys.stdin.readline().split())
maze = [list(sys.stdin.readline().strip()) for _ in range(n)]
dist = [[INF] * m for _ in range(n)]
q = deque()

q.append((0,0))
dist[0][0] = 0
while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if not(0<=nx<n and 0<=ny<m):
            continue
        if maze[nx][ny] == '1':
            if dist[nx][ny] > dist[x][y] + 1:
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx,ny))
        else:
            if dist[nx][ny] > dist[x][y]:
                dist[nx][ny] = dist[x][y]
                q.append((nx,ny))
print(dist[n-1][m-1])
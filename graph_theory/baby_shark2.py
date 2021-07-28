'''
TITLE   : 아기 상어 2
URL     : https://www.acmicpc.net/problem/17086
DATE    : 21.07.27
'''
import sys

dx = [-1,-1,-1,0,0,1,1,1]
dy = [-1,0,1,-1,1,-1,0,1]

n, m = map(int, sys.stdin.readline().split())
area = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

def bfs(x,y):
    q = []
    visit = [[False]*m for _ in range(n)]
    q.append((x,y,0))
    visit[x][y] = True
    while q:
        curr_x, curr_y, time = q.pop(0)
        for i in range(8):
            nx = curr_x + dx[i]
            ny = curr_y + dy[i]
            if 0<=nx<n and 0<=ny<m and not visit[nx][ny]:
                if area[nx][ny] == 1:
                    return time + 1
                else:
                    visit[nx][ny] = True
                    q.append((nx,ny,time + 1))

max_dist = 0
for i in range(n):
    for j in range(m):
        if area[i][j] == 0:
            max_dist = max(max_dist, bfs(i,j))

print(max_dist)
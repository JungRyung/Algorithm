'''
TITLE   : 벽 부수고 이동하기
URL     : https://www.acmicpc.net/problem/2206
DATE    : 21.08.10
'''
import sys
from collections import deque
INF = 10e9

dx = [-1,0,1,0]
dy = [0,-1,0,1]

n, m = map(int, sys.stdin.readline().split())
maze = [[] for _ in range(n)]
for i in range(n):
    maze[i] = list(sys.stdin.readline().strip())

def bfs():
    visit = [[False]*m for _ in range(n)]
    visit[0][0] = True
    q = deque()
    q.append((0,0,0))
    while q:
        x, y, t = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m and not visit[nx][ny] and maze[nx][ny] == '0':
                if nx == n-1 and ny == m-1:
                    return t+1
                visit[nx][ny] = True
                q.append((nx,ny,t+1))
    return -1

smallest_step = INF
step = bfs()
if step >= 0:
    smallest_step = step

for i in range(n):
    for j in range(m):
        if maze[i][j] == '1':
            maze[i][j] = '0'
            step = bfs()
            if step >= 0:
                # print(i,j,step)
                smallest_step = min(smallest_step, step+1)
            maze[i][j] = '1'
if smallest_step == INF:
    print(-1)
else:
    print(smallest_step)
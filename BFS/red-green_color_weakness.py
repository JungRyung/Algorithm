'''
Title   : 적록색약
URL     : https://www.acmicpc.net/problem/10026
DATE    : 21.07.24
'''
import sys

dx = [-1,0,1,0]
dy = [0,-1,0,1]

n = int(sys.stdin.readline())
grid = [list(sys.stdin.readline().strip()) for _ in range(n)]
visit = [[False]*n for _ in range(n)]
area_cnt = 0

def bfs(x, y):
    global area_cnt
    area_cnt += 1
    q = []
    q.append((x, y))
    visit[x][y] = True
    while q:
        curr = q.pop(0)
        for i in range(4):
            nx = curr[0] + dx[i]
            ny = curr[1] + dy[i]
            if 0<=nx<n and 0<=ny<n and not visit[nx][ny] and grid[x][y]==grid[nx][ny]:
                visit[nx][ny] = True
                q.append((nx,ny))

#색약이 아닌 사람
for i in range(n):
    for j in range(n):
        if not visit[i][j]:
            bfs(i,j)
print(area_cnt,end=' ')

visit = [[False]*n for _ in range(n)]
area_cnt = 0

for i in range(n):
    for j in range(n):
        if grid[i][j] == 'G':
            grid[i][j] = 'R'

for i in range(n):
    for j in range(n):
        if not visit[i][j]:
            bfs(i,j)
print(area_cnt)

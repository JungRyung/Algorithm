'''
TITLE   : 유기농 배추
URL     : https://www.acmicpc.net/problem/1012
DATE    : 21.08.05
'''
import sys

dx = [-1,0,1,0]
dy = [0,-1,0,1]

for _ in range(int(sys.stdin.readline())):
    m, n, k = map(int, sys.stdin.readline().split())
    field = [[0]*m for i in range(n)]
    for i in range(k):
        a, b = map(int, sys.stdin.readline().split())
        field[b][a] = 1
    
    visit = [[False]*m for i in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(m):
            if not visit[i][j] and field[i][j] == 1:
                cnt += 1
                visit[i][j] = True
                q = []
                q.append((i,j))
                while q:
                    x, y = q.pop(0)
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0<=nx<n and 0<=ny<m and not visit[nx][ny] and field[nx][ny] == 1:
                            visit[nx][ny] = True
                            q.append((nx,ny))
    print(cnt)
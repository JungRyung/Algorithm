'''
Title   : 미로 탐색
URL     : https://www.acmicpc.net/problem/2178
Date    : 21.07.10
'''
import sys

dx = [-1,0,1,0]
dy = [0,-1,0,1]

n, m = map(int, sys.stdin.readline().split())
maze = [list(sys.stdin.readline().strip()) for _ in range(n)]
visit = [[False]*m for _ in range(n)]

q = [(0,0,1)]
visit[0][0] = True
while q:
    x, y, t = q.pop(0)
    if x==n-1 and y==m-1:
        print(t)
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<m and maze[nx][ny] == '1' and not visit[nx][ny]:
            q.append((nx,ny,t+1))
            visit[nx][ny] = True
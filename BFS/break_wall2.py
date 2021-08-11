'''
TITLE   : 벽 부수고 이동하기
URL     : https://www.acmicpc.net/problem/2206
DATE    : 21.08.11
'''
import sys
from collections import deque

dx = [-1,0,1,0]
dy = [0,-1,0,1]

def bfs():
    q = deque()
    q.append([0, 0, 1])
    visit = [[[0] * 2 for _ in range(m)] for __ in range(n)]
    visit[0][0][1] = 1
    while q:
        x, y, w = q.popleft()
        if x == n-1 and y == m-1:
            return visit[x][y][w]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m:
                # 벽을 만났을 때
                if maze[nx][ny] == 1 and w == 1:
                    visit[nx][ny][0] = visit[x][y][1] + 1
                    q.append([nx,ny,0])
                # 방문하지 않은 벽이 아닌 공간을 만났을 때
                elif maze[nx][ny] == 0 and visit[nx][ny][w] == 0:
                    visit[nx][ny][w] = visit[x][y][w] + 1
                    q.append([nx,ny,w])
    return -1

n, m = map(int, sys.stdin.readline().split())
maze = [list(sys.stdin.readline().strip()) for _ in range(n)]
print(bfs())
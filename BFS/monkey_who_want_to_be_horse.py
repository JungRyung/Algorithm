'''
TITLE   : 말이 되고픈 원숭이
URL     : https://www.acmicpc.net/problem/1600
DATE    : 21.10.24
'''
import sys
from collections import deque

dx = [0,-1,0,1,-2,-1,1,2,2,1,-1,-2]
dy = [-1,0,1,0,-1,-2,-2,-1,1,2,2,1]

k = int(sys.stdin.readline())
w, h = map(int, sys.stdin.readline().split())

land = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]



def bfs():
    visit = [[[0]*(k+1) for __ in range(w)] for _ in range(h)]
    visit[0][0][0] = 1
    q = deque()
    q.append((0,0,0))

    while q:
        x, y, t = q.popleft()
        if x == h-1 and y == w-1:
            return visit[x][y][t] - 1
        for i in range(12):
            nx = x + dx[i]
            ny = y + dy[i]
            # 앞뒤양옆으로 이동할 때
            if 0<=i<4:
                if 0<=nx<h and 0<=ny<w and not visit[nx][ny][t] and land[nx][ny] == 0:
                    visit[nx][ny][t] = visit[x][y][t] + 1
                    q.append((nx,ny,t))
            # 눈 목 자로 이동할 때
            elif 4<=i<12 and t < k:
                if 0<=nx<h and 0<=ny<w and not visit[nx][ny][t+1] and land[nx][ny] == 0:
                    visit[nx][ny][t+1] = visit[x][y][t] + 1
                    q.append((nx,ny,t+1))
    return -1
ans = bfs()
print(ans)
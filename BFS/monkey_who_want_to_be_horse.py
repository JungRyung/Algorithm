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
    # visit = [[False]*w for _ in range(h)]
    # visit[0][0] = True
    q = deque()
    q.append((0,0,0,0))

    while q:
        x, y, t, jump = q.popleft()
        for i in range(12):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<h and 0<=ny<w and land[nx][ny] == 0:
                # 앞뒤양옆으로 이동할 때
                if 0<=i<4:
                    if nx==h-1 and ny==w-1:
                        return t+1
                    q.append((nx,ny,t+1,jump))
                # 눈 목 자로 이동할 때
                elif 4<=i<12 and jump<k:
                    if nx==h-1 and ny==w-1:
                        return t+1
                    q.append((nx,ny,t+1,jump+1))
    return -1
ans = bfs()
print(ans)
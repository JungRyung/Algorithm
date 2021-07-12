'''
TITLE   : 보물섬
URL     : https://www.acmicpc.net/problem/2589
DATE    : 21.07.12
'''
import sys
from collections import deque

dx = [-1,0,1,0]
dy = [0,-1,0,1]

h, w = map(int, sys.stdin.readline().split())
site_map = [list(sys.stdin.readline().strip()) for _ in range(h)]

def find_max_dist(x,y):
    visit = [[False]*w for _ in range(h)]
    max_dist = 0
    q = deque()
    visit[x][y] = True
    q.append((x,y,0))
    while q:
        now_x, now_y, dist = q.popleft()
        for i in range(4):
            nx = now_x + dx[i]
            ny = now_y + dy[i]
            if 0<=nx<h and 0<=ny<w and not visit[nx][ny] and site_map[nx][ny]=='L':
                q.append((nx,ny,dist+1))
                visit[nx][ny] = True
                max_dist = max(max_dist, dist+1)
    return max_dist

treasure_dist = 0
for i in range(h):
    for j in range(w):
        if site_map[i][j] == 'L':
            treasure_dist = max(treasure_dist,find_max_dist(i,j))

print(treasure_dist)
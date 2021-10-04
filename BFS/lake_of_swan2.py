'''
TITLE   : 백조의 호수
URL     : https://www.acmicpc.net/problem/3197
DATE    : 21.10.04
'''
import sys
from collections import deque

dx = [-1,0,1,0]
dy = [0,-1,0,1]

def print_lake(lake, r):
    for i in range(r):
        print(''.join(lake[i]))
    print()

def melt(lake, melt_points):
    next_melt_points = deque()
    while melt_points:
        x, y = melt_points.popleft()
        lake[x][y] = '.'
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<r and 0<=ny<c and lake[nx][ny] == 'X':
                next_melt_points.append((nx,ny))
    return lake, next_melt_points
        
    

r, c = map(int, sys.stdin.readline().split())
lake = []
swan = []

for i in range(r):
    tmp = list(sys.stdin.readline().strip())
    for j in range(c):
        # 해당 지점에 백조가 위치할 경우
        if tmp[j] == 'L':
            swan.append((i,j))
    lake.append(tmp)

melt_points = deque()
for i in range(r):
    for j in range(c):
        # 다음 턴에 녹을 지점일 경우
        if lake[i][j] != 'X':
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0<=nx<r and 0<=ny<c and lake[nx][ny] == 'X':
                    melt_points.append((i,j))

time = 0
while True:
    lake, melt_points = melt(lake, melt_points)
    time += 1
    
    # BFS
    visit = [[False]*c for _ in range(r)]
    x, y = swan[0]
    visit[x][y] = True
    q = deque()
    q.append((x,y))
    searched = False
    while q:
        x, y = q.popleft()
        if x == swan[1][0] and y == swan[1][1]:
            searched = True
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<r and 0<=ny<c and not visit[nx][ny]:
                if lake[nx][ny] == 'X':
                    melt_points.append((nx,ny))
                else:
                    q.append((nx,ny))
                visit[nx][ny] = True
    if searched:
        break

print(time-1)
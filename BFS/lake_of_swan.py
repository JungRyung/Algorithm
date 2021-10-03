'''
TITLE   : 백조의 호수
URL     : https://www.acmicpc.net/problem/3197
DATE    : 21.10.02
'''
import sys
from collections import deque

dx = [-1,0,1,0]
dy = [0,-1,0,1]

def melt(lake, r, c):
    melt_points = []
    for i in range(r):
        for j in range(c):
           if lake[i][j] == 'X':
               for k in range(4):
                   nx = i + dx[k]
                   ny = j + dy[k]
                   if 0<=nx<r and 0<=ny<c and lake[nx][ny] == '.':
                       melt_points.append((i,j))
                       break
    
    for melt_point in melt_points:
        x, y = melt_point
        lake[x][y] = '.'

    return lake

def print_lake(lake, r):
    for i in range(r):
        print(''.join(lake[i]))
    print()

r, c = map(int, sys.stdin.readline().split())
lake = []
swan = []

for i in range(r):
    tmp = list(sys.stdin.readline().strip())
    for j in range(c):
        if tmp[j] == 'L':
            swan.append((i,j))
    lake.append(tmp)

time = 0
melt_points = []
while True:
    # lake = melt(lake,r,c)
    for point in melt_points:
        x, y = point
        lake[x][y] = '.'
    melt_points = []
    time += 1
    print_lake(lake, r)
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

print(time)

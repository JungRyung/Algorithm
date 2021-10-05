'''
TITLE   : 백조의 호수
URL     : https://www.acmicpc.net/problem/3197
DATE    : 21.10.05
'''
# BFS + 이분탐색
import sys
from collections import deque

dx = [-1,0,1,0]
dy = [0,-1,0,1]

def print_time(time, r):
    for i in range(r):
        for t in time[i]:
            print(t,end='')
        print()
    print()

def print_lake(lake, r):
    for i in range(r):
        print(''.join(lake[i]))
    print()

def melt_time_set(lake, r, c):
    time = [[0]*c for _ in range(r)]
    q = deque()
    visit = [[False]*c for _ in range(r)]
    # 초기에 물인 부분을 queue에 초기화
    for i in range(r):
        for j in range(c):
            if lake[i][j] != 'X':
                visit[i][j] = True
                q.append((i,j))
    last_time = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<r and 0<=ny<c and not visit[nx][ny]:
                time[nx][ny] = time[x][y] + 1
                last_time = max(last_time, time[nx][ny])
                visit[nx][ny] = True
                q.append((nx,ny))
    return time, last_time

def bfs(time, swan1, swan2, mid):
    q = deque()
    visit = [[False]*c for _ in range(r)]
    x, y = swan1
    visit[x][y] = True
    q.append(swan1)
    while q:
        x, y = q.popleft()
        if (x, y) == swan2:
            return True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<r and 0<=ny<c and not visit[nx][ny] and time[nx][ny] <= mid:
                visit[nx][ny] = True
                q.append((nx,ny))
    return False

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



front = 0
time, end = melt_time_set(lake, r, c)

ans = end
while front <= end:
    mid = (front + end) // 2
    if bfs(time, swan[0], swan[1], mid):
        end = mid - 1
        ans = mid
    else:
        front = mid + 1
print(ans)
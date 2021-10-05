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
        # 해당 지점에 백조가 위치할 경우
        if tmp[j] == 'L':
            swan.append((i,j))
    lake.append(tmp)

time = [[0]*c for _ in range(r)]
def melt_time_set():
    q = deque()
    visit = [[False]*c for _ in range(r)]
    # 초기에 물인 부분을 queue에 초기화
    for i in range(r):
        for j in range(c):
            if lake[i][j] != 'X':
                visit[i][j] = True
                q.append((i,j))

    while q:
        print(q)
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<r and 0<=ny<c and not visit[nx][ny]:
                time[nx][ny] = time[x][y] + 1
                visit[nx][ny] = True
                q.append((x,y))
melt_time_set()

print(time)
print_lake(lake,r)
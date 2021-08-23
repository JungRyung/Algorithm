'''
TITLE   : 연구소 3
URL     : https://www.acmicpc.net/problem/17142
DATE    : 21.08.17
'''
import sys
from collections import deque
from itertools import combinations
INF = 10e9

dx = [-1,0,1,0]
dy = [0,-1,0,1]

n, m = map(int, sys.stdin.readline().split())
lab = [[] for _ in range(n)]
virus = []
blank_cnt = 0

for i in range(n):
    lab[i] = list(map(int, sys.stdin.readline().split()))
    for j in range(n):
        if lab[i][j] == 2:
            virus.append((i,j))
        if lab[i][j] == 0:
            blank_cnt += 1
            
# 조합 마다 bfs
minTime = INF
for comb in combinations(virus, m):
    q = deque()
    visit = [[False]*n for _ in range(n)]
    for v in comb:
        x, y = v
        visit[x][y] = True
        q.append((x,y,0))
    time = 0
    cnt = blank_cnt
    while q:
        x, y, t = q.popleft()
        if cnt == 0:
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n and not visit[nx][ny] and lab[nx][ny] != 1:
                visit[nx][ny] = True
                q.append((nx,ny,t+1))
                time = t + 1
                if lab[nx][ny] == 0:
                    cnt -= 1
    if cnt == 0:
        minTime = min(minTime,time)
if minTime != INF:
    print(minTime)
else:
    print(-1)
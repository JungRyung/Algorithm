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

for i in range(n):
    lab[i] = list(map(int, sys.stdin.readline().split()))
    for j in range(n):
        if lab[i][j] == 2:
            virus.append((i,j))
# 조합 마다 bfs

minTime = INF
for comb in combinations(virus, m):
    print(comb)
    q = deque()
    visit = [[False]*n for _ in range(n)]
    for v in comb:
        x, y = v
        visit[x][y] = True
        q.append((x,y,0))
    time = 0
    while q:
        x, y, t = q.popleft()
        time = max(time,t)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n and not visit[nx][ny] and lab[nx][ny] != 1:
                visit[nx][ny] = True
                q.append((nx,ny,t+1))
    minTime = min(minTime,time)
    print(time)
print(minTime)
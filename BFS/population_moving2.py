# 인구 이동 url: www.acmicpc.net/problem/16234
import sys
from collections import deque
n, l, r = map(int,sys.stdin.readline().split())
country_map = [[] for _ in range(n)]
dx = [-1,0,1,0]
dy = [0,-1,0,1]

for i in range(n):
    country_map[i] = list(map(int,sys.stdin.readline().split()))

def bfs(x,y,visit,cnt):
    q = deque()
    q.append((x,y))
    visit[x][y] = cnt
    sum = country_map[x][y]
    num = 1
    united = []
    united.append((x,y))
    while q:
        tmp = q.popleft()
        for i in range(4):
            nx = tmp[0] + dx[i]
            ny = tmp[1] + dy[i]
            if nx>=0 and nx<n and ny>=0 and ny<n:
                diff = abs(country_map[tmp[0]][tmp[1]] - country_map[nx][ny])
                if diff >= l and diff <= r and visit[nx][ny] == 0:
                    q.append((nx,ny))
                    united.append((nx,ny))
                    visit[nx][ny] = cnt
                    sum += country_map[nx][ny]
                    num += 1
    for i, j in united:
        country_map[i][j] = sum//num
            
    return visit
    
t = 0
while True:
    visit = [[0]*n for _ in range(n)]
    cnt = 1
    # 연합 결성
    changed = False
    for i in range(n):
        for j in range(n):
            if visit[i][j] == 0:
                need_bfs = False
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if nx>=0 and nx<n and ny>=0 and ny<n:
                        diff = abs(country_map[i][j] - country_map[nx][ny])
                        if diff >= l and diff <= r and visit[nx][ny] == 0:
                            need_bfs = True
                            break
                if need_bfs == True:
                    changed = True
                    visit = bfs(i,j,visit,cnt)
                    cnt += 1
            
    if changed == True:
        t += 1
    else:
        print(t)
        break
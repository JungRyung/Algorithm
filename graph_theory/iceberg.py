'''
Title   : 빙산
URL     : https://www.acmicpc.net/problem/2573
'''
import sys
import copy

def print_2D_arr(arr):
    row = len(arr)
    col = len(arr[0])
    print()
    for i in range(row):
        for j in range(col):
            print(arr[i][j], end=' ')
        print()

dx = [-1,0,1,0]
dy = [0,-1,0,1]

n, m = map(int, sys.stdin.readline().split())
sea_map = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

time = 0
before_cnt = 0
while True:
    time += 1
    visit = [[False]*m for _ in range(n)]
    # 녹이기
    next_map = copy.deepcopy(sea_map)
    for i in range(n):
        for j in range(m):
            if sea_map[i][j] != 0:
                cnt = 0
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0<=nx<n and 0<=ny<m and sea_map[nx][ny]==0:
                        cnt += 1
                next_map[i][j] -= cnt
                if next_map[i][j] < 0:
                    next_map[i][j] = 0
    sea_map = next_map
    # 빙산 개수 구하기
    cnt = 0
    for i in range(n):
        for j in range(m):
            if sea_map[i][j] != 0 and not visit[i][j]:
                cnt += 1
                visit[i][j] = True
                q = [(i,j)]
                while q:
                    tmp_x, tmp_y = q.pop(0)
                    for k in range(4):
                        nx = tmp_x + dx[k]
                        ny = tmp_y + dy[k]
                        if 0<=nx<n and 0<=ny<m and not visit[nx][ny] and sea_map[nx][ny]!=0:
                            visit[nx][ny] = True
                            q.append((nx,ny))
    if time == 1:
        before_cnt = cnt
    if cnt == 0:
        print(0)
        break
    elif before_cnt != cnt:
        print(time)
        break
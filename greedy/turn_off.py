'''
TITLE   : 불 끄기
URL     : https://www.acmicpc.net/problem/14939
DATE    : 21.09.23
'''
import sys
from itertools import combinations_with_replacement

dx = [-1,0,1,0]
dy = [0,-1,0,1]

def switch(x,y):
    if bolbs[x][y] == 1:
        bolbs[x][y] = 0
    else:
        bolbs[x][y] = 1
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if not(0<=nx<10 and 0<=ny<10):
            continue
        if bolbs[nx][ny] == 1:
            bolbs[nx][ny] = 0
        else:
            bolbs[nx][ny] = 1
        

def sum_list(bolbs):
    total = 0
    for i in range(10):
        total += sum(bolbs[i])
    return total

bolbs = []
for _ in range(10):
    line = list(sys.stdin.readline().strip())
    tmp_list = []
    for ch in line:
        if ch =='O':
            tmp_list.append(1)
        else:
            tmp_list.append(0)
    bolbs.append(tmp_list)

cnt = 0
for i in range(1,10):
    for j in range(10):
        if bolbs[i-1][j] == 1:
            switch(i,j)
            cnt += 1

if sum_list(bolbs) == 0:
    print(cnt)
else:
    print(-1)
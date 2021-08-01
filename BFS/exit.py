'''
TITLE   : 탈출
URL     : https://www.acmicpc.net/problem/3055
DATE    : 21.08.01
'''
import sys

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

r, c = map(int, sys.stdin.readline().split())

forest = [[] for _ in range(r)]
start_x, start_y = 0, 0

for i in range(r):
    forest[i] = list(sys.stdin.readline().strip())
    for j in range(c):
        if forest[i][j] == 'S':
            start_x, start_y = i, j

def flow_water():
    visit = [[False]*c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if not visit[i][j]:
                visit[i][j] = True
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0<=nx<r and 0<=ny<c and not visit[nx][ny] and forest[nx][ny] == '.':
                        

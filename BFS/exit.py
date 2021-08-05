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

# def print_map():
#     for i in range(r):
#         for j in range(c):
#             print(forest[i][j], end=' ')
#         print()

def flow_water():
    visit = [[False]*c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if not visit[i][j] and forest[i][j] == '*':
                visit[i][j] = True
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0<=nx<r and 0<=ny<c and not visit[nx][ny] and forest[nx][ny] == '.':
                        visit[nx][ny] = True
                        forest[nx][ny] = '*'

def bfs(start_x, start_y):
    visit = [[False]*c for _ in range(r)]
    visit[start_x][start_y] = True
    q = []
    q.append((start_x, start_y,0))
    before_t = -1
    while q:
        curr_x, curr_y, t = q.pop(0)
        if before_t != t:
            flow_water()
            # print_map()
        before_t = t
        for i in range(4):
            nx = curr_x + dx[i]
            ny = curr_y + dy[i]
            if 0<=nx<r and 0<=ny<c and not visit[nx][ny] and (forest[nx][ny] != '*' and forest[nx][ny] != 'X'):
                if forest[nx][ny] == 'D':
                    return t+1
                visit[nx][ny] = True
                q.append((nx,ny,t+1))
    return False

t = bfs(start_x, start_y)
if  t == False:
    print("KAKTUS")
else:
    print(t)
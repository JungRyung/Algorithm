'''
Title   : 치즈
URL     : https://www.acmicpc.net/problem/2636
DATE    : 21.07.25
'''
import sys

dx = [-1,0,1,0]
dy = [0,-1,0,1]

h, w = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]
visit = [[False]*w for _ in range(h)]
cheese_list = set()
removed = set()

def bfs(x,y):
    q = []
    visit[x][y] = True
    q.append((x,y))
    while q:
        curr = q.pop(0)
        for i in range(4):
            nx = curr[0] + dx[i]
            ny = curr[1] + dy[i]
            if 0<=nx<h and 0<=ny<w and not visit[nx][ny] and board[nx][ny] != 1:
                board[nx][ny] = 0
                q.append((nx,ny))
                visit[nx][ny] = True

bfs(0,0)

for i in range(h):
    for j in range(w):
        if not visit[i][j] and board[i][j] == 0:
            board[i][j] = -1
        if board[i][j] == 1:
            cheese_list.add((i,j))

cheese_cnt = 0
time = 0
while cheese_list:
    cheese_cnt = len(cheese_list)
    for cheese in cheese_list:
        x, y = cheese
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<h and 0<=ny<w and board[nx][ny] == 0:
                removed.add((x,y))
                break
    for cell in removed:
        x, y = cell
        board[x][y] = 0
    visit = [[False]*w for _ in range(h)]
    bfs(0,0)
    cheese_list = cheese_list - removed
    removed = set()
    time += 1
print(time)
print(cheese_cnt)
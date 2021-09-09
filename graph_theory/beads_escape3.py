'''
TITLE   : 구슬 탈출 3
URL     : https://www.acmicpc.net/problem/15644
DATE    : 21.09.08
'''
import sys
from collections import deque
INF = 10e9

dx = [-1,0,1,0]
dy = [0,-1,0,1]

n, m = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().strip()) for _ in range(n)]
red_x, red_y, blue_x, blue_y = 0,0,0,0
visited = set()
for i in range(n):
    for j in range(m):
        if board[i][j] == 'R':
            red_x, red_y = i, j
            board[i][j] = '.'
        if board[i][j] == 'B':
            board[i][j] = '.'
            blue_x, blue_y = i, j

q = deque()
q.append((red_x,red_y,blue_x,blue_y,0,''))
visited.add((red_x,red_y,blue_x,blue_y))

def move(x,y,i):
    nx = x + dx[i]
    ny = y + dy[i]
    cnt = 0
    while board[nx][ny] == '.':
        x, y = nx, ny
        nx = x + dx[i]
        ny = y + dy[i]
        cnt += 1
    if board[nx][ny] =='#':
        return x,y,cnt
    elif board[nx][ny] == 'O':
        return nx,ny,cnt+1

min_depth = INF
ans = ''
while q:
    rx,ry,bx,by,depth,commands = q.popleft()
    for i in range(4):
        nrx,nry,rcnt = move(rx,ry,i)
        nbx,nby,bcnt = move(bx,by,i)
        if i == 0:
            nc = 'U'
        elif i == 1:
            nc = 'L'
        elif i == 2:
            nc = 'D'
        else:
            nc = 'R'
        # 다음 위치로 이동중에 구멍을 만나는 경우
        # 파란 구슬이 구멍에 빠지는 경우
        if board[nbx][nby] == 'O':
            continue
        # 빨간 구슬이 구멍에 빠지는 경우
        if board[nrx][nry] == 'O':
            if min_depth > depth + 1:
                commands = commands + nc
                min_depth = depth + 1
                ans = commands
            continue
        # 구멍을 만나지 않고 구슬 둘 다 멈추는 경우
        # 빨간 구슬과 파란 구슬이 겹치는 경우
        if nrx == nbx and nry == nby:
            # 빨간 구슬을 뒤로 한칸 옮기기
            if rcnt > bcnt:
                nrx = nrx - dx[i]
                nry = nry - dy[i]
            # 파란 구슬을 뒤로 한칸 옮기기
            elif rcnt < bcnt:
                nbx = nbx - dx[i]
                nby = nby - dy[i]
                
        if (nrx,nry,nbx,nby) not in visited:
            visited.add((nrx,nry,nbx,nby))
            q.append((nrx,nry,nbx,nby,depth+1,commands + nc))
if min_depth == INF or min_depth > 10:
    print(-1)
else:
    print(min_depth)
    print(ans)
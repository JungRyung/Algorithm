'''
TITLE   : 로봇 청소기
URL     : https://www.acmicpc.net/problem/14503
DATE    : 21.09.06
'''
import sys

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, sys.stdin.readline().split())
r, c, d = map(int, sys.stdin.readline().split())

loc = []
for _ in range(n):
    loc.append(list(map(int, sys.stdin.readline().split())))

def left():
    if d == 0:
        return 3
    else:
        return d - 1
def behind():
    if d == 2:
        return 0
    elif d == 3:
        return 1
    else:
        return d + 2

def rotate():
    global d
    d -= 1
    if d < 0:
        d = 3

cnt = 0
while True:
    # 현재 위치 청소
    if loc[r][c] == 0:
        loc[r][c] = 2
        cnt += 1
    # 왼쪽 탐색 회전
    searched = False
    for _ in range(4):
        nx = r + dx[left()]
        ny = c + dy[left()]
        rotate()
        if loc[nx][ny] == 0:
            r = nx
            c = ny
            searched = True
            break
    if searched:
        continue
    # 네 방향 모두 청소가 이미 되어있거나 벽인 경우
    # 뒤가 벽이 아니면 후진
    if loc[r + dx[behind()]][c + dy[behind()]] != 1:
        r = r + dx[behind()]
        c = c + dy[behind()]
    # 뒤가 벽이면 정지
    else:
        break
print(cnt)
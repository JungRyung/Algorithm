'''
TITLE   : 청소년 상어
URL     : https://www.acmicpc.net/problem/19236
DATE    : 21.07.27
'''
import sys

dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,-1,-1,-1,0,1,1,1]

area = [[] for _ in range(4)]
fishes = [i for i in range(1,17)]
print(fishes)
fish_pos = [0] * 17
fish_direct = [0] * 17
for i in range(4):
    tmp_list = list(map(int, sys.stdin.readline().split()))
    for j in range(4):
        area[i].append(tmp_list[2*j])
        fish_pos[tmp_list[2*j]] = (i,j)
        fish_direct[tmp_list[j]] = tmp_list[2*j+1]
print(fish_pos)
print(fish_direct)
print(area)

shark_pos = (0,0)
shark_direct = fish_direct[area[0][0]]
fishes.remove(area[0][0])
area[0][0] = -1
eat_cnt = 1

def fish_turn(fish):
    fish_direct[fish] += 1
    if fish_direct[fish] > 8:
        fish_direct[fish] = 1

def fish_move(fish,x,y,nx,ny):
    if area[nx][ny] == 0:
        area[x][y] = 0
        area[nx][ny] = fish
        fish_pos[fish] = (nx,ny)
    else:
        other = area[nx][ny]
        area[x][y], area[nx][ny] = other, fish
        fish_pos[fish], fish_pos[other] = fish_pos[other], fish_pos[fish]
        fish_direct[fish], fish_direct[other] = fish_direct[other], fish_direct[fish]

while True:
    for fish in fishes:
        x, y = fish_pos[fish]
        direct = fish_direct[fish]
        nx = x + dx[direct-1]
        ny = y + dy[direct-1]
        if 0<=nx<4 and 0<=ny<4 and area[nx][ny]!=-1:
            fish_move(fish,x,y,nx,ny)
        else:
            for i in range(7):
                fish_turn(fish)
                nx = x + dx[direct-1]
                ny = y + dy[direct-1]
                if 0<=nx<4 and 0<=ny<4 and area[nx][ny]!=-1:
                    fish_move(fish,x,y,nx,ny)
                    break
    
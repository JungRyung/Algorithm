'''
TITLE   : 열쇠
URL     : https://www.acmicpc.net/problem/9328
DATE    : 21.10.06
'''
import sys
from collections import deque
import copy

dx = [-1,0,1,0]
dy = [0,-1,0,1]

def print_building(building, h, w):
    for b in building:
        print(''.join(b))

def bfs(building, q, visit, keys, h, w):
    q = deque(q)
    shifted = False
    new_keys = []
    cnt = 0
    while q:
        x, y = q.popleft()
        curr = building[x][y]
        if ord('a')<=ord(curr)<=ord('z'):
            shifted = True
            new_keys.append(curr)
            building[x][y] = '.'
        elif ord('A')<=ord(curr)<=ord('Z'):
            # 그 문을 열 수 있는 열쇠가 있는 경우
            if curr.lower() in keys:
                building[x][y] = '.'
            else:
                continue
        elif curr == '$':
            cnt += 1
            building[x][y] = '.'

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<h and 0<=ny<w and not visit[nx][ny] and building[nx][ny] != '*':
                curr = building[nx][ny]
                visit[nx][ny] = True
                q.append((nx,ny))
                
    keys = keys + new_keys
    return building, keys, cnt, shifted

for _ in range(int(sys.stdin.readline())):
    start_points = []
    q = []
    h, w = map(int, sys.stdin.readline().split())
    building = []
    visit = [[False]*w for __ in range(h)]
    ans = 0
    for i in range(h):
        tmp = list(sys.stdin.readline().strip())
        for j in range(w):
            if tmp[j] != '*' and (i==0 or i==h-1 or j==0 or j==w-1):
                q.append((i,j))
                visit[i][j] = True
        building.append(tmp)

    keys = []
    tmp = list(sys.stdin.readline().strip())
    if tmp[0] != '0':
        keys = tmp

    shifted = True
    while shifted:
        shifted = False
        visit_copy = copy.deepcopy(visit)
        q_copy = copy.deepcopy(q)
        building, keys, cnt, shifted = bfs(building, q_copy, visit_copy, keys, h, w)
        ans += cnt
        
    print(ans)

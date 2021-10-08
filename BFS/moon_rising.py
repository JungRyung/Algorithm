'''
TITLE   : 달이 차오른다, 가자.
URL     : https://www.acmicpc.net/problem/1194
DATE    : 21.10.08
'''
import sys
from collections import deque
import copy

dx = [-1,0,1,0]
dy = [0,-1,0,1]

keys = []

def print_building(building, h, w):
    for b in building:
        print(''.join(b))

def bfs(start, keys):
    x, y = start
    visit = [[False]*m for _ in range(n)]
    q = deque()
    shifted = False
    escaped = False
    new_keys = []
    cnt = 0
    visit[x][y] = True
    q.append((x,y,0))
    while q:
        x, y, c = q.popleft()
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
        elif curr == '1':
            cnt = c
            escaped = True

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m and not visit[nx][ny] and building[nx][ny] != '#':
                visit[nx][ny] = True
                q.append((nx,ny,c+1))
                
    keys = keys + new_keys
    return shifted, escaped, cnt, keys


n, m = map(int, sys.stdin.readline().split())
building = []
visit = [[False]*m for __ in range(n)]
ans = 0
for i in range(n):
    tmp = list(sys.stdin.readline().strip())
    for j in range(m):
        if tmp[j] == '0':
            start = (i,j)
            tmp[j] = '.'
    building.append(tmp)

shifted = True
ans = 0
while shifted:
    print(keys)
    shifted = False
    shifted, escaped, ans, keys = bfs(start, keys)
    if escaped:
        break
if escaped:
    print(ans)
else:
    print(-1)

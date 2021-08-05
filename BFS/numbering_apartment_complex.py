'''
TITLE   : 단지번호붙이기
URL     : https://www.acmicpc.net/problem/2667
DATE    : 21.08.05
'''
import sys

dx = [-1,0,1,0]
dy = [0,-1,0,1]

n = int(sys.stdin.readline())
complex = [list(sys.stdin.readline().strip()) for _ in range(n)]

visit = [[False]*n for _ in range(n)]
complex_list = []
number = 0
for i in range(n):
    for j in range(n):
        if not visit[i][j] and complex[i][j] == '1':
            visit[i][j] = True
            number += 1
            q = []
            q.append((i,j))
            cnt = 0
            while q:
                cnt += 1
                x, y = q.pop(0)
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0<=nx<n and 0<=ny<n and not visit[nx][ny] and complex[nx][ny] == '1':
                        visit[nx][ny] = True
                        q.append((nx,ny))
            complex_list.append(cnt)
complex_list.sort()
print(number)
for ans in complex_list:
    print(ans)
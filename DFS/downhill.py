'''
TITLE   : 내리막 길
URL     : https://www.acmicpc.net/problem/1520
DATE    : 21.07.25
'''
import sys
sys.setrecursionlimit(10 ** 8)

dx = [-1,0,1,0]
dy = [0,-1,0,1]

m, n = map(int, sys.stdin.readline().split())
hill = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
da = [[-1]*n for _ in range(m)]

def dfs(x,y):
    if x == m-1 and y == n-1:
        return 1
    if da[x][y] == -1:
        da[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<m and 0<=ny<n and hill[x][y] > hill[nx][ny]:
                da[x][y] += dfs(nx,ny)
    return da[x][y]

print(dfs(0,0))
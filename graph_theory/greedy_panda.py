'''
TITLE   : 욕심쟁이 판다
URL     : https://www.acmicpc.net/problem/1937
DATE    : 21.08.24
'''
import sys
sys.setrecursionlimit(10**9)

dx = [-1,0,1,0]
dy = [0,-1,0,1]

def dfs(x,y):
    if dp[x][y] < 0:
        dp[x][y] = 0
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0<=nx<n and 0<=ny<n and forest[x][y] < forest[nx][ny]:
                dp[x][y] = max(dp[x][y], dfs(nx,ny))
        dp[x][y] += 1
    return dp[x][y]
    
n = int(sys.stdin.readline())
forest = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dp = [[-1]*n for _ in range(n)]

ans = 0
for i in range(n):
    for j in range(n):
        ans = max(ans, dfs(i,j))
print(ans)

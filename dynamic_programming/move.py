'''
TITLE   : 이동하기
URL     : https://www.acmicpc.net/problem/11048
DATE    : 21.08.01
'''
import sys

n, m = map(int, sys.stdin.readline().split())
maze = []
maze.append([0]*(m+1))
for _ in range(n):
    maze.append([0] + list(map(int, sys.stdin.readline().split())))

dp = [[0]*(m+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,m+1):
        dp[i][j] = max(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + maze[i][j]
print(dp[n][m])
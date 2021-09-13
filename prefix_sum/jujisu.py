'''
TITLE   : 주지수
URL     : https://www.acmicpc.net/problem/15724
DATE    : 21.09.13
'''
import sys

n, m = map(int, sys.stdin.readline().split())
territory = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dp = [[0] * (m+1) for _ in range(n+1)]
for i in range(n):
    for j in range(m):
        dp[i+1][j+1] = dp[i][j+1] + dp[i+1][j] - dp[i][j] + territory[i][j]

k = int(sys.stdin.readline())
for _ in range(k):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    print(dp[x2][y2] - dp[x2][y1-1] - dp[x1-1][y2] + dp[x1-1][y1-1])